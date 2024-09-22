#%%
"""
Code for plotting TPP model. Goal - x1 - x1c
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import yaml
import pprint
import os
import sys

sys.path.append("..")
from models import TPPFactory

mpl.rcParams['figure.dpi'] = 300
plt.rcParams.update({'font.size': 20})

with open("params_x1c.yaml") as stream:
    try:
        params = yaml.safe_load(stream)
        pprint.pprint(params)
        params['x1c'] = params['gamma'] * params['mu'] / (params['beta'] - params['mu'] - params['theta'])
    except yaml.YAMLError as exc:
        print(exc)

factory = TPPFactory()
model = factory.create_model()
model.set_parameters(
    r=params['r'],
    K=params['K'],
    alpha=params['alpha'],
    beta=params['beta'],
    mu=params['mu'],
    gamma=params['gamma'],
    theta=params['theta'],
    T=params['T'],
    N=params['N'],
    h=params['h'],
    x=params['x'],
    type_goal='x1c'
)
x, u = model.calculate(x1c=params['x1c'])
model.plot(x, u, x1c=params['x1c'], save_fig=True, name_fig1="3.18", name_fig2="3.19")

#%%
"""
Code for plotting TPP model. Goal - x1 + rho * x2 - d
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import yaml
import pprint
import os
import sys

sys.path.append("..")
from models import TPPFactory

mpl.rcParams['figure.dpi'] = 300
plt.rcParams.update({'font.size': 20})

with open("params_rho_d.yaml") as stream:
    try:
        params = yaml.safe_load(stream)
        pprint.pprint(params)
    except yaml.YAMLError as exc:
        print(exc)

factory = TPPFactory()
model = factory.create_model()
model.set_parameters(
    r=params['r'],
    K=params['K'],
    alpha=params['alpha'],
    beta=params['beta'],
    mu=params['mu'],
    gamma=params['gamma'],
    theta=params['theta'],
    T=params['T'],
    N=params['N'],
    h=params['h'],
    x=params['x'],
    type_goal='rho_d'
)
x, u = model.calculate(rho=params['rho'], d=params['d'])
model.plot(x, u, rho=params['rho'], d=params['d'], save_fig=True, name_fig1="3.21", name_fig2="3.22")