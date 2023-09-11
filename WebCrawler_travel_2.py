# -*- coding: utf-8 -*-
"""
Created on Sun May 28 21:42:26 2023

@author: user
"""

#%% 繪製102-111年出國(目的地)人次統計長條圖

# import plotly_express as px
import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd


df = pd.read_csv('TravelDestination_102_111.csv', encoding='utf-8')
df.info()

trace1 = go.Bar(
    x=df["年別(Year)"], y=df["亞洲地區(Asia)"],
    name='Asia')

trace2 = go.Bar(
    x=df["年別(Year)"], y=df["非洲地區(Africa)"],
    name='Africa')

trace3 = go.Bar(
    x=df["年別(Year)"], y=df["美洲地區(Americas)"],
    name='Americas')

trace4 = go.Bar(
    x=df["年別(Year)"], y=df["大洋洲地區(Oceania)"],
    name='Oceania')

trace5 = go.Bar(
    x=df["年別(Year)"], y=df["歐洲地區(Europe)"],
    name='Europe')

trace6 = go.Bar(
    x=df["年別(Year)"], y=df["其他未列明(Unknow)"],
    name='Unknow')

trace7 = go.Bar(
    x=df["年別(Year)"], y=df["小計(Total)"],
    name='Total')


data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]
layout = go.Layout(title_text="102 - 111年出國(目的地)人次統計")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='OutboundTravelers_102_111.html')

