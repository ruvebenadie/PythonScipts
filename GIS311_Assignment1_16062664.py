#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ruve Benadie 16062664
#GIS311 Assignment 1

#Import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#weekdays = C:\Users\ruveb\Desktop\GIS311\Data\Section 1\johannesburg-gpzones-2020-1-OnlyWeekdays-MonthlyAggregate.csv
#weekends = C:\Users\ruveb\Desktop\GIS311\Data\Section 1\johannesburg-gpzones-2020-1-OnlyWeekends-MonthlyAggregate.csv
#accept csv files as input
df_weekdays = input('Please enter file path to weekdays data, remember to add .csv')
df_weekends = input('Please enter file path to weekends data, remember to add .csv')
df_weekdays = str(df_weekdays)
df_weekends = str(df_weekends)
df_weekdays = pd.read_csv(r'C:\Users\ruveb\Desktop\GIS311\Data\Section 1\johannesburg-gpzones-2020-1-OnlyWeekdays-MonthlyAggregate.csv')
df_weekends = pd.read_csv(r'C:\Users\ruveb\Desktop\GIS311\Data\Section 1\johannesburg-gpzones-2020-1-OnlyWeekends-MonthlyAggregate.csv')

#check if columns exits:
#get column names
weekday_columns = df_weekdays.columns
weekend_columns = df_weekends.columns

#check if columns in files are similar
common_columns = weekday_columns.intersection(weekend_columns)
print('These columns exists in both CSV files:\n',common_columns, "\n you will be able to compare them")

for i in weekend_columns:
    if i not in weekday_columns:
        print("These columns are not in the dataset \n", i ,"\n you will not be able to compare them")

#check if column can be converted a to numeric value:
for i in df_weekdays["sourceid"]:
    try:
        float(i)
    except ValueError:
        print(df_weekdays["sourceid"], "Can not be converted")

for i in df_weekdays["dstid"]:
    try:
        float(i)
    except ValueError:
        print(df_weekdays["dstid"], "Can not be converted")

for i in df_weekdays["month"]:
    try:
        float(i)
    except ValueError:
        print(df_weekdays["month"], "Can not be converted")

for i in df_weekdays["mean_travel_time"]:
    try:
        float(i)
    except ValueError:
        print(df_weekdays["mean_travel_time"], "Can not be converted")

for i in df_weekdays["standard_deviation_travel_time"]:
    try:
        float(i)
    except ValueError:
        print(df_weekdays["standard_deviation_travel_time"], "Can not be converted")

for i in df_weekdays["geometric_mean_travel_time"]:
    try:
        float(i)
    except ValueError:
        print(df_weekdays["geometric_mean_travel_time"], "Can not be converted")

for i in df_weekdays["geometric_standard_deviation_travel_time"]:
    try:
        float(i)
    except ValueError:
        print(df_weekdays["geometric_standard_deviation_travel_time"], "Can not be converted")

for i in df_weekends["sourceid"]:
    try:
        float(i)
    except ValueError:
        print(df_weekends["sourceid"], "Can not be converted")

for i in df_weekends["dstid"]:
    try:
        float(i)
    except ValueError:
        print(df_weekends["dstid"], "Can not be converted")

for i in df_weekends["month"]:
    try:
        float(i)
    except ValueError:
        print(df_weekends["month"], "Can not be converted")

for i in df_weekends["mean_travel_time"]:
    try:
        float(i)
    except ValueError:
        print(df_weekends["mean_travel_time"], "Can not be converted")

for i in df_weekends["standard_deviation_travel_time"]:
    try:
        float(i)
    except ValueError:
        print(df_weekends["standard_deviation_travel_time"], "Can not be converted")

for i in df_weekends["geometric_mean_travel_time"]:
    try:
        float(i)
    except ValueError:
        print( df_weekends["geometric_mean_travel_time"], "Can not be converted")

for i in df_weekends["geometric_standard_deviation_travel_time"]:
    try:
        float(i)
    except ValueError:
        print( df_weekends["geometric_standard_deviation_travel_time"], "Can not be converted")

#compare the files:
#compare mean travel times
y = df_weekdays.iloc[:,0:1].groupby(["sourceid"])
print(y)
meantt_wd = df_weekdays["mean_travel_time"].mean()
meantt_we = df_weekends["mean_travel_time"].mean()
print("\nThe average travel time over weekdays is:", meantt_wd, "\nThe average travel time over weekends is:", meantt_we, "\n")

