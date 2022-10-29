#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/sdcard/sai1729/trunk/circle/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if



#Input parameters
B = np.array([1,2])
f = -20

P = np.array([5,5])
r1= 5

r2 = np.sqrt(np.dot(B,B.T)-f)
print(r2)
A = 2*P-B
print(A)
#Generating the unit circle
xcirc1 = circ_gen(A,r1)

xcirc2 = circ_gen(B,r2)


##Plotting the circle
plt.plot(xcirc1[0,:],xcirc1[1,:],label='First Circle')

plt.plot(xcirc2[0,:],xcirc2[1,:],label='Second Circle')


#Generating all lines
xPA = line_gen(P,A)
xPB = line_gen(P,B)

#Plotting all lines
plt.plot(xPA[0,:],xPA[1,:],label='$Radius1$')

plt.plot(xPB[0,:],xPB[1,:],label='$Radius2$')




#Labeling the coordinates
tri_coords = np.vstack((A,B,P)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#
#if using termux
plt.savefig('/sdcard/sai1729/trunk/circle/circle1.pdf')
#subprocess.run(shlex.split("termux-open /storage/emulated/0/github/cbse-papers/2020/math/12/solutions/figs/matrix-12-3.pdf"))
#else
#plt.show()
