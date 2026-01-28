import matplotlib.pyplot as p
bloodsugar_women = [113, 85,  90, 150, 120, 71, 114, 125, 99, 102, 102, 85, 100]
bloodsugar_men = [112, 75, 130, 128, 80, 99, 100, 99, 106, 117, 109, 72, 100]
type = [bloodsugar_men,bloodsugar_women]
colors = ["g", "r"]
bins = [80, 100, 125, 150]
label = ["Men", "Women"]
p.xlabel("Blood Sugar Range")
p.ylabel("Number of Patients")
p.hist(type,bins=8, width=0.95, color=colors, label=label, orientation="vertical")
p.title("Blood Sugar level chart")
p.legend()
p.show()