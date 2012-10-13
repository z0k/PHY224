#Exercise 3
#Pendulum 3
#October 10th 2012


from numpy import *
from scipy import *
from pylab import *
from scipy.optimize import leastsq


data = loadtxt('time_length.txt', dtype='float')
data2 = loadtxt('angle_time.txt', dtype='float')

period = data[:, 0]

#Convert centimeters into meters.
length = data[:, 1] / 100

<<<<<<< HEAD
g = 9.80665
=======
angle = (pi / 180.) * data2[:,0]
print angle

period2 = data2[:,1]
print period2


g = 980.665
>>>>>>> d88c1a61a00c73f7737caaa55f86ccbbdc16b6a9
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


<<<<<<< HEAD

def grav(p):
    return 4 * pi ** 2 / p[1]


plsq = leastsq(residuals, p, args=(period_square, length), maxfev=2000)


title('Linear Fit of Period vs. Length')
xlabel('Length')
ylabel('Period$^2$')
errorbar(length, period_square, 0.05, fmt='r+')
plot(length, period_square, marker='o', linestyle='None')
plot(length, peval(length, plsq[0]))
=======
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
>>>>>>> d88c1a61a00c73f7737caaa55f86ccbbdc16b6a9
show()

print 'The acceleration due to gravity is ', grav(plsq[0])
