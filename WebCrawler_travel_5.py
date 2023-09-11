# -*- coding: utf-8 -*-
"""
Created on Mon May 29 00:19:03 2023

@author: user
"""

#%% 繪製112年 1月 - 3月 出國(目的地-亞洲)人次統計長條圖

import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd


df = pd.read_csv('TravelDestination_112_1_3_Asia.csv', encoding='utf-8')
df.info()
# print(df)
df = df.drop(0, axis = 0)
# print(df)

df["香港"] = pd.to_numeric(df["香港"])
df["日本"] = pd.to_numeric(df["日本"])
df["韓國"] = pd.to_numeric(df["韓國"])
df["中國大陸"] = pd.to_numeric(df["中國大陸"])
df["澳門"] = pd.to_numeric(df["澳門"])
df["越南"] = pd.to_numeric(df["越南"])
df["泰國"] = pd.to_numeric(df["泰國"])
df["馬來西亞"] = pd.to_numeric(df["馬來西亞"])
df["新加坡"] = pd.to_numeric(df["新加坡"])
df["菲律賓"] = pd.to_numeric(df["菲律賓"])
df["汶萊"] = pd.to_numeric(df["汶萊"])
df["印尼"] = pd.to_numeric(df["印尼"])
df["柬埔寨"] = pd.to_numeric(df["柬埔寨"])
df["緬甸"] = pd.to_numeric(df["緬甸"])
df["阿拉伯聯合大公國"] = pd.to_numeric(df["阿拉伯聯合大公國"])
df["土耳其"] = pd.to_numeric(df["土耳其"])
df["小計"] = pd.to_numeric(df["小計"])
df.info()

trace1 = go.Bar(
    x=df["年別月份"], y=df["香港"],
    name='Hong Kong')

trace2 = go.Bar(
    x=df["年別月份"], y=df["澳門"],
    name='Macao')

trace3 = go.Bar(
    x=df["年別月份"], y=df["中國大陸"],
    name='Mainland China')

trace4 = go.Bar(
    x=df["年別月份"], y=df["日本"],
    name='Japan')

trace5 = go.Bar(
    x=df["年別月份"], y=df["韓國"],
    name='Korea')

trace6 = go.Bar(
    x=df["年別月份"], y=df["新加坡"],
    name='Singapore')

trace7 = go.Bar(
    x=df["年別月份"], y=df["馬來西亞"],
    name='Malaysia')

trace8 = go.Bar(
    x=df["年別月份"], y=df["泰國"],
    name='Thailand')

trace9 = go.Bar(
    x=df["年別月份"], y=df["菲律賓"],
    name='Philippines')

trace10 = go.Bar(
    x=df["年別月份"], y=df["印尼"],
    name='Indonesia')

trace11 = go.Bar(
    x=df["年別月份"], y=df["汶萊"],
    name='Brunei')

trace12 = go.Bar(
    x=df["年別月份"], y=df["越南"],
    name='Vietnam')

trace13 = go.Bar(
    x=df["年別月份"], y=df["緬甸"],
    name='Myanmar')

trace14 = go.Bar(
    x=df["年別月份"], y=df["柬埔寨"],
    name='Cambodia')

trace15 = go.Bar(
    x=df["年別月份"], y=df["阿拉伯聯合大公國"],
    name='United Arab Emirates')

trace16 = go.Bar(
    x=df["年別月份"], y=df["土耳其"],
    name='Turkey')

trace17 = go.Bar(
    x=df["年別月份"], y=df["小計"],
    name='Total')

data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9,
        trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17]
layout = go.Layout(title_text="112年 1月 - 3月 出國(目的地-亞洲)人次統計")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='OutboundTravelers_112_1_3_Asia.html')