# -*- coding: utf-8 -*-
"""
Created on Sun May 28 23:48:58 2023

@author: user
"""

#%% 繪製102-111年出國(目的地-亞洲)人次統計長條圖

import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd


df = pd.read_csv('TravelDestination_102_111_Asia.csv', encoding='utf-8')
df.info()

trace1 = go.Bar(
    x=df["年別"], y=df["香港Hong Kong"],
    name='Hong Kong')

trace2 = go.Bar(
    x=df["年別"], y=df["澳門 Macao"],
    name='Macao')

trace3 = go.Bar(
    x=df["年別"], y=df["大陸 Mainland China"],
    name='Mainland China')

trace4 = go.Bar(
    x=df["年別"], y=df["日本 Japan"],
    name='Japan')

trace5 = go.Bar(
    x=df["年別"], y=df["韓國 Korea"],
    name='Korea')

trace6 = go.Bar(
    x=df["年別"], y=df["新加坡 Singapore"],
    name='Singapore')

trace7 = go.Bar(
    x=df["年別"], y=df["馬來西亞 Malaysia"],
    name='Malaysia')

trace8 = go.Bar(
    x=df["年別"], y=df["泰國 Thailand"],
    name='Thailand')

trace9 = go.Bar(
    x=df["年別"], y=df["菲律賓 Philippines"],
    name='Philippines')

trace10 = go.Bar(
    x=df["年別"], y=df["印尼 Indonesia"],
    name='Indonesia')

trace11 = go.Bar(
    x=df["年別"], y=df["汶淶 Brunei"],
    name='Brunei')

trace12 = go.Bar(
    x=df["年別"], y=df["越南 Vietnam"],
    name='Vietnam')

trace13 = go.Bar(
    x=df["年別"], y=df["緬甸 Myanmar"],
    name='Myanmar')

trace14 = go.Bar(
    x=df["年別"], y=df["柬埔寨 Cambodia"],
    name='Cambodia')

trace15 = go.Bar(
    x=df["年別"], y=df["阿拉伯聯合大公國 United Arab Emirates"],
    name='United Arab Emirates')

trace16 = go.Bar(
    x=df["年別"], y=df["土耳其 Turkey"],
    name='Turkey')

trace17 = go.Bar(
    x=df["年別"], y=df["亞洲其他地區 Others"],
    name='Others')

data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9,
        trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17]
layout = go.Layout(title_text="102 - 111年出國(目的地-亞洲)人次統計")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='OutboundTravelers_102_111_Asia.html')