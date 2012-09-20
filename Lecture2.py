import pylab
from numpy import *
x = arange(0, 8 * pi, 0.05 * pi)
pylab.plot(x, cos(x))
pylab.plot(x, cos(x) * exp(-x / 20.0))
pylab.xlabel('x')
pylab.title('Oscillations and damped oscillations')
pylab.savefig('pylabplot.png')

pylab.show()

import os
currdir = os.getcwd()

print "File saved in ", currdir
