from numpy import *
from pylab import *
from scipy.optimize import leastsq

data = loadtxt('charge_discharge.txt', skiprows=1,dtype='float')

time = data[:,0] - data[0,0]

voltage = data[:,1] - data[-1,1]

p = zeros(2)
p[0] = 6.504677
p[1] = 3.74 * 10 ** -4


def peval(time, p):
    return  p[0] * exp(-time / p[1])

def residuals(p, voltlage, time):
    return voltage - peval(time, p)


p_final, cov_x, info, mesg, success = leastsq(residuals, p,
args=(voltage, time), full_output=True)


print p_final
plot(time, voltage )

plot(time, peval(time, p_final))
show()


