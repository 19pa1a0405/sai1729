import numpy as np
import random
import matplotlib.pyplot as plt

def line_gen(A,B):
   len =10
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB


#if using termux
import subprocess
import shlex
#end if


#input parameters
a=5                     #length of base (CD)
b=4                     #length of side (CB)
theta = np.pi/3         #angle between CB & CD
C = np.array([0,0])     #Vertex C
B = np.array([a,0])
D = b*np.array([(np.cos(theta)),(np.sin(theta))])
A = B-C+D
l=D+B     
O=l/2
x=B-O
y=B-A
ar1=0.5*np.linalg.norm((np.cross(D,O)))
ar2=0.5*np.linalg.norm((np.cross(x,y)))


k=C-B
l=C-D
m=A-D
n=A-B

ar3=0.5*np.linalg.norm((np.cross(k,l)))
ar4=0.5*np.linalg.norm((np.cross(n,B)))
ar5=0.5*np.linalg.norm((np.cross(m,n)))
print("Ar(DOC)=",ar1)
print("Ar(AOB)=",ar2)
print("Ar(DCB)=",ar3)
print("Ar(ACB)=",ar4)
print("Ar(DAB)=",ar5)
##Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)

x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_OC = line_gen(O,C)
x_OD = line_gen(O,D)


#Pliotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CD[0,:],x_CD[1,:])
plt.plot(x_DA[0,:],x_DA[1,:])

plt.plot(x_OA[0,:],x_OA[1,:])
plt.plot(x_OB[0,:],x_OB[1,:])
plt.plot(x_OC[0,:],x_OC[1,:])
plt.plot(x_OD[0,:],x_OD[1,:])


#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,                                   
                 (tri_coords[0,i], tri_coords[1,i]),   
                 textcoords="offset points",            
                 xytext=(5,-15),                      
                 ha='left')                           

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()
