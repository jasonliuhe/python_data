import chart_studio.plotly as py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.io as pio
pio.renderers.default = "browser"

from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs, plot, iplot
colorscale='ylorbr'
projection={'type':'mercator'}

cf.go_offline()
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
print(df.head())
df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
print(df2.head())
df.iplot(kind='scatter',x='A',y='B',mode='markers',size=10)

