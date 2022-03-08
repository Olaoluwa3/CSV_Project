# 1) Changing the file to include all the data for the year of 2018
# 2) Change the title to - Daily low and high temperatures - 2018
# 3) Extract low temps from the file and add to chart
# 4) Shade in the area between high and low


import csv
from datetime import datetime
from numpy import append

infile = open("death_valley_2018_simple.csv", 'r')
file_reader = csv.reader(infile, delimiter = ",")

header_row = next(file_reader)

#print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)


highs = []
dates = []
lows = []

test_date = datetime.strptime('2018-07-01','%Y-%m-%d')
print(test_date)



for item in file_reader:

    try:
        current_date = datetime.strptime(item[2],'%Y-%m-%d')
        high = int(item[4])
        low = int(item[5])
        
    
    except ValueError:
        print(f"Missing data for {current_date}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
    
    
print(highs)
print(dates)


import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)
plt.title("Daily low and high temperatures - 2018", fontsize=16)
plt.xlabel("Year 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)


fig.autofmt_xdate()

plt.show()


