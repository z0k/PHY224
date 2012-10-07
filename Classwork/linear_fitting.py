from numpy import *
from scipy import *
from pylab import *
from scipy.optimize import leastsq


data = loadtxt('time_length.txt')

period = data[:,0]
print period

length = data[:,1]
print length

g = 9.8
p = zeros(2)
p[0] = 0
p[1] = (4 * pi ** 2) / g


period_square = period ** 2

def peval(length, p):
    return p[1] * ((length * (2 * pi) ** 2) / g) + p[0]


def residuals(p, period_square, length):
    err = period_square - peval(length, p)
    return err

plsq = leastsq(residuals, p, args=(period_square, length), maxfev=2000)

#plot(length, period_square)
plot(length, peval(length, p))
show()
