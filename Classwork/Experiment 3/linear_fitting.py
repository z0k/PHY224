from numpy import *
from scipy import *
from pylab import *
from scipy.optimize import leastsq

#Length in meters.
L = 0.351
#Acceleration due to gravity.
g = 9.80665
T0 = 2. * pi * (L / g) ** (0.5)
data = loadtxt('angle_time.txt', dtype='float')

angle = (pi / 180.) * data[:,0]



period_nonlinear = data[:,1] / T0

period_error = ( (0.05 / period_nonlinear) ** 2 + (0.017 / 1.1891) ** 2 ) ** 0.5
print period_error

x = sin(angle / 2.) ** 2

p = zeros(2)
p[0] = 1.
p[1] = 0.25


def peval(angle, p):
    return p[1] * x + p[0]


def residuals(p, period_nonlinear, angle):
    return period_nonlinear - peval(angle, p)


plsq = leastsq(residuals, p, args=(period_nonlinear, angle), maxfev=2000)

title('Linear Fit of Period vs. Angle')

#Angle is really "sin(angle / 2) ** 2"
xlabel('Angle')
ylabel('Period (seconds)')
errorbar(x, period_nonlinear * T0, period_error, fmt='r+')
plot(x, period_nonlinear * T0, marker='o', linestyle='None')
plot(x, peval(angle, plsq[0]) * T0)
show()




