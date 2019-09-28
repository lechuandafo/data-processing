# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

#-----底图绘制
matplotlib.rcParams['toolbar'] = 'None'
fig = plt.figure(figsize=(12, 12), edgecolor='w')
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])

##中国地图
#m = Basemap(projection='lcc', 
#            llcrnrlon=80.33, 
#            llcrnrlat=3.01, 
#            urcrnrlon=138.16, 
#            urcrnrlat=56.123,
#            resolution='h',
#            lat_0 = 42.5,
#            lon_0=120,
#            ax=ax1,
#            area_thresh=10000)

#江西地图
m = Basemap(projection='merc', #投影方式
            llcrnrlon=113.5,#起始经度 113.5
            llcrnrlat=24.5, #起始纬度 24.5
            urcrnrlon=117.5, #终止经度117.5
            urcrnrlat=30.05,#终止纬度30.05
            resolution='h',#设置边界的详细程度,h是高
            lat_0 = 28.68,
            lon_0=115.89,
            ax=ax1,
            area_thresh=10000)

island_col = '#FFDEAD' #陆地颜色
lake_col = '#87CEFA' #湖水颜色
line_col = 'purple' #轨迹颜色
m.fillcontinents(color = island_col,lake_color = lake_col)
m.drawstates()        # 绘制州
m.drawcoastlines()    # 绘制海岸线
m.drawcountries()     # 绘制国家

m.drawparallels(np.arange(24,31,1),labels=[1,1,0,1])
# 画出纬线， 在北纬10度到90度区间内以20度为单位， 纬度标记在图形左右和下测
m.drawmeridians(np.arange(112,120,1),labels=[1,1,0,1])
# 画出经线， 从西经180度到东经180度区间内以30度为单位， 经度标记在图形左右和下测

shp_info = m.readshapefile("./CHN_adm_shp/CHN_adm1",'states',drawbounds=True) # CHN_adm1的数据是中国各省区域

#-----数据读取
posi = pd.read_csv('driving_data.csv',header = 0)
num = len(posi) 
lng = posi["lng"].values # 获取经度值
lat = posi["lat"].values # 获取纬度值

x,y = m(lng,lat)

#-----轨迹绘制
#散点
m.scatter(x, y, s=1, c='r', alpha=0.7, zorder=10)

#连线
#m.plot(x,y,marker=None,color = line_col,linewidth = 1)

