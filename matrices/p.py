import numpy as np
import random
import matplotlib.pyplot as plt
import sympy as sym

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
A = np.array([2,-3]) 
B = np.array([-2,1])
C = np.array([4.5,0])
X = (A+B+C)/3
##Generating all line
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

x=np.linspace(-5,5.5,20)
y=(1-(2*x))/3
plt.plot(x,y)
h=np.linspace(-5,5,20)
k=(9-(2*h))/2
plt.plot(h,k)
#Pliotting all lines
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CA[0,:],x_CA[1,:])
#Labeling the coordinates
tri_coords = np.vstack((A,B,C,X)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','X']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,                               
                 (tri_coords[0,i], tri_coords[1,i]),    
                 textcoords="offset points",        
                 xytext=(5,-15),                      
                 ha='left')                           
plt.plot(h,k)
plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()
