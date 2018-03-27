import numpy as np
import pylab as pl
x = np.linspace(-10,10,100)
y1 = 5 * x + 50
pl.figure()     # Lesson 1
pl.plot(x,y1)
y2 = 2 * x ** 2 + 3 * x - 1
pl.figure()     # Lesson 2
pl.plot(x,y1)
pl.plot(x,y2)
pl.show()

