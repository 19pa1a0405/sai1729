import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp


import sys, os                                          #for path to external scripts
sys.path.insert(0,'\sdcard\sai1729\trunk\opt1\CoordGeo')

#local imports
#from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

# ax+by+cz = d
EQ = np.array(( [2.0, 1.0], [1.0, 2.0], [-1.5, -2.0], [1.0, 0], [0,1.0] ))
EQ_b = np.array([180.0,240.0,-310.0,0,0])
# ax+by+cz >= d
# objective function coeffs
c = np.array([3.0, 3.5])

x = cp.Variable(2,integer=True)

#Cost function
f = c@x
obj = cp.Minimize(f)
#Constraints
constraints = [EQ@x >= EQ_b]

#solution
prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value:", f.value)
print("optimal var:", x.value.T)


#program to generate graph#      

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Generating and plotting line 2x+y=180
A=np.array([0,180])
B=np.array([90,0])
AB=line_gen(A,B)
plt.plot(AB[0,:],AB[1,:],label='2x+y=180')

#Generating and plotting line x+2y=240
C=np.array([0,120])
D=np.array([240,0])
CD=line_gen(C,D)
plt.plot(CD[0,:],CD[1,:],label='x+2y=240')

#Generating and plotting line 1.5x+2y=310
E=np.array([0,155])
F=np.array([310/1.5,0])
EF=line_gen(E,F)
plt.plot(EF[0,:],EF[1,:],label='1.5x+2y=310')

#Shading Required Region
x1=[20,40,140]
y1=[140,100,50]
plt.fill(x1,y1,alpha=0.5)

#Labelling points
plt.plot(20,140,'o',color='r')
plt.text(22.2,142.2,'A(20,140)')
plt.plot(40,100 ,'o',color='r')
plt.text(41.1,101.5,'B(40,100)')
plt.plot(140,50,'o',color='r')
plt.text(142.3,51.3,'C(140,50)')


plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig('/sdcard/sai1729/trunk/opt1/op.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/FWCmodule1/optimization/output.pdf"))
#else
#plt.show()
