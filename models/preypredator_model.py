from models.models import AbstractModel, AbstractFactory
import matplotlib.pyplot as plt
from typing import List, Tuple, NoReturn
import numpy as np
import seaborn as sns

class PreyPredatorFactory(AbstractFactory):
    """
    Factory class for continuous systems 
    """
    def create_model(self):
        return PreyPredatorModel()

class PreyPredatorModel(AbstractModel):
    """
    Class for base prey-predator model 
    """
    def set_parameters(
        self,
        alpha1: float,
        alpha2: float,
        beta1: float,
        beta2: float,
        T: float,
        N: float,
        h: float,
        x: List[float],
        type_goal: str
        ) -> NoReturn:
        
        self.alpha1 = alpha1
        self.alpha2 = alpha2
        self.beta1 = beta1
        self.beta2 = beta2
        self.T = T
        self.M = np.arange(0, N, h)
        self.N = N
        self.h = h
        self.x = np.empty((0, 2), dtype=np.float32)
        self.x = np.vstack((self.x, x))
        self.type_goal = type_goal

    def calculate(self, **kwargs) -> Tuple[List[float], List[float]]:
        u = [0]

        for i in range(len(self.M)-1):
            if self.type_goal == "x1c":
                f1 = u[i] * self.x[i, 0] - self.beta1 * self.x[i, 0] * self.x[i, 1]
                f2 = -self.alpha2 * self.x[i, 1] + self.beta2 * self.x[i, 0] * self.x[i, 1]
                psi = self.x[i, 0] - kwargs['x1c']
                u.append(-psi / (self.T * self.x[i, 0]) + self.beta1 * self.x[i, 1])
            elif self.type_goal == "rho_d":
                f1 = u[i] * self.x[i, 0] - self.beta1 * self.x[i, 0] * self.x[i, 1]
                f2 = -self.alpha2 * self.x[i, 1] + self.beta2 * self.x[i, 0] * self.x[i, 1]
                psi = self.x[i, 0] + kwargs['rho'] * self.x[i, 1] - kwargs['d']
                u.append((self.T * self.beta1 * self.x[i, 0] * self.x[i, 1] - 
                          self.T*kwargs['rho']*f2 - psi) * (self.T * self.x[i, 0]) ** (-1))

            x1 = self.x[i, 0] + self.h * f1
            x2 = self.x[i, 1] + self.h * f2
            self.x = np.vstack((self.x, [x1, x2]))

        return self.x, u

    def plot(self, x: List[List[float]], u: List[float], **kwargs) -> NoReturn:        
        plt.figure(figsize=(10, 7))
        plt.grid(visible=True)
        plt.plot(self.M, x[:, 0], 'g', label=r'$x_{1}$')
        plt.plot(self.M, x[:, 1], 'b', label=r'$x_{2}$')

        v = np.linspace(round(np.min(self.x[:, 0])) - 10, round(np.max(self.x[:, 0])) + 10, 10)
        y = np.linspace(round(np.min(self.x[:, 1])) - 10, round(np.max(self.x[:, 1])) + 10, 10)
        X, Y = np.meshgrid(v, y)

        if "x1c" in kwargs:
            plt.plot(self.M, kwargs['x1c'] * np.ones(len(self.M)), 'k--', label=r"$x_{1}^{*}$")

            psi = X - kwargs['x1c']
            U = -psi / (self.T * X) + self.beta1 * Y
            Xdot = U * X - self.beta1 * X * Y
            Ydot = -self.alpha2 * Y + self.beta2 * X * Y 
        elif "rho" in kwargs and "d" in kwargs:
            x1s = self.alpha2 / self.beta2
            x2s = (-self.alpha2 + self.beta2 * kwargs['d']) / (kwargs['rho'] * self.beta2)
            plt.plot(self.M, x1s * np.ones(len(self.M)), 'k-.', label=r"$x_{1}^{*}$")
            plt.plot(self.M, x2s * np.ones(len(self.M)), 'k--', label=r"$x_{2}^{*}$")

            psi = X + kwargs['rho'] * Y - kwargs['d']
            Ydot = -self.alpha2 * Y + self.beta2 * X * Y
            U = (self.T * self.beta1 * X * Y - self.T*kwargs['rho']*Ydot - psi) * (self.T * X) ** (-1)
            Xdot = U * X - self.beta1 * X * Y 

        plt.ylim(bottom=0)
        sns.set_style('whitegrid')
        plt.xlim(0, self.N)
        plt.legend(loc="best")
        plt.xlabel('Время, дни')
        plt.ylabel('Популяция, ед/л')

        if "save_fig" in kwargs:
            plt.savefig(f"{kwargs['name_fig1']}.png")
            plt.savefig(f"{kwargs['name_fig1']}.svg")
            plt.savefig(f"{kwargs['name_fig1']}.eps")

        plt.figure(figsize=(10, 7))
        plt.plot(self.M, u, 'k', label=r'$u(t)$')
        sns.set_style('whitegrid')
        plt.xlim(0, self.N)
        plt.legend(loc="upper right")
        plt.xlabel('Время, дни')
        plt.ylabel('Управление')
        
        if "save_fig" in kwargs:
            plt.savefig(f"{kwargs['name_fig2']}.png")
            plt.savefig(f"{kwargs['name_fig2']}.svg")
            plt.savefig(f"{kwargs['name_fig2']}.eps")

        plt.figure(figsize=(10, 7))
        plt.streamplot(X, Y, Xdot, Ydot)
        plt.plot(self.x[0, 0], self.x[0, 1], 'bo', zorder=3, label="Начальное состояние")
        plt.plot(self.x[-1, 0], self.x[-1, 1], 'ro', zorder=2, label='Конечное состояние')
        plt.plot(self.x[:, 0], self.x[:, 1], 'r-', zorder=1, linewidth=3)
        plt.legend(loc="lower right")
        plt.xlabel(r'$x_{1}$')
        plt.ylabel(r'$x_{2}$')
        plt.xlim(left=0)
        plt.ylim(bottom=0)

        if "save_fig" in kwargs:
            plt.savefig(f"{kwargs['name_fig3']}.png")
            plt.savefig(f"{kwargs['name_fig3']}.svg")
            plt.savefig(f"{kwargs['name_fig3']}.eps")

        plt.show()