# -*- coding: cp1252 -*-
import pylab
from numpy import *
from scipy import *
from scipy.special import gamma
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


background = loadtxt('Background20min.txt', dtype=int)
data = loadtxt('Radioctive Activity-Fiesta Plate(3sec. Dwell).txt', dtype=float, skiprows=2)

#An index for the count detection events.
sample_num = data[:, 0]
#Number of events in specified time interval.
counts = data[:, 1]
#The time interval is three seconds.
time = sample_num * 3
#Background average radiation.
background_avg = mean(background)
#Counts with background average radiation deducted.
pineapple_counts = counts - background_avg

#Guess parameters are defined.
p = zeros(2)
p[0] = 100.
p[1] = -1000.


#Fit function to fit the radioactive decay. A single exponential is used.
def peval(time, p):
    return p[0] * exp(time / p[1])


def residuals(p, pineapple_counts, time):
    return pineapple_counts - peval(time, p)


p_final, cov_x, info, mesg, success = leastsq(residuals, p,
args=(pineapple_counts, time), full_output=True)

pylab.title('Something')
pylab.plot(time, pineapple_counts, marker='o', linestyle='None')
pylab.xlabel('Time')
pylab.ylabel('Counts')
pylab.plot(time, peval(time, p_final))
pylab.show()

#Histogram is plotted showing the number of counts.
n, bins, patches = plt.hist(pineapple_counts, bins=10, normed=1, facecolor='blue', alpha=0.75)
#Mu is the average number of counts per counting interval.
mu = mean(pineapple_counts)
sigma = mu ** 0.5


def poisson(mu, pineapple_counts):
    return (exp(-mu) * mu ** pineapple_counts) / gamma(pineapple_counts + 1)


print sigma
print poisson(mu, pineapple_counts)
#This adds a normal probability density functin to the histogram.
y = mlab.normpdf(bins, mu, sigma)

l = plt.plot(bins, y, 'g-')
pylab.show()
