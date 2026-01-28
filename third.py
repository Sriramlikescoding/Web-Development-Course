import matplotlib.pyplot as p
x1 = [58, 10, 25, 3, 98, 76, 45, 98, 34, 59]
y1= [3, 57, 40, 12, 37, 78, 98, 70, 67, 69]
x2 = [1, 2, 57, 49, 56, 29, 57, 24, 33, 83]
y2= [49, 29, 34, 8, 20, 27,38, 78, 69, 27]
p.scatter(x1, y1, c='red', linewidth=2, marker='s', edgecolors='green', s=50)
p.scatter(x2, y2, c='green', linewidth=2, marker='^', edgecolors='red', s=50)
p.xlabel("X axis")
p.ylabel("Y axis")
p.show()