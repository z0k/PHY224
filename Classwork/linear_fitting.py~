from numpy import *
from scipy import *
from pylab import *
from scipy.optimize import leastsq


data = loadtxt('time_length.txt')

period = data[:,0]
print period

length = data[:,1]
print length

g = 980.665
p = zeros(2)
p[0] = 0.
p[1] = (4. * pi ** 2) / g


period_square = period ** 2

def peval(length, p):
    return p[1] * length + p[0]


def residuals(p, period_square, length):
    err = period_square - peval(length, p)
    return err

plsq = leastsq(residuals, p, args=(period_square, length), maxfev=2000)

xlabel('Length')
ylabel('Period$^2$')
errorbar(length, period_square, 0.05, fmt='r+')
plot(length, period_square, marker='o', linestyle='None')
plot(length, peval(length, p))

show()
