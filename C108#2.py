from numpy import fabs
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
heightlist = df["Height(Inches)"].tolist()
fig = ff.create_distplot([heightlist],["Height"],show_hist=False)
fig.show()
