# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:09:25 2019

@author: saich
"""

import numpy as np
import random
random.seed(30)

import scipy.io
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


Numpyfile= scipy.io.loadmat("AllSamples.mat") 
x=Numpyfile['AllSamples']

#print(x)

f = plt.figure(2)
plt.figure(figsize=(10,10))
plt.scatter(x[:,0], x[:,1])
plt.title('input data')
plt.show()
def centroids(k):
    
    indexes=random.sample(set(range(len(x))),k)
    return(x[indexes])
    
            
    
#k=7    
meand=[0,0]

def distance(a,b):
        d=(a[0]-b[0])**2+(a[1]-b[1])**2
        return d
    
#indexes=random.sample(set(range(len(x))),1)
#centroidx=x[indexes]


for k in range(2,11):
    #centroid=centroids(k)
    
    #indexes=random.sample(set(range(len(x))),k)
    #print(indexes)
    
    
    centroid1=centroids(k)
   # print(centroid1)
    
   
    print(centroid1)
    present=centroid1
    
    prev=present+1
    
    
    
    #for i in range(k):
    #    cluster[i] = []
    #   # cluster_ = []
    
    print((present==prev).all())
    count=0
    while(not (present==prev).all()):
        #print(count+1)
        count=count+1
        cluster=[[]for i in range(k)]
        for i in range(x.shape[0]):
            d=[]
            for j in range(present.shape[0]):
                d.append(distance(x[i],present[j]))
            m=d.index(min(d))
            cluster[m].append(x[i])
        
        
        for q in range(k):
            
            
            cluster[q] = np.asarray(cluster[q]) 
            
        prev = np.empty_like (present)
        prev[:]=present
        present=np.empty_like(prev)
        
        for p in range(k):
            present[p]=cluster[p].mean(axis=0)
        
        
    print(count)
            
    print((present==prev).all())
        
        
    #    d1=distance(x[i],present[0])
    #    d2=distance(x[i],present[1])
    #    if d1<=d2:
    #        cluster[0].append(x[i])
    #    else:
    #        cluster[1].append(x[i])
    
    #for i in range(k):
    #        
    #    cluster[i] = np.asarray(cluster[i])
    #cluster[1]= np.asarray(cluster[1])
            
    
    #plt.subplot(2,5,k-1)
    f = plt.figure(1)
    
    plt.figure(figsize=(10,10))
    for i in range(k):
        
        plt.scatter(cluster[i][:,0],cluster[i][:,1],cmap='viridis',label = i+1)
        
    #plt.scatter(cluster[1][:,0],cluster[1][:,1],label = 'cluster2')
    plt.legend()
    plt.show()
    sum=0
    for i in range(k):
        #for j in cluster[i]:
            #print(present[i])
#            sum=sum+distance(j,present[i])
            
        sqsum=np.square(present[i]-cluster[i])
        sum=np.sum(sqsum)+sum
                
            
    meand.append(sum)
    prev = np.empty_like (present)
    
    present=np.empty_like(prev)
    centroid1=np.empty_like(prev)
    
    
    
plt.figure(figsize=(10,10))           
Z=np.arange(2,k+1)    
plt.plot(Z,meand[2:])  
#ew = np.array[[]]
plt.show
