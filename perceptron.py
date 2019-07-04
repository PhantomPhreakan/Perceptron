# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
x1=[0,0,1,1]
x2=[0,1,0,1]
y=[0,0,0,1]
lr=0.2
theta=0.5
weights=[0.5,0.5,0.5]
i=0
count=0
while(count<4):
    yc=weights[0]+(weights[1]*x1[i%4])+(weights[2]*x2[i%4])
    if (yc>theta):
        yc=1
    else:
        yc=0
    if(yc != y[i%4]):
        count=0
        if(yc > y[i%4]):
            weights[0]=weights[0]-lr*1
            weights[1]=weights[1]-lr*x1[i%4]
            weights[2]=weights[2]-lr*x2[i%4]
        else:
            weights[0]=weights[0]+lr*1
            weights[1]=weights[1]+lr*x1[i%4]
            weights[2]=weights[2]+lr*x2[i%4]
        print("Epoch ",i," :",weights)
    else:
        count+=1
    i+=1
a=[]
b=[]
c=[]
d=[]  
print(weights)
for i in range(0,4):
    if(y[i]==0):
        a.append(x1[i])
        b.append(x2[i])
    else:
        c.append(x1[i])
        d.append(x2[i])
ypl=[]        
plt.scatter(a,b,color='r')
plt.scatter(c,d)



xintr=(theta-weights[0])/weights[1]
yintr=(theta-weights[0])/weights[2]

slope=-yintr/xintr
xx=plt.xlim()
yeq = []
for x in xx:
    yeq.append(yintr+slope*x)
plt.plot(xx,yeq)
plt.show()

    

