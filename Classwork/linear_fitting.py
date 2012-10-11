from numpy import *
from scipy import *
from pylab import *
from scipy.optimize import leastsq


data = loadtxt('time_length.txt', dtype='float')
data2 = loadtxt('angle_time.txt', dtype='float')

period = data[:,0]
print period

length = data[:,1]
print length

angle = (pi / 180.) * data2[:,0]
print angle

period2 = data2[:,1]
print period2


g = 980.665
p = zeros(2)
p[0] = 0.
p[1] = (4. * pi ** 2) / g 


period_squared = period ** 2
period_squared_error = 2. * period * 0.05

#Need to define theta max. 
period_nonlinear = period[0] * (1. + 0.25 * sin(angle / 2.) ** 2)


def peval(length, p):
    return p[1] * length + p[0]


def residuals(p, period_squared, length):
    return period_squared - peval(length, p)


plsq = leastsq(residuals, p, args=(period_squared, length), maxfev=2000)

title('No Idea Whats Going On')
xlabel('Length')
ylabel('Period$^2$')
errorbar(length, period_squared, period_squared_error, fmt='r+')
plot(length, period_squared, marker='o', linestyle='None')
plot(length, peval(length, p))
show()

title('Experimental Data')
plot(sin(angle / 2.) ** 2, period2)
show()
