# -*- coding: utf-8 -*-
"""
Created on Sun May 28 23:22:35 2023

@author: user
"""

#%% 繪製112年 1月-3月 出國(目的地)人次統計長條圖

import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd


df = pd.read_csv('TravelDestination_112_1_3.csv', encoding='utf-8')
df.info()
df_n = df.drop(0, axis = 0)
print(df_n)

df_n["亞洲地區"] = pd.to_numeric(df_n["亞洲地區"])
df_n["非洲地區"] = pd.to_numeric(df_n["非洲地區"])
df_n["美洲地區"] = pd.to_numeric(df_n["美洲地區"])
df_n["大洋洲地區"] = pd.to_numeric(df_n["大洋洲地區"])
df_n["歐洲地區"] = pd.to_numeric(df_n["歐洲地區"])
df_n["其他未列明"] = pd.to_numeric(df_n["其他未列明"])
df_n["小計"] = pd.to_numeric(df_n["小計"])
df_n.info()

trace1 = go.Bar(
    x=df_n["年別月份"], y=df_n["亞洲地區"],
    name='Asia')

trace2 = go.Bar(
    x=df_n["年別月份"], y=df_n["非洲地區"],
    name='Africa')

trace3 = go.Bar(
    x=df_n["年別月份"], y=df_n["美洲地區"],
    name='Americas')

trace4 = go.Bar(
    x=df_n["年別月份"], y=df_n["大洋洲地區"],
    name='Oceania')

trace5 = go.Bar(
    x=df_n["年別月份"], y=df_n["歐洲地區"],
    name='Europe')

trace6 = go.Bar(
    x=df_n["年別月份"], y=df_n["其他未列明"],
    name='Unknow')

trace7 = go.Bar(
    x=df_n["年別月份"], y=df_n["小計"],
    name='Total')


data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]
layout = go.Layout(title_text="112年 1月 - 3月 出國(目的地)人次統計")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='OutboundTravelers_112_1_3.html')
