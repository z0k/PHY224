from numpy import *
from pylab import *
from scipy.optimize import leastsq

data = loadtxt('charge_discharge.txt', skiprows=1, dtype='float')

time = data[:, 0] - data[0, 0]

voltage = data[:, 1] - data[-1, 1]

#Initial guess paramters.
p = zeros(2)
p[0] = 6.504677
p[1] = 3.74 * 10 ** -4


#Fit function.
def peval(time, p):
    return p[0] * exp(-time / p[1])


def residuals(p, voltlage, time):
    return voltage - peval(time, p)


p_final, cov_x, info, mesg, success = leastsq(residuals, p,
args=(voltage, time), full_output=True)

#p_final is a value outputed from the leastsq function.
print p_final
y_final = peval(time, p_final)
#Chi-square.
chi2 = sum((voltage - y_final) ** 2 / abs(0.01))
#Degrees of freedom.
dof = len(time) - len(p_final)
print "RMS of residuals (sqrt(chisquared/dof))", sqrt(chi2 / dof)

for i in range(len(p_final)):
    print "p[%d] =%8.5f +/- %.6f" % (i, p_final[i], sqrt(cov_x[i, i]))

plot(time, voltage)
title('Voltage vs. Time graph')
ylabel('Voltage')
xlabel('Time')

plot(time, peval(time, p_final))
show()
