import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sympy as sym
import sys                                          
sys.path.insert(0,'/sdcad/sai1729/trunk/conic/CoordGeo')   

#from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import *

import subprocess
import shlex

lamda1=25/144
lamda2=-25/81
V = np.array(([lamda1,0],[0,lamda2]))

u = np.array(([0,0]))
e1=np.array(([1,0]))
e2=np.array(([0,1]))
e3=np.array(([-1,0]))
f =-1
f0=-f

e=np.sqrt(1-(lamda1/lamda2))
print(e)

F1=e*(np.sqrt((f0)/(lamda2*(1-e**2))))*e1
F2=e*(np.sqrt((f0)/(lamda2*(1-e**2))))*e3

print(F1)
print(F2)

#ellipse
lamda4 = 16
lamda3 = (lamda4)-((F1.T)@e1)**2
print(lamda3)
f1=-(lamda4)*(lamda3)
print(f1)

def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	return x_ellipse
##Generating the ellipse
x_elli= ellipse_gen(np.sqrt(lamda4),np.sqrt(lamda3))

#Plotting the ellipse
plt.plot(x_elli[0,:],x_elli[1,:],label='$Ellipse$')


def hyper_gen(y):
        x=np.sqrt((1/lamda1)+(-lamda2/lamda1)*(y**2))
        return x
#Standard hyperbola
len = 100
y = np.linspace(-5,5,len)
x = hyper_gen(y)
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
#Plotting the hyperbola
plt.plot(x,y,label='Hyperbola')
plt.plot(-x,y)

#Labeling the coordinates
tri_coords = np.vstack((F1,F2,u)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['F1','F2','u']
for i, txt in enumerate(vert_labels):
        plt.annotate(txt, # this is the text
                                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                                                  textcoords="offset points", # how to position the text
                                                                   xytext=(0,10), # distance from text to points (x,y)
                                                                                    ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')


plt.savefig('/sdcard/sai1729/trunk/conic/conic1.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/sai1729/trunk/conic/conic1.pdf"))
#plt.show()
