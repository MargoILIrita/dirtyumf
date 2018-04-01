import plotly.offline as py
import numpy as np
import lastsemester as ls

def drawUIT():
    data = [dict(
        visible=False,
        line=dict(color='00CED1', width=6),
        name='t = ' + str(1),
        x=np.arange(0, 5, 0.1),
        y=ls.allinone(1,0.1))]

    steps = []
    for i in range(len(data)):
        step = dict(
            method='restyle',
            args=['visible', [False] * len(data)],
        )
        step['args'][1][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Time: "},
        pad={"t": 50},
        steps=steps
    )]

    layout = dict(sliders=sliders)

    fig = dict(data=data, layout=layout)

    py.plot(fig, filename='Temperature in time')

drawUIT()