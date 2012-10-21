from numpy import *
from scipy import *
from pylab import *
from scipy.optimize import leastsq


data = loadtxt('time_length.txt', dtype='float')
data2 = loadtxt('angle_time.txt', dtype='float')

period = data[:,0]

#Convert data into centimeters.
length = data[:,1] / 100

angle = (pi / 180.) * data2[:,0]

<<<<<<< HEAD:Classwork/linear_fitting.py~
#Period data is normalized (divided by initial value)
period2 = data2[:,1] / data2[0,1]
print period2

=======
period2 = data2[:,1]


>>>>>>> b1da9a0f9d458f60830a4f9b918ccea9b49f4ccc:Classwork/Ex3/linear_fitting2.py
g = 9.80665
p = zeros(2)
p[0] = 1.
p[1] = 0.25


period_squared = period ** 2
period_squared_error = 2. * period * 0.05

<<<<<<< HEAD:Classwork/linear_fitting.py~
period_nonlinear = 1. + 0.25 * sin(angle / 2.) ** 2


def peval(angle, p):
    return p[1] * sin(angle / 2.) ** 2 + p[0]
=======
>>>>>>> b1da9a0f9d458f60830a4f9b918ccea9b49f4ccc:Classwork/Ex3/linear_fitting2.py


def residuals(p, period_nonlinear, angle):
    return period_nonlinear - peval(angle, p)


def grav(p):
    return 4 * pi ** 2 / p[1]

<<<<<<< HEAD:Classwork/linear_fitting.py~
=======
def grav(p):
    return 4 * pi ** 2 / p[1]
>>>>>>> b1da9a0f9d458f60830a4f9b918ccea9b49f4ccc:Classwork/Ex3/linear_fitting2.py

plsq = leastsq(residuals, p, args=(period_nonlinear, angle), maxfev=2000)

<<<<<<< HEAD:Classwork/linear_fitting.py~
title('Linear Fit of Period vs. Length')
xlabel('Length')
ylabel('Period$^2$')
errorbar((sin(angle / 2.) ** 2), period_nonlinear, 0.05, fmt='r+')
plot((sin(angle / 2.) ** 2), period_nonlinear, marker='o', linestyle='None')
plot((sin(angle / 2.) ** 2), peval(angle, plsq[0]))
show()

title('Linear Fit of Period vs. Angle')

=======
plsq = leastsq(residuals, p, args=(period_squared, length), maxfev=2000)

title('Linear Fit of Period$^2$ vs. Length')
xlabel('Length')
ylabel('Period$^2$')
errorbar(length, period_squared, period_squared_error, fmt='r+')
plot(length, period_squared, marker='o', linestyle='None')
plot(length[-2],period_squared[-2], marker='D')
plot(length, peval(length, plsq[0]))
show()

>>>>>>> b1da9a0f9d458f60830a4f9b918ccea9b49f4ccc:Classwork/Ex3/linear_fitting2.py
print 'The acceleration due to gravity is ', grav(plsq[0])
