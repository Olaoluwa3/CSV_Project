# 1) Use the header row to determine the indexes for TMIN and TMAX
# 2) Use the station name to automatically generate an appropriate title for graph
# 3) Create 2 subplot graphs in one visualization to see both graphs to compare side by side



import csv
from datetime import datetime


infile_deathValley = open("death_valley_2018_simple.csv", 'r')
deathValley_reader = csv.reader(infile_deathValley, delimiter = ",")


infile_sitkaWeather = open("sitka_weather_2018_simple.csv", 'r')
sitkaWeather_reader = csv.reader(infile_sitkaWeather, delimiter = ",")


header_rowDV = next(deathValley_reader)
header_rowSW = next(sitkaWeather_reader)




for index, column_header in enumerate(header_rowDV):
    print(index, column_header)
    if column_header == "TMIN":
        low_indexDV = index
    elif column_header =="TMAX":
        high_indexDV = index
    elif column_header == "DATE":
        date_index = index          #Only one set of dates needed
    elif column_header == "NAME":
        name_indexDV = index
    


for index, column_header in enumerate(header_rowSW):
    print(index, column_header)
    if column_header == "TMIN":
        low_indexSW = index
    if column_header =="TMAX":
        high_indexSW = index
    if column_header == "NAME":
        name_indexSW = index 



highsDV = []
lowsDV = []
highsSW = []
lowsSW = []
dates = []




for item in deathValley_reader:

    try:
        current_date = datetime.strptime(item[date_index],'%Y-%m-%d')
        highDV = int(item[high_indexDV])
        lowDV = int(item[low_indexDV])
        station_nameDV = item[name_indexDV]
        
    except ValueError:
        print(f"Missing data for {current_date} in death_valley file")

    else:
        highsDV.append(highDV)
        lowsDV.append(lowDV)
        dates.append(current_date)




for item in sitkaWeather_reader:

    try:
        current_date = datetime.strptime(item[date_index],'%Y-%m-%d')
        highSW = int(item[high_indexSW])
        lowSW = int(item[low_indexSW])
        station_nameSW = item[name_indexSW]
        
    except ValueError:
        print(f"Missing data for {current_date} in sitka_weather file")

    else:
        highsSW.append(highSW)
        lowsSW.append(lowSW)



    
    
#Draw diagram

import matplotlib.pyplot as plt

fig = plt.figure()



plt.subplot(2,1,1)
plt.plot(dates, highsSW, c="red")
plt.plot(dates, lowsSW, c="blue")
plt.fill_between(dates, highsSW, lowsSW, facecolor='blue', alpha=0.1)
plt.title(station_nameSW)

plt.subplot(2,1,2)
plt.plot(dates, highsDV, c="red")
plt.plot(dates, lowsDV, c="blue")
plt.fill_between(dates, highsDV, lowsDV, facecolor='blue', alpha=0.1)
plt.title(station_nameDV)

fig.autofmt_xdate()

plt.suptitle(f"Temperature comparison between {station_nameSW} and {station_nameDV}")
plt.show()


