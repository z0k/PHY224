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

sample_num = data[:,0]
counts = data[:,1]

time = sample_num * 3

background_avg = mean(background)
#Counts with background average deducted.
pineapple_counts = counts - background_avg

p = zeros(2)
p[0] = 100.
p[1] = -1000.




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
pylab.plot(time, peval(time,p_final))
pylab.show()


n,bins,patches = plt.hist(pineapple_counts, bins=10, normed=1, facecolor='blue', alpha = 0.75)

mu = mean(pineapple_counts)
sigma = mu ** 0.5

y=mlab.normpdf(bins, mu, sigma)

l = plt.plot(bins, y, 'g-')

pylab.show()



