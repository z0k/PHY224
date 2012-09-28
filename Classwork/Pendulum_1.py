import pylab
from numpy import *


#Maximum number of objects in each array (or number of iterations + 1)
n = 1000
#Define the mass of the bob in kilograms.
m = 0.040
#Define the constant for the time step interval.
delta_t = 0.01
#Define the constant for gravity in meteres per second square.
g = 9.81
#Define the constant for length in meters.
L = 0.353

omega = (g / L) ** (1. / 2.)

#Initialize the array for angular velocity. Set initial velocity to 0.
angular_velocity = zeros(n)
angular_velocity[0] = 0.

#Initialize the array for the angle theta. Set initial angle to be 3 degrees,
#converted to radians.
theta_array = zeros(n)
theta_array[0] = (3. * pi) / 180.

#Initialize the array for time.
time = arange(0, n)

#Initialize the array for energy.
total_energy = zeros(n)

#The loop is iterated up to 999. It assigns values to the indicated arrays
#according to the forward Euler algorithm.
for i in range(0, n - 1):
    angular_velocity[i + 1] = angular_velocity[i] - ((omega ** 2) * theta_array[i] * delta_t)
    theta_array[i + 1] = theta_array[i] + angular_velocity[i] * delta_t
    total_energy[i] = (1. / 2. * (m * L ** 2) * angular_velocity[i] ** 2) + (1. / 2. * m * g * L * theta_array[i] ** 2)

#A graph is plotted with time in seconds on the x-axis and theta in degrees
#on the y-axis.
pylab.plot(time * delta_t, theta_array * (180. / pi))
pylab.xlabel('time')
pylab.ylabel('theta')
pylab.show()

pylab.plot(time * delta_t, angular_velocity)
pylab.xlabel('time')
pylab.ylabel('angular velocity')
pylab.show()

#A phase diagram is plotted: theta in degrees versus the angular velocity.
pylab.plot(theta_array * (180. / pi), angular_velocity)
pylab.xlabel('theta')
pylab.ylabel('angular velocity')
pylab.show()

#A graph is plotted with time in seconds on the x-axis and energy in __ on
#the y-axis.
pylab.plot(time * delta_t, total_energy)
pylab.xlabel('time')
pylab.ylabel('total energy')
pylab.show()
