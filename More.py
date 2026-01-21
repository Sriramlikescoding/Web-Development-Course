import matplotlib.pyplot as p
import numpy as np
x = np.array([1, 2, 3, 4])
y = x*2
p.plot(x,y)
x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]
p.plot(x1,y1, "--")
p.xlabel("X Axis Data")
p.ylabel("Y Axis DAta")
p.title("Multiple Plots")
p.fill_between(x,y,y1, color = "Red", alpha = 0.5)

p.show()