#%%
"""
Code for plotting prey-predator model with goal - x1 - x1c
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import yaml
import pprint
import os
import sys

sys.path.append("..")
from models import PreyPredatorFactory

mpl.rcParams['figure.dpi'] = 300
plt.rcParams.update({'font.size': 20})
plt.rcParams['svg.fonttype'] = 'none'

with open("params_x1c.yaml") as stream:
    try:
        params = yaml.safe_load(stream)
        pprint.pprint(params)
        params['x1c'] = params['alpha2'] / params['beta2']
    except yaml.YAMLError as exc:
        print(exc)

factory = PreyPredatorFactory()
model = factory.create_model()
model.set_parameters(
    alpha1=params['alpha1'],
    alpha2=params['alpha2'],
    beta1=params['beta1'],
    beta2=params['beta2'],
    T=params['T'],
    N=params['N'],
    h=params['h'],
    x=params['x'],
    type_goal=params['type_goal']
)
x, u = model.calculate(x1c=params['x1c'])
model.plot(x, u, x1c=params['x1c'], save_fig=True, name_fig1="3.1", name_fig2="3.2")

#%%
"""
Code for plotting prey-predator model with goal - x1 + rho*x2 - d
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import yaml
import pprint
import os
import sys

sys.path.append("..")
from models import PreyPredatorFactory

mpl.rcParams['figure.dpi'] = 300
plt.rcParams.update({'font.size': 20})
plt.rcParams['svg.fonttype'] = 'none'

with open("params_rho_d.yaml") as stream:
    try:
        params = yaml.safe_load(stream)
        pprint.pprint(params)
    except yaml.YAMLError as exc:
        print(exc)

factory = PreyPredatorFactory()
model = factory.create_model()
model.set_parameters(
    alpha1=params['alpha1'],
    alpha2=params['alpha2'],
    beta1=params['beta1'],
    beta2=params['beta2'],
    T=params['T'],
    N=params['N'],
    h=params['h'],
    x=params['x'],
    type_goal=params['type_goal']
)
x, u = model.calculate(rho=params['rho'], d=params['d'])
model.plot(x, u, rho=params['rho'], d=params['d'], save_fig=True, name_fig1="3.4", name_fig2="3.5")

#%%
"""
Code for plotting prey-predator model with big phase. Goal - x1 - x1c
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import yaml
import pprint
import os
import sys

sys.path.append("..")
from models import PreyPredatorBigPhaseFactory

mpl.rcParams['figure.dpi'] = 300
plt.rcParams.update({'font.size': 20})
plt.rcParams['svg.fonttype'] = 'none'

with open("params_bigphase.yaml") as stream:
    try:
        params = yaml.safe_load(stream)
        pprint.pprint(params)
        params['x1c'] = params['alpha2'] / params['beta2']
    except yaml.YAMLError as exc:
        print(exc)

factory = PreyPredatorBigPhaseFactory()
model = factory.create_model()
model.set_parameters(
    alpha1=params['alpha1'],
    alpha2=params['alpha2'],
    beta1=params['beta1'],
    beta2=params['beta2'],
    T1=params['T1'],
    T2=params['T2'],
    x1c=params['x1c'],
    N=params['N'],
    h=params['h'],
    x=params['x'],
)
x, u = model.calculate(x1c=params['x1c'])
model.plot(x, u, x1c=params['x1c'], save_fig=True, name_fig1="3.7", name_fig2="3.8")