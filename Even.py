#y=2x+1
#y=2x^2+2
import matplotlib.pyplot as p
import numpy as np
x = np.arange(1, 11, 1)
y1 = (2*x)+1
y2 = (2*x**2)+2
p.plot(x,y1, color = "green", linewidth = 3, label = "y=2x+1")
p.plot(x,y2, color = 'red', linewidth = 3, label = "y=2x^2+2")
p.xlabel("Sequencial Points")
p.ylabel("Fetched Points")
p.legend()
p.show()
