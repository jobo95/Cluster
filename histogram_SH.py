from mpl_toolkits.basemap import Basemap
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



time_start=1979
time_end=2016

leap_year=np.arange(1900,2112,4)

#bmus=np.load('bmu_KMeans_79-14.npy')
bmus=np.load('bmu_SOM_79-16_3times3.npy')
ice=bmus

djf_ice=np.empty(0)
mam_ice=np.empty(0)
jja_ice=np.empty(0)
son_ice=np.empty(0)


k=1
global l
l=0
i=time_start
while i<time_end:
    print (i)
    if (k is 1):
        end=31
        for jj in range(end):
            djf_ice=np.append(djf_ice,ice[l])
            l=l+1
        print (l)
        print ('jja')
        k=2

    if (k is 2):
        if ( i in leap_year):
            end=29
            print ('gggggggggggggggggggggggggggggggggggg')
        else:
            end=28

        for jj in range(end):
            djf_ice=np.append(djf_ice,ice[l])
            l=l+1
        print (l)
        print ('son')
        k=3

    if (k is 3):
        end=31
        for jj in range(end):
            mam_ice=np.append(mam_ice,ice[l])
            l=l+1
        print (l)
        print ('apr')
        k=4

    if (k is 4):
        end=30
        for jj in range(end):
            mam_ice=np.append(mam_ice,ice[l])
            l=l+1
        print (l)
        print ('may')
        k=5

    if (k is 5):
        end=31
        for jj in range(end):
            mam_ice=np.append(mam_ice,ice[l])
            l=l+1
        print (l)
        print ('jun')
        k=6

    if (k is 6):
        end=30
        for jj in range(end):
            jja_ice=np.append(jja_ice,ice[l])
            l=l+1
        print (l)
        print ('jul')
        k=7
    
    if (k is 7):
        end=31
        for jj in range(end):
            jja_ice=np.append(jja_ice,ice[l])
            l=l+1
        print (l)
        print ('aug')
        k=8
    
    if (k is 8):
        end=31
        for jj in range(end):
            jja_ice=np.append(jja_ice,ice[l])
            l=l+1
        print (l)
        print ('sep')
        k=9
    
    if (k is 9):
        end=30
        for jj in range(end):
            son_ice=np.append(son_ice,ice[l])
            l=l+1
        print (l)
        print ('oct')
        k=10
    
    if (k is 10):
        end=31
        for jj in range(end):
            son_ice=np.append(son_ice,ice[l])
            l=l+1
        print (l)
        print ('nov')
        k=11
    
    if (k is 11):
        end=30
        for jj in range(end):
            son_ice=np.append(son_ice,ice[l])
            l=l+1
        print (l)
        print ('dec')
        k=12
    
    if (k is 12):
        end=31
        for jj in range(end):
            djf_ice=np.append(djf_ice,ice[l])
            l=l+1
        print (l)
        print ('jan')
        k=1
    i=i+1 
#################################
####                    #########
####  HISTOGRAMME       #########
#################################
#data=[djf_ice,jja_ice,son_ice,djf_ice,jan_ice,jja_ice,son_ice,djf_ice]

djf_ice_bin=np.bincount(djf_ice.astype(int))/djf_ice.size
mam_ice_bin=np.bincount(mam_ice.astype(int))/mam_ice.size
jja_ice_bin=np.bincount(jja_ice.astype(int))/jja_ice.size
son_ice_bin=np.bincount(son_ice.astype(int))/son_ice.size
frequency=np.bincount(bmus.astype(int))/bmus.size

for jj in range(9):
    ax=plt.subplot(3,3,jj+1)
    
    frequency_ice = (djf_ice_bin[jj],mam_ice_bin[jj],jja_ice_bin[jj],son_ice_bin[jj])
    
    ind = np.arange(len(frequency_ice))  # the x locations for the groups
    width = 0.35  # the width of the bars
    
    rects1 = ax.bar(ind - width/2, frequency_ice, width,
                    color='SkyBlue', label='ice ('+str(time_start)+'-'+str(time_end-1)+')')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('relative frequency')
    ax.set_xticks(ind)
    ax.set_ylim(0,0.18)
    ax.set_xticklabels(('djf','mam', 'jja', 'son'))
    #ax.legend()
    plt.title(frequency[jj])


plt.tight_layout()
plt.show()
