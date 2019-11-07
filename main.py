# load apm library
from apm import *

# Integrate model and return solution
sol = apm_solve('Program_Q',3); #3 is optimization mode

print("x1=",sol['x[1]'])
print("x2=",sol['x[2]'])
print("x3=",sol['x[3]'])
print("ksi=",sol['ksi'])

print("h12=",sol['h12'])
print("h13=",sol['h13'])
print("h14=",sol['h14'])
print("h22=",sol['h22'])
print("h23=",sol['h23'])
print("h24=",sol['h24'])
print("h32=",sol['h32'])
print("h33=",sol['h33'])
print("h34=",sol['h34'])
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
