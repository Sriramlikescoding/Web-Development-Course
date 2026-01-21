#X is velocity y is
import matplotlib.pyplot as p
x = [0, 5, 10, 15, 20, 25, 30]
y1 = [10, 15, 20, 20, 30, 15, 0]
y2 = [10, 12, 15, 12, 20, 10, 0]

p.plot(x,y1, linestyle = 'dashed', marker = 'D')
p.plot(x,y2, linestyle = 'dashed', marker = 'D')
p.xlabel("Velocity")
p.ylabel("Time")
p.title("Velocity/Time Graph")
p.xlim(5,25)
p.ylim(5,25)
p.show()