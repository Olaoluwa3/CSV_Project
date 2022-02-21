
#using the datetime module
#adding dates to the x axis for the month of July 2018

from datetime import datetime
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
dates = []

test_date = datetime.strptime('2018-07-01','%Y-%m-%d')
print(test_date)



for item in file_reader:
    highs.append(int(item[5]))
    current_date = datetime.strptime(item[2],'%Y-%m-%d')
    dates.append(current_date)
    
print(highs)
print(dates)


import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("Month of July 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)


fig.autofmt_xdate()

plt.show()



