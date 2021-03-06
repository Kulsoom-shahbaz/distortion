# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:52:06 2018

@author: Kulsoom
"""

"""
Reference Citation
- Author: Trevor Tomesh
- Date: 26 october 2018
- Title of program: Reading the .dat file in digital Filters in python 
- Code version: 1.1
- Type: Computer program - Digital filters 
- Source: Schoology Application
"""
import pandas as pd
import numpy as np
import random #for random integers
import math
import matplotlib.pyplot as plt #for plotting graph

data = pd.read_csv("a.dat", header=None, delimiter=r"\s+")

x = data[0]
y = data[1]
time_list = []
amp_list = []
zlist = []
# populate the lists with the contents of the columns read
fs=44100
delay=1
ran=1
freq=0.312    
for i in range(0,int(len(x))):
   time_list.append(float(x.iloc[i]))
   amp_list.append(float(y.iloc[i]))   
f = open("out.dat", "w")
i=0

#DISTORTION hard clipping --> Implemented
while (i<=len(y)-1):  # while loop reads the signal until the last bit
    if(amp_list[i]>0.50): #if amplitude is greater than 0.05 then cut it off and put equal to 0.05
        amp_list[i]=0.50 
    elif(amp_list[i]<-0.50):  #if amplitude is greater than- 0.05 then cut it off and put equal to 0.05
        amp_list[i]=-0.50
    i=i+1 #next iteration

for i in range(0,(len(y))):
    amp_list[i]=amp_list[i]*10.5 #amplify the signal 

#Plot the graphs in time - amplitude domain
plt.xlabel('time')
plt.ylabel('amplitude')   
plt.plot(time_list,y)
plt.axis([0.00,0.02,-1,1])
plt.show()
plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(time_list,amp_list)
plt.axis([0.00,0.02,-1,1])
plt.show()
f.write("; Sample Rate "+str(44100/8)+"\n")
f.write("; Channels 1"+"\n")
# simple inverse filter
for i in range(0,int(len(time_list)-2)):
f.write(str(time_list[i])+"   "+str(((amp_list[i])))+"\n")  
f.close() 
