import matplotlib.pyplot as p
x = [1,2,3,4]
y = [1, 4, 9, 16]
x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]
p.plot(x,y)
p.plot(x1,y1, "--")
p.xlabel("X-Axis Data")
p.ylabel("Y-Axis Data")
p.title("Multiple Plots")
p.show()