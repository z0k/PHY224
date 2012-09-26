import pylab
from numpy import *


#Maximum number of objects in each array (or number of iterations + 1)
n = 1000

#Define the constant for the time step interval.
delta_t = 0.01
#Define the constant for gravity in meteres per second square.
g = 9.81
#Define the constant for length in centimeters.
L = 35.3

omega = (g / L) ** (1. / 2.)

#Initialize the array for angular velocity. Set initial velocity to 0.
angular_velocity = zeros(n)
angular_velocity[0] = 0.

#Initialize the array for the angle theta. Set initial angle to be ...
theta_array = zeros(n)
theta_array[0] = (3. * pi) / 180.

#Initialize the array for time.
time = arange(0, n)

#The loop is iterated 999 times. It assigns values to the indicated arrays
#according to the forward Euler algorithm.
for i in range(0, n - 1):
    angular_velocity[i + 1] = angular_velocity[i] - ((omega ** 2) * theta_array[i] * delta_t)
    theta_array[i + 1] = theta_array[i] + angular_velocity[i] * delta_t

#A graph is plotted with time in seconds on the x-axis and theta in radians
#on the y-axis.
pylab.plot(time * delta_t, theta_array)
pylab.xlabel('time')
pylab.ylabel('theta')
pylab.show()
