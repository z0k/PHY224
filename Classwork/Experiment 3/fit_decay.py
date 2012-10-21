import pylab
from numpy 

theta = [11.75, 10.0, 8.75, 7.75, 6.5, 5.25]
time = [20.92, 56.68, 84.46, 110.34, 143.25, 179.66]


pylab.plot(time, log(theta / theta[0]))
pylab.show()

