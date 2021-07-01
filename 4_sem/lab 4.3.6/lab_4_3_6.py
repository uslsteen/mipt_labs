import pandas as pd
import plotly.graph_objects as go

err_perc = 10

data = pd.read_csv('lab_436_1.csv')

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=data['n'],
    y=data['z_3'],
    name="data",
    
    error_y=dict(
        type='percent',
        value = err_perc,
        color = 'purple'
    ),
    marker=dict(color='purple', size=10),

))

fig.update_layout(title_text="Graph of vector")

fig.update_xaxes(title_text="size")
fig.update_yaxes(title_text="capacity")

fig.show()