#general statistics
print("Basic statistics for weekdays:\n",df_weekdays.iloc[:,3:].describe(), "\n")
print("Basic statistics for weekends:\n ",df_weekends.iloc[:,3:].describe(), "\n")

#monthly statistics
wd_mean_mm = df_weekdays.iloc[:, 2:].groupby(["month"]).mean()
print("\nMean per month for weekdays:\n", wd_mean_mm, "\n")

we_mean_mm = df_weekends.iloc[:,2:].groupby(["month"]).mean()
print("\nMean per month for weekends:\n", we_mean_mm, "\n")

wd_max_mm = df_weekdays.iloc[:,2:].groupby(["month"]).max()
print("\nMaximum per month for weekdays:\n", wd_max_mm)

we_max_mm = df_weekends.iloc[:, 2:].groupby(["month"]).max()
print("\nMaximum per month for weekends:\n", we_max_mm)

wd_min_mm = df_weekdays.iloc[:, 2:].groupby(["month"]).min()
print("\nMinimum per month for weekdays:\n", wd_min_mm)

we_min_mm = df_weekends.iloc[:, 2:].groupby(["month"]).min()
print("\nMinimum per month for weekends:\n", we_min_mm)

#charts:
#line graph
ywdm = df_weekdays.iloc[:,[2,3]].groupby(["month"]).mean()
month = ["Jan", "Feb", "Mar"]

plt.plot(month, ywdm)
plt.title("Average Time Traveled per Month for Weekdays")
plt.xlabel("Month")
plt.ylabel("Average Time Traveled")
plt.show()

ywem= df_weekends.iloc[:,[2,3]].groupby(["month"]).mean()
plt.plot(month, ywem)
plt.title("Average Time Traveled per Month for Weekends")
plt.xlabel("Month")
plt.ylabel("Average Time Traveled")
plt.show()

ygmwd = df_weekdays.iloc[:, [2, 5]].groupby(["month"]).mean()
plt.plot(month, ygmwd)
plt.title("Geometric Mean Travel Time per Month for Weekdays")
plt.xlabel("Month")
plt.ylabel("Geometric Mean")
plt.show()


ygmwe = df_weekends.iloc[:, [2, 5]].groupby(["month"]).mean()
plt.plot(month, ygmwe)
plt.title("Geometric Mean Travel Time per Month for Weekends")
plt.xlabel("Month")
plt.ylabel("Geometric Mean")
plt.show()

ystdwd = df_weekdays.iloc[:, [2,4]].groupby(["month"]).mean()
plt.plot(month, ystdwd)
plt.title("Standard Deviation per Month for Weekdays")
plt.xlabel("Month")
plt.ylabel("Mean Standard Deviation")
plt.show()

ystdwe = df_weekends.iloc[:, [2,4]].groupby(["month"]).mean()
plt.plot(month, ystdwe)
plt.title("Standard Deviation per Month for Weekends")
plt.xlabel("Month")
plt.ylabel("Mean Standard Deviation")
plt.show()

ygstdwd = df_weekdays.iloc[:, [2,6]].groupby(["month"]).mean()
plt.plot(month, ygstdwd)
plt.title("Geometric Standard Deviation per Month for Weekdays")
plt.xlabel("Month")
plt.ylabel("Mean Geometric Standard Deviation")
plt.show()

ygstdwe = df_weekends.iloc[:, [2,6]].groupby(["month"]).mean()
plt.plot(month, ygstdwe)
plt.title("Geometric Standard Deviation per Month for Weekends")
plt.xlabel("Month")
plt.ylabel("Mean Geometric Standard Deviation")
plt.show()

#Box plot

label = ["Mean Travel Time", "Geometric Mean"]
box = plt.boxplot(df_weekdays.iloc[:,[3,5]], showmeans=True, meanline=True)
plt.xticks([1,2], label)
plt.xticks(rotation = 90)
plt.title("Box Plot for Weekdays")
plt.show()

plt.boxplot(df_weekends.iloc[:,[3,5]], showmeans=True, meanline=True)
plt.xticks([1,2], label)
plt.xticks(rotation = 90)
plt.title("Box Plot for Weekends")
plt.show()



# In[ ]:




