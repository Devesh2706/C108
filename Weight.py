import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
Weightlist = df["Weight(Pounds)"].tolist()
fig = ff.create_distplot([Weightlist],["Weight(Pounds)"],show_hist=False)

fig.show()
