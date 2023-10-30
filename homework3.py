import numpy as np

''' 
HOMEWORK 3
'''

################################################
################### 1 ##########################
################################################
"hidden layer input wights"
w11=1;w12=0;w13=-1;w14=0
w21=0;w22=1;w23=-1;w24=-1
w01=-1;w02=-1;w03=-1;w04=-1
 
"hidden layer output wights"
v11=1;v12=-1
v21=1;v22=-1
v31=1;v32=-1
v41=1;v42=-1
v01=0;v02=2

"inputs"
x1=3;x2=14

"hidden layer"
z1 = x1*w11 + x2*w21 + w01
z2 = x1*w12 + x2*w22 + w02
z3 = x1*w13 + x2*w23 + w03
z4 = x1*w14 + x2*w24 + w04

fz1 = max(z1,0)
fz2 = max(z2,0)
fz3 = max(z3,0)
fz4 = max(z4,0)

"output layer"
u1 = max(fz1*v11 + fz2*v21 + fz3*v31 + fz4*v41 + v01,0)
u2 = max(fz1*v12 + fz2*v22 + fz3*v32 + fz4*v42 + v02,0)

print('u1:',str(u1),", ",'u2:',str(u2))

"output"
print("o1:"," ",str(np.exp(u1)),"/",str((np.exp(u1)+np.exp(u2))))
print("o2:"," ",str(np.exp(u2)),"/",str((np.exp(u1)+np.exp(u2))))


o1 = np.exp(u1)/(np.exp(u1)+np.exp(u2))
o2 = np.exp(u2)/(np.exp(u1)+np.exp(u2))

print('Salida')
print('o1:',str(o1),'o2:',str(o2))

################################################
################### 2 ##########################
################################################

print("SUM_i fzi = 1")
fz1 = 1/4
fz2 = 1/4
fz3 = 1/4
fz4 = 1/4

u1 = max(fz1*v11 + fz2*v21 + fz3*v31 + fz4*v41 + v01,0)
u2 = max(fz1*v12 + fz2*v22 + fz3*v32 + fz4*v42 + v02,0)

print('u1:',str(u1))
print("o1:"," ",str(np.exp(u1)),"/",str((np.exp(u1)+np.exp(u2))))
o1 = np.exp(u1)/(np.exp(u1)+np.exp(u2))
print('o1:',str(o1))

print("SUM_i fzi = 0")
fz1 = 0
fz2 = 0
fz3 = 0
fz4 = 0

u1 = max(fz1*v11 + fz2*v21 + fz3*v31 + fz4*v41 + v01,0)
u2 = max(fz1*v12 + fz2*v22 + fz3*v32 + fz4*v42 + v02,0)

print('u1:',str(u1))
print("o1:"," ",str(np.exp(u1)),"/",str((np.exp(u1)+np.exp(u2))))
o1 = np.exp(u1)/(np.exp(u1)+np.exp(u2))
print('o1:',str(o1))

print("SUM_i fzi = 3")
fz1 = 3/4
fz2 = 3/4
fz3 = 3/4
fz4 = 3/4

u1 = max(fz1*v11 + fz2*v21 + fz3*v31 + fz4*v41 + v01,0)
u2 = max(fz1*v12 + fz2*v22 + fz3*v32 + fz4*v42 + v02,0)

print('u1:',str(u1))
print("o1:"," ",str(np.exp(u1)),"/",str((np.exp(u1)+np.exp(u2))))
o1 = np.exp(u1)/(np.exp(u1)+np.exp(u2))
print('o1:',str(o1))

################################################
############# Inverser temperature #############
################################################
print('INVERSER TEMPERATURE')
fz1 = max(z1,0)
fz2 = max(z2,0)
fz3 = max(z3,0)
fz4 = max(z4,0)

"output layer"
u1 = max(fz1*v11 + fz2*v21 + fz3*v31 + fz4*v41 + v01,0)
u2 = max(fz1*v12 + fz2*v22 + fz3*v32 + fz4*v42 + v02,0)

print('u1:',str(u1),", ",'u2:',str(u2))

"parametro"
beta = 1

"output"
print("o1:"," ",str(np.exp(beta*u1)),"/",str((np.exp(beta*u1)+np.exp(beta*u2))))
print("o2:"," ",str(np.exp(beta*u2)),"/",str((np.exp(beta*u1)+np.exp(beta*u2))))


o1 = np.exp(beta*u1)/(np.exp(beta*u1)+np.exp(beta*u2))
o2 = np.exp(beta*u2)/(np.exp(beta*u1)+np.exp(beta*u2))

print('Salida')
print('o1:',str(o1),'o2:',str(o2))