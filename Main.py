import numpy as np
import matplotlib.pyplot as p
data = {"Maths":20, "Science":15, "Coding":30, "Geography":28}
courses = list(data.keys())
values = list(data.values())
figure = p.figure(figsize=(10,5))
p.bar(courses, values, color="red", width = 0.5)
p.xlabel("Courses Offered")
p.ylabel("Students Enrolled")
p.title("Students enrolled in different courses")
p.show()