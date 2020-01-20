# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:09:25 2019

@author: saich
"""

import numpy as np
import random
random.seed(30) #can remove seed to get random values every time
#random.seed(20)

import scipy.io
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


Numpyfile= scipy.io.loadmat("AllSamples.mat") 
x=Numpyfile['AllSamples']



f = plt.figure(2)
plt.figure(figsize=(10,10))
plt.scatter(x[:,0], x[:,1])
plt.title('input data')
plt.show()       #plotting the given samples
 
meand=[0,0]

def distance(a,b):          #defining distance function for calculating distance between points
        d=(a[0]-b[0])**2+(a[1]-b[1])**2
        return d


for k in range(2,11):
    
    
    indexes=random.sample(((list(x))),k) #selecting k random samplse as the inital centroids
    
    centroid=np.array(indexes)
    print("inital centroids for K="+str(k)) #printing initial centroids
    print(centroid)
    present=centroid
    
    
    prev=present+1     #taking prev such that prev!=present
    
    
    
    
    count=0
    while(not (present==prev).all()): #checks if the prev centroids equal present centroids
        
        count=count+1
        cluster=[[]for i in range(k)] #creating list of lists to add the samples belonginf to each cluster
        for i in range(x.shape[0]):
            
            d=[]
            for j in range(present.shape[0]):
                
                d.append(distance(x[i],present[j]))
            m=d.index(min(d)) #calculating distance from all the centroids to each sample and selecting closest centroid
            cluster[m].append(x[i])
        
        
        for q in range(k):
            
            cluster[q] = np.asarray(cluster[q])  #changing list of lists to nparray
            
        
        prev[:]=present #making the old centroid as present
        
        for p in range(k):
            
            present[p]=cluster[p].mean(axis=0) #calcuting the new centroid by taking mean of the cluster's samples
        
        
    print(count)
   
    print((present==prev).all())
    print("final centroids for K="+str(k))        #printing the final obtained centroids   
    print((present))    #printing the final obtained centroids
    f = plt.figure(1)
    
    plt.figure(figsize=(10,10))
    
    for i in range(k):
        plt.scatter(cluster[i][:,0],cluster[i][:,1],cmap='viridis',label = i+1)#plotting clusters
    plt.scatter(present[:,0],present[:,1],s=100, color='black') #plotting the final centroids
        
    plt.legend()
    titles='Clusters='+str(k)
    plt.title(titles)
    
    plt.show()
    sum=0
    for i in range(k):     
        
        sqsum=np.square(present[i]-cluster[i]) #calculating the objective function
        sum=np.sum(sqsum)+sum
            
                 
    meand.append(sum)#storing the obj function value for each k



plt.figure(figsize=(10,10))           
Z=np.arange(2,k+1)    
plt.plot(Z,meand[2:])  #plotting the obj function w.r.t k
plt.title('Obj Function Vs K')
plt.show
