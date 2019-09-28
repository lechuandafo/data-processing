# -*- coding: utf-8 -*-


import pandas as pd
import folium


m = folium.Map([28.68,115.89], zoom_start=8)  #中心区域的确定
posi = pd.read_csv('driving_data.csv',header = 0)
num = len(posi) 
lng = posi["lng"].values # 获取经度值
lat = posi["lat"].values # 获取维度之维度值

location = [[lat[i],lng[i]] for i in range(len(lat))]
route = folium.PolyLine(    #polyline方法为将坐标用线段形式连接起来
    location,    #将坐标点连接起来
    #weight=1000,  #线的大小为3
    color='purple',  #线的颜色为黑色
    #opacity=0.8    #线的透明度
).add_to(m)    #将这条线添加到刚才的区域m内
m.save("driving_data.html")  #将结果以HTML形式保存到桌面上

