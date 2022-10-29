#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *


import sys                                          #for path to external scripts
sys.path.insert(0,'/home/sai1729/trunk/opt1/CoordGeo')         #path to my scripts

#local imports

#from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import circ_gen
#from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

r = 5
def S(R):
	return  (1/3)*pi*R**2*r+(1/3)*pi*R**2*np.sqrt(r**2-R**2)


#Gradient Descent
cur_x = r-1# The algorithm starts at x=2
gamma = 0.001 # step size multiplier
precision = 0.00000001
previous_step_size = 1 
max_iters = 100000000 # maximum number of iterations
iters = 0 #iteration counter


df = lambda R:(2/3)*pi*R*r+(2*pi*R*r**2-3*pi*R**3)/(3*np.sqrt(np.abs(r**2-R**2)))


while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cur_x
    cur_x  += gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters+=1
max_val=S(cur_x,)
print("Maximum value of f(x) is ", max_val, "at","R =",cur_x)


#Plotting f(x)
x=np.linspace(0.1,r,100)
y=S(x)
plt.plot(x,y)
#Labelling points
plt.plot(cur_x,max_val,'o')
plt.text(cur_x, max_val,f'P({cur_x:.4f},{max_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
#plt.legend()

#if using termux
plt.savefig('/sdcard/sai1729/trunk/opt2/opt0.pdf')
#subprocess.run(shlex.split("termux-open '/sdcard//sai1729/trunk/opt2/opt0.pdf'"))
#else
#plt.show()
