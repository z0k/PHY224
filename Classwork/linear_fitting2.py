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

period2 = data2[:,1]


g = 9.80665
p = zeros(2)
p[0] = 0.
p[1] = (4. * pi ** 2) / g 


period_squared = period ** 2
period_squared_error = 2. * period * 0.05


def peval(length, p):
    return p[1] * length + p[0]


def residuals(p, period_squared, length):
    return period_squared - peval(length, p)


def grav(p):
    return 4 * pi ** 2 / p[1]


plsq = leastsq(residuals, p, args=(period_squared, length), maxfev=2000)

title('Linear Fit of Period vs. Length')
xlabel('Length')
ylabel('Period$^2$')
errorbar(length, period_squared, period_squared_error, fmt='r+')
plot(length, period_squared, marker='o', linestyle='None')
plot(length, peval(length, plsq[0]))
show()

print 'The acceleration due to gravity is ', grav(plsq[0])
