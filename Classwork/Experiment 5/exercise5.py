from numpy import *
from scipy.optimize import leastsq
from scipy import *
from pylab import *


data = loadtxt('Exercise5_data.txt', dtype='float')
time = data[:, 0]
conduction = data[:, 1]

conduction_error = 0.04 * conduction
time_error = 0.001

p = zeros(4)
p[0] = 5.9
p[1] = -2. / 5.
p[2] = 3
p[3] = .008


def peval(time, p):
    return p[0] * (1 - exp(p[1] * time)) + p[2] * (exp(p[3] * time) - 1)


def residuals(p, conduction, time):
    return conduction - peval(time, p)

p_final, cov_x, info, mesg, success = leastsq(residuals, p,
args=(conduction, time), full_output=True)

#p_final is a value outputed from the leastsq function.
y_final = peval(time, p_final)
#Chi-square.
chi2 = sum((conduction - y_final) ** 2 / abs(0.3))
#Degrees of freedom.
dof = len(time) - len(p_final)
print "RMS of residuals (sqrt(chisquared/dof))", sqrt(chi2 / dof)

for i in range(len(p_final)):
    print "p[%d] =%8.3f +/- %.4f" % (i, p_final[i], sqrt(cov_x[i, i]))

errorbar(time, conduction, time_error, conduction_error, fmt='r+')

plot(time, peval(time, p_final))
plot(time, conduction)
title('Figure 1')
xlabel('Time')
ylabel('Conduction')
show()
