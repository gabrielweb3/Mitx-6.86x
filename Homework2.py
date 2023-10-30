# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:21:03 2023

Homework 2

@author: d518448
"""
import numpy as np

U = np.array([[6,0,3,6]])
V = np.array([[4,2,1]])
print('X=',U.T@V)
X = np.array([[24,12,6],[0,0,0],[12,6,3],[24,12,6]])
Y = np.array([[5,0,7],[0,2,0],[4,0,0],[0,3,6]])

### Error cuadrático
E2 = 0
for i in range(Y.shape[0]):
    for j in range(Y.shape[1]):
        if Y[i,j]!=0:
            E2 += (Y[i,j]-X[i,j])**2/2
            
### Regularización en U
RU = 0
for i in range(U.shape[1]):
    RU += U[0,i]**2/2
    
### Regularización en V
RV = 0
for i in range(V.shape[1]):
    RV += V[0,i]**2/2
    
### Regularización total
R = RU + RV

### Actualización U
U1 = []
for a in range(Y.shape[0]):
    Num = 0
    den = 0
    for i in range(Y.shape[1]):
        if Y[a,i]!=0:
            Num += V[0,i]*Y[a,i]
            den += V[0,i]**2
    U1.append(Num/(1+den))
