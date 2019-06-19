# load apm library
from apm import *

# Integrate model and return solution
sol = apm_solve('Program_Q',3); #3 is optimization mode

print("x1=",sol['x[1]'])
print("x2=",sol['x[2]'])
print("x3=",sol['x[3]'])
print("ksi=",sol['ksi'])
# Plot results
"""
import matplotlib
import matplotlib.pyplot as plt
plt.figure()
plt.plot(z['time'],z['x'],'r-')
plt.plot(z['time'],z['y'],'b--')
plt.legend(['x','y'])
plt.savefig('plot.png')
plt.show()

"""