import matplotlib.pyplot as p

Year = [1920, 1930, 1940, 1950, 1950, 1960, 1970, 1980, 1990, 2000, 2010]

UnemploymentRate = [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3, 6.5]
p.plot(Year, UnemploymentRate, color = "Red", marker = "o")
p.title("Unemployment vs. Years", fontsize = 14)
p.xlabel("Year", fontsize = 14)
p.ylabel("Unemployment Rate", fontsize =14)
p.grid(True)
p.show()