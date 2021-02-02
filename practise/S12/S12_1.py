# import plotly.offline as py
# import cufflinks as cf
# import pandas as pd
# import numpy as np
# 
# 
# df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
# 
# py.plot([{
#     'x': df.index,
#     'y': df[col],
#     'name': col
# 
# }for col in df.columns], filename='simple-line.html')
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'png'

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show();
