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
time_change=2000
time_end=2016
t_hice=time_change-time_start
ar_slice=int(((t_hice)*(31+31+28+31)+5))

leap_year=np.arange(1900,2112,4)

#bmus=np.load('bmu_KMeans_79-14.npy')
bmus=np.load('bmu_SOM_79-16_4times4.npy')
hice=bmus[0:ar_slice]
lice=bmus[ar_slice:]

jan_hice=np.empty(0)
feb_hice=np.empty(0)
mar_hice=np.empty(0)
dec_hice=np.empty(0)

jan_lice=np.empty(0)
feb_lice=np.empty(0)
mar_lice=np.empty(0)
dec_lice=np.empty(0)

k=1
global l
l=0
i=time_start
while i<time_change:
    print (i)
    if (k is 1):
        end=31
        for jj in range(end):
            jan_hice=np.append(jan_hice,hice[l])
            l=l+1
        print (l)
        print ('feb')
        k=2

    if (k is 2):
        if ( i in leap_year):
            end=29
            print ('gggggggggggggggggggggggggggggggggggg')
        else:
            end=28

        for jj in range(end):
            feb_hice=np.append(feb_hice,hice[l])
            l=l+1
        print (l)
        print ('mar')
        k=3

    if (k is 3):
        end=31
        for jj in range(end):
            mar_hice=np.append(mar_hice,hice[l])
            l=l+1
        print (l)
        print ('dec')
        k=4

    if (k is 4):
        end=31
        for jj in range(end):
            dec_hice=np.append(dec_hice,hice[l])
            l=l+1
        print (l)
        print ('jan')
        k=1
    i=i+1 
    

    
#low ice
k=1
l=0
i=time_change
while i<=time_end:
    print (i)
    if (k is 1):
        end=31
        for jj in range(end):
            jan_lice=np.append(jan_lice,lice[l])
            l=l+1
        print (l)
        print ('feb')
        k=2

    if (k is 2):
        if ( i in leap_year):
            end=29
        else:
            end=28
        for jj in range(end):
            feb_lice=np.append(feb_lice,lice[l])
            l=l+1
        print (l)
        print ('mar')
        k=3

    if (k is 3):
        end=31
        for jj in range(end):
            mar_lice=np.append(mar_lice,lice[l])
            l=l+1
        print (l)
        print ('dec')
        k=4

    if (k is 4):
        end=31
        for jj in range(end):
            dec_lice=np.append(dec_lice,lice[l])
            l=l+1
        print (l)
        print ('jan')
        k=1
    i=i+1 
    

#################################
####                    #########
####  HISTOGRAMME       #########
#################################
data=[jan_hice,feb_hice,mar_hice,dec_hice,jan_lice,feb_lice,mar_lice,dec_lice]

jan_hice_bin=np.bincount(jan_hice.astype(int))/jan_hice.size
feb_hice_bin=np.bincount(feb_hice.astype(int))/feb_hice.size
mar_hice_bin=np.bincount(mar_hice.astype(int))/mar_hice.size
dec_hice_bin=np.bincount(dec_hice.astype(int))/dec_hice.size

jan_lice_bin=np.bincount(jan_lice.astype(int))/jan_lice.size
feb_lice_bin=np.bincount(feb_lice.astype(int))/feb_lice.size
mar_lice_bin=np.bincount(mar_lice.astype(int))/mar_lice.size
dec_lice_bin=np.bincount(dec_lice.astype(int))/dec_lice.size

ax=plt.subplot(2,3,1)

frequency_lice = (dec_lice_bin[0],jan_lice_bin[0],feb_lice_bin[0],mar_lice_bin[0])
frequency_hice = (dec_hice_bin[0],jan_hice_bin[0],feb_hice_bin[0],mar_hice_bin[0])

ind = np.arange(len(frequency_lice))  # the x locations for the groups
width = 0.35  # the width of the bars

rects1 = ax.bar(ind - width/2, frequency_hice, width,
                color='SkyBlue', label='hice ('+str(time_start)+'-'+str(time_change-1)+')')
rects2 = ax.bar(ind + width/2, frequency_lice, width,
                color='IndianRed', label='lice')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('relative frequency')
ax.set_xticks(ind)
ax.set_xticklabels(('dec','jan', 'feb', 'mar'))
ax.legend()
plt.title('0')
#########################
ax=plt.subplot(2,3,2)

frequency_lice = (dec_lice_bin[1],jan_lice_bin[1],feb_lice_bin[1],mar_lice_bin[1])
frequency_hice = (dec_hice_bin[1],jan_hice_bin[1],feb_hice_bin[1],mar_hice_bin[1])

ind = np.arange(len(frequency_lice))  # the x locations for the groups
width = 0.35  # the width of the bars

rects1 = ax.bar(ind - width/2, frequency_hice, width,
                color='SkyBlue', label='hice')
rects2 = ax.bar(ind + width/2, frequency_lice, width,
                color='IndianRed', label='lice')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('relative frequency')
ax.set_xticks(ind)
ax.set_xticklabels(('dec','jan', 'feb', 'mar'))
ax.legend()

plt.title('1')

####################################
ax=plt.subplot(2,3,3)

frequency_lice = (dec_lice_bin[2],jan_lice_bin[2],feb_lice_bin[2],mar_lice_bin[2])
frequency_hice = (dec_hice_bin[2],jan_hice_bin[2],feb_hice_bin[2],mar_hice_bin[2])

ind = np.arange(len(frequency_lice))  # the x locations for the groups
width = 0.35  # the width of the bars

rects1 = ax.bar(ind - width/2, frequency_hice, width,
                color='SkyBlue', label='hice')
rects2 = ax.bar(ind + width/2, frequency_lice, width,
                color='IndianRed', label='lice')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('relative frequency')
ax.set_xticks(ind)
ax.set_xticklabels(('dec','jan', 'feb', 'mar'))
ax.legend()
plt.title('2')

#############################################
ax=plt.subplot(2,3,4)

frequency_lice = (dec_lice_bin[3],jan_lice_bin[3],feb_lice_bin[3],mar_lice_bin[3])
frequency_hice = (dec_hice_bin[3],jan_hice_bin[3],feb_hice_bin[3],mar_hice_bin[3])

ind = np.arange(len(frequency_lice))  # the x locations for the groups
width = 0.35  # the width of the bars

rects1 = ax.bar(ind - width/2, frequency_hice, width,
                color='SkyBlue', label='hice')
rects2 = ax.bar(ind + width/2, frequency_lice, width,
                color='IndianRed', label='lice')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('relative frequency')
ax.set_xticks(ind)
ax.set_xticklabels(('dec','jan', 'feb', 'mar'))
ax.legend()
plt.title('3')

####################################################
ax=plt.subplot(2,3,5)

frequency_lice = (dec_lice_bin[4],jan_lice_bin[4],feb_lice_bin[4],mar_lice_bin[4])
frequency_hice = (dec_hice_bin[4],jan_hice_bin[4],feb_hice_bin[4],mar_hice_bin[4])

ind = np.arange(len(frequency_lice))  # the x locations for the groups
width = 0.35  # the width of the bars

rects1 = ax.bar(ind - width/2, frequency_hice, width,
                color='SkyBlue', label='hice')
rects2 = ax.bar(ind + width/2, frequency_lice, width,
                color='IndianRed', label='lice')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('relative frequency')
ax.set_xticks(ind)
ax.set_xticklabels(('dec','jan', 'feb', 'mar'))
ax.legend()
plt.title('4')
plt.tight_layout()
plt.show()
