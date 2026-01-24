import numpy as np
import matplotlib.pyplot as p
width = 0.25
fig = p.subplots(figsize=(12,8))
it = [12, 30, 1, 8, 22]
ece= [28,6,16, 5, 10]
cse= [3, 24, 29, 25, 17]
bar1 = np.arange(len(it))
bar2 = [x+width for x in bar1]
bar3 = [x+width for x in bar2]

p.bar(bar1, it, width, color = "Green", label = "IT")
p.bar(bar2, ece, width, color = "Orange", label = "ECE")
p.bar(bar3, cse, width,color = "Red", label = "CSE")
p.xlabel('Branch', fontsize = '15')
p.ylabel("Students Passed")
p.legend()
p.show()
