#Create a file object

from email import header
import csv
from shutil import which

from numpy import append

infile = open("sitka_weather_07-2018_simple.csv", 'r')
file_reader = csv.reader(infile, delimiter = ",")

header_row = next(file_reader)

#print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []

for item in file_reader:
    highs.append(int(item[5]))
    
print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c="red")
plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()