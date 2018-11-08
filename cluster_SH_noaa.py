#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:49:00 2018

@author: jriebold
"""

from mpl_toolkits.basemap import Basemap
from pca import EOF
from matplotlib import colors
import numpy as np
import sys
sys.path[0]='/home/jriebold/SOMPY-master'
import sompy
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import netCDF4
#from cdo import *

path='/model2/jriebold/model3/paleo/NOAA_20CR/daymean_1979-2014/'
#path='/model2/jriebold/model3/paleo/NOAA_20CR/daymean_1908-1943/'
file_name='slp.N_djfm_aac.nc'

dataset= netCDF4.Dataset(path+file_name)
lon_nc=list(dataset.variables.keys())[1]
lat_nc=list(dataset.variables.keys())[2]
variable_nc=list(dataset.variables.keys())[3]

var=dataset.variables[variable_nc]
lat=dataset.variables[lat_nc]
lon=dataset.variables[lon_nc]

dx=np.abs(lon[0]-lon[-1])/(lon.size*1.0-1)
dy=np.abs(lat[0]-lat[-1])/(lat.size*1.0-1)


data=np.reshape(var,(var.shape[0],var.shape[1]*var.shape[2]))

periods=1
mapsize=5

x=np.linspace(lon[0],lon[-1],lon.size)
y=np.linspace(lat[0],lat[-1],lat.size)
cos=np.sqrt(np.cos((np.pi/180)*(np.abs(y))))

xx,yy=np.meshgrid(x,y)

data_backup=np.copy(data)

for i in range(periods):
    fig=plt.figure(i)

    interval=[(data_backup[:,0].size/periods)*(i),(data_backup[:,0].size/periods)*(i+1)]
    data=data_backup[int(interval[0]):int(interval[1]),:]

    t=0
   # for k in range(data.shape[1]):
   #     data[:,k]=data[:,k]*cos[t]
   #     
   #     if k>=(t+1)*lon[:].size:
   #         t=t+1

   # pca=PCA(n_components=5)
   # pca.fit(data)
   # data=pca.transform(data)
    

    ####################
    ######         #####
    ######  SOM    #####
    ####################
    #som = sompy.SOMFactory.build(data,mask=None,mapsize=[1,5], mapshape='planar', lattice='rect', normalization=None, 		initialization='random', neighborhood='gaussian', training='batch', name='sompy') 
    #som.train(n_job=1,train_rough_len=15,train_finetune_len=30,train_finetune_radiusin=3,train_finetune_radiusfin=0.10,train_rough_radiusin=200,train_rough_radiusfin=2,verbose=None)
    #    
    #a=som.codebook.matrix

    #####################
    #######          ####
    ###### KMeans    ####
    #####################

    means=KMeans(n_clusters=5,n_init=10,max_iter=400,algorithm='elkan').fit(data)
    a=means.cluster_centers_


    #a=pca.inverse_transform(a)

    for j in range(mapsize):

        plt.subplot(2,3,j+1)
        plot_dat=a[j,:].reshape((lat.size,lon.size))


        m = Basemap(projection='npstere',boundinglat=30,round=True,lon_0=0,resolution='c')
        #m=Basemap(projection='stere',width=16000000,height=7000000,lat_0=59,lon_0=0)
          
        m.drawcoastlines(linewidth=0.5)
        m.drawparallels(np.arange(30.,88.,20.))
        m.drawmeridians([-90,-60,-30,0,30,60,90],labels=[1,1,1,1])
        m 
        g=m.contourf(xx, yy, plot_dat,cmap='seismic',linewidths=4.5,levels=[-20,-10,-5,-3,-2,-1,1,2,3,5,10,20],latlon=True)
        m.contour(xx, yy, plot_dat,cmap='seismic',linewidths=0.8,levels=[-20,-10,-5,-3,-2,-1,1,2,3,5,10,20],latlon=True)
        plt.title(j)

        s=fig.colorbar(g,ticks=[-20,-10,-5,-3,-2,-1,1,2,3,5,10,20],orientation="horizontal")
        s.set_label('[hPa]')
plt.tight_layout()
#np.save('bmu_SOM_08-43_alldim',som._bmu[0])
#np.save('bmu_SOM_79-14_5dim',som._bmu[0])
#np.save('bmu_KMeans_08-43_alldim',means.labels_)
#np.save('bmu_KMeans_79-14_alldim',means.labels_)
#np.save('bmu_SOM_08-43_alldim',som._bmu[0])
plt.show()

