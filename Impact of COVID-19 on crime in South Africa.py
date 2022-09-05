#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#read covid data
df_confirmed = pd.read_csv(r'C:\Users\ruveb\Desktop\GIS311\Data\Section 2\COVID-19\covid19za_provincial_cumulative_timeline_confirmed.csv')
df_death = pd.read_csv(r'C:\Users\ruveb\Desktop\GIS311\Data\Section 2\COVID-19\covid19za_provincial_cumulative_timeline_deaths.csv')
df_recover = pd.read_csv(r'C:\Users\ruveb\Desktop\GIS311\Data\Section 2\COVID-19\covid19za_provincial_cumulative_timeline_recoveries.csv')


# In[3]:


#clean covid data
#missing values
#number of missing values and fixing them
confirm_missing_count = df_confirmed.isnull().sum()
print("Count of null values per column for confirmed cases:\n", confirm_missing_count)
#dropping null values, no inference can be made and no data can be found on google to fill in the missing values, the total can still be used
df_confirmed_NaNDr = df_confirmed.drop([20,31], axis = 0)
confirm_missing_count = df_confirmed_NaNDr.isnull().sum()
print("Count of null values per column after dropping null rows for confirmed cases:\n", confirm_missing_count)

#no significant missing values need to be dropped
death_missing_count = df_death.isnull().sum()
print("Count of null values per column for deaths:\n", death_missing_count)

#Gauteng has missing values because of suspected problematic reporting, cases cant be reported unless problems is fixed, other province data can still be used
recover_missing_count = df_recover.isnull().sum()
print("Count of null values per column for recoveries:\n ", recover_missing_count)
df_dropGP_recoveries = df_recover.drop([216,217], axis = 0)
recover_missing_count = df_dropGP_recoveries.isnull().sum()
print("Count of null values per column after removing missing GP values for recoveries:\n ", recover_missing_count)


# In[4]:


#df_confirmed = confrimed cases, used for totals
#df_confirmed_NaNDr = used per province
#deaths = deaths, no missing values
#df_recover  = not for GP values or total
#df_dropGP_recoveries = GP missing values dropped, used for GP and totals

#stats for deaths reported
deaths_stats_EC = df_death["EC"].describe()
print("Basic statistics for the Eastern Cape for deaths reported:\n", deaths_stats_EC)

deaths_stats_FS = df_death["FS"].describe()
print("Basic statistics for the Free State for deaths reported:\n", deaths_stats_FS)

deaths_stats_GP = df_death["GP"].describe()
print("Basic statistics for Gauteng for deaths reported:\n", deaths_stats_GP)

deaths_stats_KZN = df_death["KZN"].describe()
print("Basic statistics for KwaZulu-Natal for deaths reported:\n", deaths_stats_KZN)

deaths_stats_LP = df_death["LP"].describe()
print("Basic statistics for Limpopo for deaths reported:\n", deaths_stats_LP)

deaths_stats_MP = df_death["MP"].describe()
print("Basic statistics for Mpumalanga for deaths reported:\n", deaths_stats_MP)

deaths_stats_NC = df_death["NC"].describe()
print("Basic statistics for the Northern Cape for deaths reported:\n", deaths_stats_NC)

deaths_stats_NW = df_death["NW"].describe()
print("Basic statistics for North West for deaths reported:\n", deaths_stats_NW)

deaths_stats_WC = df_death["WC"].describe()
print("Basic statistics for Western Cape for deaths reported:\n", deaths_stats_WC)

deaths_stats_Uk = df_death["UNKNOWN"].describe()
print("Basic statistics with unknown location for deaths reported:\n", deaths_stats_Uk)

#remove space from data
df_death["total"] = df_death["total"].replace("52 846", 52846)
df_death["total"] = df_death["total"].astype(float)
deaths_stats_tot = df_death["total"].describe()
print("Basic statistics for total deaths reported:\n", deaths_stats_tot)


# In[5]:


#confirmed cases stats
confirm_stats_EC = df_confirmed_NaNDr["EC"].describe()
print("Basic statistics for the Eastern Cape for confirmed cases:\n", confirm_stats_EC)

confirm_stats_FS = df_confirmed_NaNDr["FS"].describe()
print("Basic statistics for the Free State for confirmed cases:\n", confirm_stats_FS)

confirm_stats_GP = df_confirmed_NaNDr["GP"].describe()
print("Basic statistics for Gauteng for confirmed cases:\n", confirm_stats_GP)

confirm_stats_KZN = df_confirmed_NaNDr["KZN"].describe()
print("Basic statistics for KwaZulu-Natal for confirmed cases:\n", confirm_stats_KZN)

confirm_stats_LP = df_confirmed_NaNDr["LP"].describe()
print("Basic statistics for Limpopo for confirmed cases:\n", confirm_stats_LP)

confirm_stats_MP = df_confirmed_NaNDr["MP"].describe()
print("Basic statistics for Mpumalanga for confirmed cases:\n", confirm_stats_MP)

confirm_stats_NC = df_confirmed_NaNDr["NC"].describe()
print("Basic statistics for the Northern Cape for confirmed cases:\n", confirm_stats_NC)

confirm_stats_NW = df_confirmed_NaNDr["NW"].describe()
print("Basic statistics for North West for confirmed cases:\n", confirm_stats_NW)

confirm_stats_WC = df_confirmed_NaNDr["WC"].describe()
print("Basic statistics for Western Cape for confirmed cases:\n", confirm_stats_WC)

confirm_stats_Uk = df_confirmed_NaNDr["UNKNOWN"].describe()
print("Basic statistics with unknown location for confirmed cases:\n", confirm_stats_Uk)

confirm_stats_tot = df_confirmed["total"].describe()
print("Basic statistics for total confirmed cases:\n", confirm_stats_tot)


# In[6]:


#recoveries
recover_stats_EC = df_recover["EC"].describe()
print("Basic statistics for the Eastern Cape for recoveries:\n", confirm_stats_EC)

recover_stats_FS = df_recover["FS"].describe()
print("Basic statistics for the Free State for recoveries:\n", recover_stats_FS)

recover_stats_GP = df_dropGP_recoveries["GP"].describe()
print("Basic statistics for Gauteng for recoveries:\n", recover_stats_GP)

recover_stats_KZN = df_recover["KZN"].describe()
print("Basic statistics for KwaZulu-Natal for recoveries:\n", recover_stats_KZN)

recover_stats_LP = df_recover["LP"].describe()
print("Basic statistics for Limpopo for recoveries:\n", recover_stats_LP)

recover_stats_MP = df_recover["MP"].describe()
print("Basic statistics for Mpumalanga for recoveries:\n", recover_stats_MP)

recover_stats_NC = df_recover["NC"].describe()
print("Basic statistics for the Northern Cape for recoveries:\n", recover_stats_NC)

recover_stats_NW = df_recover["NW"].describe()
print("Basic statistics for North West for recoveries:\n", recover_stats_NW)

recover_stats_WC = df_recover["WC"].describe()
print("Basic statistics for Western Cape for recoveries:\n", recover_stats_WC)

recover_stats_Uk = df_recover["UNKNOWN"].describe()
print("Basic statistics with unknown location for recoveries:\n", recover_stats_Uk)

recover_stats_tot = df_dropGP_recoveries["total"].describe()
print("Basic statistics for total recoveries:\n", recover_stats_tot)


# In[7]:


df_death["date"] = pd.to_datetime(df_death["date"],format='%d-%m-%Y')
df_death["month"] = df_death['date'].dt.to_period('M')

ECdeath = df_death.iloc[:, [2,14]].groupby(["month"]).mean()
print("Average deaths per month and year for the Eastern Cape:\n", ECdeath)

FSdeath = df_death.iloc[:, [3,14]].groupby(["month"]).mean()
print("Average deaths per month and year for the Free State:\n", FSdeath)

GPdeath = df_death.iloc[:, [4,14]].groupby(["month"]).mean()
print("Average deaths per month and year for Gauteng:\n", GPdeath)

KZNdeath = df_death.iloc[:, [5,14]].groupby(["month"]).mean()
print("Average deaths per month and year for KwaZulu-Natal:\n", KZNdeath)

LPdeath = df_death.iloc[:, [6,14]].groupby(["month"]).mean()
print("Average deaths per month and year for Limpopo:\n", LPdeath)

MPdeath = df_death.iloc[:, [7,14]].groupby(["month"]).mean()
print("Average deaths per month and year for Mpumalanga:\n", MPdeath)

NCdeath = df_death.iloc[:, [8,14]].groupby(["month"]).mean()
print("Average deaths per month and year for the Northern Cape:\n", NCdeath)

NWdeath = df_death.iloc[:, [9,14]].groupby(["month"]).mean()
print("Average deaths per month and year for the North West:\n", NWdeath)

WCdeath = df_death.iloc[:, [10,14]].groupby(["month"]).mean()
print("Average deaths per month and year for the Western Cape:\n", WCdeath)

Ukdeath = df_death.iloc[:, [11,14]].groupby(["month"]).mean()
print("Average deaths per month and year with Unknown location:\n", Ukdeath)

totdeath = df_death.iloc[:, [12,14]].groupby(["month"]).mean()
print("Total average deaths per month and year:\n", totdeath)


# In[8]:


#group by month and year for total confirmed cases
df_confirmed["date"] = pd.to_datetime(df_confirmed["date"],format='%d-%m-%Y')
df_confirmed["month"] = df_confirmed['date'].dt.to_period('M')
totconfirmed = df_confirmed.iloc[:, [12,14]].groupby(["month"]).mean()
print("Total average confirmed cases per month and year:\n", totconfirmed)


# In[9]:


#group by month and year for province confirmed cases
df_confirmed_NaNDr["date"] = pd.to_datetime(df_confirmed_NaNDr["date"],format='%d-%m-%Y')
df_confirmed_NaNDr["month"] = df_confirmed_NaNDr['date'].dt.to_period('M')

ECconfirmed = df_confirmed_NaNDr.iloc[:, [2,14]].groupby(["month"]).mean()
print("Average confirmed cases per month and year for the Eastern Cape:\n", ECconfirmed)

FSconfirmed = df_confirmed_NaNDr.iloc[:, [3,14]].groupby(["month"]).mean()
print("Average confirmed cases  per month and year for the Free State:\n", FSconfirmed)

GPconfirmed = df_confirmed_NaNDr.iloc[:, [4,14]].groupby(["month"]).mean()
print("Average confirmed cases  per month and year for Gauteng:\n", GPconfirmed)

KZNconfirmed = df_confirmed_NaNDr.iloc[:, [5,14]].groupby(["month"]).mean()
print("Average confirmed cases  per month and year for KwaZulu-Natal:\n", KZNconfirmed)

LPconfirmed = df_confirmed_NaNDr.iloc[:, [6,14]].groupby(["month"]).mean()
print("Average confirmed cases per month and year for Limpopo:\n", LPconfirmed)

MPconfirmed = df_confirmed_NaNDr.iloc[:, [7,14]].groupby(["month"]).mean()
print("Average confirmed cases per month and year for Mpumalanga:\n", MPconfirmed)

NCconfirmed = df_confirmed_NaNDr.iloc[:, [8,14]].groupby(["month"]).mean()
print("Average confirmed cases per month and year for the Northern Cape:\n", NCconfirmed)

NWconfirmed = df_confirmed_NaNDr.iloc[:, [9,14]].groupby(["month"]).mean()
print("Average confirmed cases per month and year for the North West:\n", NWconfirmed)

WCconfirmed= df_confirmed_NaNDr.iloc[:, [10,14]].groupby(["month"]).mean()
print("Average confirmed cases per month and year for the Western Cape:\n", WCconfirmed)

Ukconfirmed = df_confirmed_NaNDr.iloc[:, [11,14]].groupby(["month"]).mean()
print("Average confirmed cases per month and year with Unknown location:\n", Ukconfirmed)


# In[10]:


#average recoveries per month and year
df_recover["date"] = pd.to_datetime(df_recover["date"],format='%d-%m-%Y')
df_recover["month"] = df_recover['date'].dt.to_period('M')
df_dropGP_recoveries["date"] = pd.to_datetime(df_dropGP_recoveries["date"],format='%d-%m-%Y')
df_dropGP_recoveries["month"] = df_dropGP_recoveries['date'].dt.to_period('M')


ECrecover = df_recover.iloc[:, [2, 14]].groupby(["month"]).mean()
print("Average recoveries per month and year for the Eastern Cape:\n", ECrecover)

FSrecover = df_recover.iloc[:, [3,14]].groupby(["month"]).mean()
print("Average recoveries per month and year for the Free State:\n", FSrecover)

GPrecover = df_dropGP_recoveries.iloc[:, [4,14]].groupby(["month"]).mean()
print("Average recoveries  per month and year for Gauteng:\n", GPrecover)

KZNrecover = df_recover.iloc[:, [5,14]].groupby(["month"]).mean()
print("Average recoveries  per month and year for KwaZulu-Natal:\n", KZNrecover)

LPrecover = df_recover.iloc[:, [6,14]].groupby(["month"]).mean()
print("Average recoveries per month and year for Limpopo:\n", LPrecover)

MPrecover = df_recover.iloc[:, [7,14]].groupby(["month"]).mean()
print("Average recoveries per month and year for Mpumalanga:\n", MPrecover)

NCrecover = df_recover.iloc[:, [8,14]].groupby(["month"]).mean()
print("Average recoveries per month and year for the Northern Cape:\n", NCrecover)

NWrecover = df_recover.iloc[:, [9,14]].groupby(["month"]).mean()
print("Average recoveries per month and year for the North West:\n", NWrecover)

WCrecover = df_recover.iloc[:, [10,14]].groupby(["month"]).mean()
print("Average recoveries per month and year for the Western Cape:\n", WCrecover)

Ukrecover = df_recover.iloc[:, [11,14]].groupby(["month"]).mean()
print("Average recoveries per month and year with Unknown location:\n", Ukrecover)

totrecover = df_dropGP_recoveries.iloc[:, [12,14]].groupby(["month"]).mean()
print("Total average recoveries per month and year:\n", totrecover)


# In[11]:


#plots and charts
#Make a fiter for provinces
prov = ["Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal", "Limpopo", "Mpumalanga", "Norhtern Cape", "North West", "Western Cape", "Unknown"]

plt.boxplot(df_death.iloc[:,2:12], showmeans=True, meanline=True, labels=prov)
plt.xlabel("Province", fontsize = 16)
plt.ylabel("Number of Deaths")
plt.xticks(rotation = 90)

plt.gcf().set_size_inches([20, 10])
plt.title("Box Plot for Deaths per Province", fontsize = 20, fontweight = 'bold')
plt.show()

plt.boxplot(df_recover.iloc[:,2:12], showmeans=True, meanline=True, labels=prov)
plt.xlabel("Province",fontsize = 16)
plt.ylabel("Number of Recoveries")
plt.xticks(rotation = 90)
plt.gcf().set_size_inches([20, 10])
plt.title("Box Plot for Recoveries per Province", fontsize = 20, fontweight = 'bold')
plt.show()

plt.boxplot(df_confirmed_NaNDr.iloc[:,2:12], showmeans=True, meanline=True, labels=prov)
plt.xlabel("Province",fontsize = 16)
plt.ylabel("Number of Confirmed Cases")
plt.xticks(rotation = 90)
plt.gcf().set_size_inches([20, 10])
plt.title("Box Plot for Confirmed Cases per Province", fontsize = 20, fontweight = 'bold')
plt.show()


# In[12]:


#Plot per month-Deaths
ECdeath.plot(kind = 'line')
plt.title("Average deaths per month for the Eastern Cape")
plt.ylabel("Average Deaths")
plt.xlabel("Month")

FSdeath.plot(kind = 'line')
plt.title("Average deaths per month for the Free State")
plt.ylabel("Average Deaths")
plt.xlabel("Month")

GPdeath.plot(kind = 'line')
plt.title("Average deaths per month for Gauteng")
plt.ylabel("Average Deaths")
plt.xlabel("Month")

KZNdeath.plot(kind = 'line')
plt.title("Average deaths per month for KwaZulu-Natal")
plt.ylabel("Average Deaths")
plt.xlabel("Month")

LPdeath.plot(kind = 'line')
plt.title("Average deaths per month for Limpopo")
plt.ylabel("Average Deaths")
plt.xlabel("Month")

MPdeath.plot(kind = 'line')
plt.title("Average deaths per month for Mpumalanga")
plt.ylabel("Average Deaths")
plt.xlabel("Month")

NCdeath.plot(kind = 'line')
plt.title("Deaths per month for the Northern Cape")
plt.ylabel("Average Deaths")
plt.xlabel("Month")

NWdeath.plot(kind = 'line')
plt.title("Average deaths per month for North West")
plt.ylabel("Average Deaths")
plt.xlabel("Month")

WCdeath.plot(kind = 'line')
plt.title("Average deaths per month for the Western Cape")
plt.ylabel("Average Deaths")
plt.xlabel("Month")

Ukdeath.plot(kind = 'line')
plt.title("Average deaths per month for Unknown locations")
plt.ylabel("Average Deaths")
plt.xlabel("Month")

totdeath.plot(kind = 'line')
plt.title("Average total deaths per month")
plt.ylabel("Average Deaths")
plt.xlabel("Month")

plt.show()


# In[13]:


#recoveries per month
ECrecover.plot(kind = 'line')
plt.title("Average recoveries per month for the Eastern Cape")
plt.ylabel("Average Recovercies")
plt.xlabel("Month")

FSrecover.plot(kind = 'line')
plt.title("Average recoveries per month for the Free State")
plt.ylabel("Average Recovercies")
plt.xlabel("Month")

GPrecover.plot(kind = 'line')
plt.title("Average recoveries per month for Gauteng")
plt.ylabel("Average Recovercies")
plt.xlabel("Month")

KZNrecover.plot(kind = 'line')
plt.title("Average recoveries per month for KwaZulu-Natal")
plt.ylabel("Average Recovercies")
plt.xlabel("Month")

LPrecover.plot(kind = 'line')
plt.title("Average recoveries per month for Limpopo")
plt.ylabel("Average Recovercies")
plt.xlabel("Month")

MPrecover.plot(kind = 'line')
plt.title("Average recoveries per month for Mpumalanga")
plt.ylabel("Average Recovercies")
plt.xlabel("Month")

NCrecover.plot(kind = 'line')
plt.title("Average recoveries per month for the Northern Cape")
plt.ylabel("Average Recovercies")
plt.xlabel("Month")

NWrecover.plot(kind = 'line')
plt.title("Average recoveries per month for North West")
plt.ylabel("Average Recovercies")
plt.xlabel("Month")

WCrecover.plot(kind = 'line')
plt.title("Average recoveries per month for Western Cape")
plt.ylabel("Average Recovercies")
plt.xlabel("Month")

Ukrecover.plot(kind = 'line')
plt.title("Average recoveries per month for Unknown locations")
plt.ylabel("Average Recovercies")
plt.xlabel("Month")

totrecover.plot(kind = 'line')
plt.title("Average total recoveries per month")
plt.ylabel("Average Recovercies")
plt.xlabel("Month")

plt.show()


# In[14]:


#confirmed cases per month
ECconfirmed.plot(kind = 'line')
plt.title("Average confirmed cases per month for the Eastern Cape")
plt.ylabel("Average Confirmed Cases")
plt.xlabel("Month")

FSconfirmed.plot(kind = 'line')
plt.title("Average confirmed cases per month for the Free State")
plt.ylabel("Average Confirmed Cases")
plt.xlabel("Month")

GPconfirmed.plot(kind = 'line')
plt.title("Average confirmed cases per month for Gauteng")
plt.ylabel("Average Confirmed Cases")
plt.xlabel("Month")

KZNconfirmed.plot(kind = 'line')
plt.title("Average confirmed cases per month for KwaZulu-Natal")
plt.ylabel("Average Confirmed Cases")
plt.xlabel("Month")

LPconfirmed.plot(kind = 'line')
plt.title("Average confirmed cases per month for Limpopo")
plt.ylabel("Average Confirmed Cases")
plt.xlabel("Month")

MPconfirmed.plot(kind = 'line')
plt.title("Average confirmed cases per month for Mpumalanga")
plt.ylabel("Average Confirmed Cases")
plt.xlabel("Month")

NCconfirmed.plot(kind = 'line')
plt.title("Average confirmed cases per month for the Northern Cape")
plt.ylabel("Average Confirmed Cases")
plt.xlabel("Month")

NWconfirmed.plot(kind = 'line')
plt.title("Average confirmed cases per month for North West")
plt.ylabel("Average Confirmed Cases")
plt.xlabel("Month")

WCconfirmed.plot(kind = 'line')
plt.title("Average confirmed cases per month for the Western Cape")
plt.ylabel("Average Confirmed Cases")
plt.xlabel("Month")

Ukconfirmed.plot(kind = 'line')
plt.title("Average confirmed cases per month for Unknown locations")
plt.ylabel("Average Confirmed Cases")
plt.xlabel("Month")

totconfirmed.plot(kind = 'line')
plt.title("Average total confirmed cases per month")
plt.ylabel("Average Confirmed Cases")
plt.xlabel("Month")

plt.show()


# In[ ]:





# In[15]:


#read SAPS files for Q1
df_q1SASo = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q1_SASo.xlsx")
df_q1ProvSo = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q1_ProvSo.xlsx")
df_q1Srape = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q1_Station_Rape.xlsx")
df_q1SSexAs  = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q1SSexAs.xlsx")
df_q1Satmp = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q1SAtSo.xlsx")
df_q1Scont = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q1SConSo.xlsx")
df_q1Tembisa = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\q1Tembisa.xlsx")
df_q1Sandton = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q1Sandton.xlsx")


# In[16]:


#clean data
df_q1Sandton["% Change"] = df_q1Sandton["% Change"].replace("0 Cases", 0)

#stats for SA sexual offences
q1SAstats = df_q1SASo.iloc[0:4,0:5].describe()
print("Basic Quarter 1 Statistics for the Republic of South Africa:\n",q1SAstats)

#Stats per province
q1provstats = df_q1ProvSo.iloc[[0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18,20,21,22,23,25,26,27,28,30,31,32,33,35,36,37,38,40,41,42,43],[0,1,2,3,4,5,8]].groupby(["Province"]).describe()
print("Basic Quarter 1 Statistics per Province:\n",q1provstats)

#Top 30 Station Rape Stat
q1Srape = df_q1Srape.iloc[:,1:7].groupby(["Province"]).describe()
print("Basic Quarter 1 Statistics for the top 30 Stations for Rape:\n",q1Srape)

#Top 30 Station Sexual Assault
q1SSexAs = df_q1SSexAs.iloc[:,1:7].groupby(["Province"]).describe()
print("Basic Quarter 1 Statistics for the top 30 Stations for Sexual Assault:\n",q1SSexAs)

#Top 30 Station Attempted Sexual Assault
q1Satmp = df_q1Satmp.iloc[:,1:7].groupby(["Province"]).describe()
print("Basic Quarter 1 Statistics for the top 30 Stations for Attempted Sexual Assault:\n",q1Satmp)

#Top 30 Station Contact Sexual Assault
q1Scont = df_q1Scont.iloc[:,1:7].groupby(["Province"]).describe()
print("Basic Quarter 1 Statistics for the top 30 Stations for Contact Sexual Assault:\n",q1Scont)

#Stats for low income area in Gauteng (Tembisa)
q1Tembisa = df_q1Tembisa.iloc[0:4,0:5].describe()
print("Basic Quarter 1 Statistics for Tembisa:\n",q1Tembisa)

#Stats for High income area in Gauteng (Sandton)
q1Sandton = df_q1Sandton.iloc[0:4, 0:5].describe()
print("Basic Quarter 1 Statistics for Sandton:\n",q1Sandton)


# In[17]:


#charts for SA Q1
df_q1SASo.iloc[0,1:5].plot(kind = "line")
plt.title("Change in Number of Rape Cases for SA during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1SASo.iloc[1,1:5].plot(kind = "line")
plt.title("Change in Number of Sexual Assault Cases for SA during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1SASo.iloc[2,1:5].plot(kind = "line")
plt.title("Change in Number of Attempted Sexual Offence Cases for SA during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1SASo.iloc[3,1:5].plot(kind = "line")
plt.title("Change in Number of Contact Sexual Offence Cases for SA during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1SASo.iloc[4,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for SA during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()


# In[18]:


#Quarter 1 Provincial Graphs
df_q1ProvSo.iloc[0,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for the Eastern Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[1,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for the Eastern Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[2,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for the Eastern Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[3,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for the Eastern Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[4,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for the Eastern Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[5,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for the Eastern Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[6,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for the Free State during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[7,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for the Free State during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[8,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for the Free State during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[9,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for the Free State during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[10,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for Gauteng during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[11,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for Gauteng during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[12,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for Gauteng during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[13,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for Gauteng during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[14,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for Gauteng during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[15,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for KwaZulu-Natal during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[16,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for KwaZulu-Natal during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[17,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for KwaZulu-Natal during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[18,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for KwaZulu-Natal during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[19,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for KwaZulu-Natal during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[20,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for Limpopo during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[21,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for Limpopo during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[22,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for Limpopo during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[23,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for Limpopo during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[24,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for Limpopo during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[25,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for Mpumalanga during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[26,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for Mpumalanga during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[27,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for Mpumalanga during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[28,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for Mpumalanga during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[29,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for Mpumalanga during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[30,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for the Northern Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[31,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for the Northern Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[32,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for the Northern Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[33,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for the Northern Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[34,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for the Northern Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[35,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for North West during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[36,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for North West during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[37,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for North West during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[38,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for North West during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[39,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for North West during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[40,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for the Western Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[41,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for the Western Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[42,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for the Western Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[43,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for the Western Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q1ProvSo.iloc[44,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for the Western Cape during Quarter 1")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()


# In[19]:


#Comparing high and low income
df_q1Sandton.iloc[0,1:5].plot(kind = "line")
df_q1Tembisa.iloc[0,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Rape Cases For Sandton (high income) and Tembisa (low income) in Gauteng for Quarter 1")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q1Sandton.iloc[1,1:5].plot(kind = "line")
df_q1Tembisa.iloc[1,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Sexual Assault Cases For Sandton (high income) and Tembisa (low income) in Gauteng for Quarter 1")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q1Sandton.iloc[2,1:5].plot(kind = "line")
df_q1Tembisa.iloc[2,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Attempted Sexual Offence Cases For Sandton (high income) and Tembisa (low income) in Gauteng for Quarter 1")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q1Sandton.iloc[3,1:5].plot(kind = "line")
df_q1Tembisa.iloc[3,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Contact Sexual Offence Cases For Sandton (high income) and Tembisa (low income) in Gauteng for Quarter 1")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q1Sandton.iloc[4,1:5].plot(kind = "line")
df_q1Tembisa.iloc[4,1:5].plot(kind = "line", color = "red")
plt.title("Change in Total Number of Sexual Offence Cases For Sandton (high income) and Tembisa (low income) in Gauteng for Quarter 1")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()


# In[20]:


#Read SAPS Q2 data
df_q2SASo = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q2SASo.xlsx")
df_q2ProvSo = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q2ProvSo.xlsx")
df_q2Srape = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q2Srape.xlsx")
df_q2SSexAs  = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q2SsexAs.xlsx")
df_q2Satmp = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q2Satmp.xlsx")
df_q2Scont = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q2Scont.xlsx")
df_q2Tembisa = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q2Tembisa.xlsx")
df_q2Sandton = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q2Sandton.xlsx")


# In[21]:


#clean data
df_q2Sandton["% Change"] = df_q2Sandton["% Change"].replace("0 Cases", 0)


# In[22]:


#stats for SA sexual offences
q2SAstats = df_q2SASo.iloc[0:4,0:5].describe()
print("Basic Statistics for South Africa for Quarter 2:\n",q2SAstats)

#Stats per province
q2provstats = df_q2ProvSo.iloc[[0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18,20,21,22,23,25,26,27,28,30,31,32,33,35,36,37,38,40,41,42,43],[0,1,2,3,4,5,8]].groupby(["Province"]).describe()
print("Basic Statistics for South Africa Provinces for Quarter 2:\n",q2provstats)

#Top 30 Station Rape Stat
q2Srape = df_q2Srape.iloc[:,1:7].groupby(["Province"]).describe()
print("Basic Statistics for Top 30 Stations for Rape Cases for Quarter 2:\n",q2Srape)

#Top 30 Station Sexual Assault
q2SSexAs = df_q2SSexAs.iloc[:,1:7].groupby(["Province"]).describe()
print("Basic Statistics for Top 30 Stations for Sexual Assault Cases for Quarter 2:\n",q2SSexAs)

#Top 30 Station Attempted Sexual Assault
q2Satmp = df_q2Satmp.iloc[:,1:7].groupby(["Province"]).describe()
print("Basic Statistics for Top 30 Stations for Attempted Sexual Assault Cases for Quarter 2:\n", q2Satmp)

#Top 30 Station Contact Sexual Assault
q2Scont = df_q2Scont.iloc[:,1:7].groupby(["Province"]).describe()
print("Basic Statistics for Top 30 Stations for Contact Sexual Assault Cases for Quarter 2:\n",q2Scont)

#Stats for low income area in Gauteng (Tembisa)
q2Tembisa = df_q2Tembisa.iloc[0:4,0:5].describe()
print("Basic Statistics for Tembisa for Quarter 2:\n", q2Tembisa)

#Stats for High income area in Gauteng (Sandton)
q2Sandton = df_q2Sandton.iloc[0:4, 0:5].describe()
print("Basic Statistics for Sandton for Quarter 2:\n",q2Sandton)


# In[23]:


#Charts for SA Q2
df_q2SASo.iloc[0,1:5].plot(kind = "line")
plt.title("Change in Number of Rape Cases for SA during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2SASo.iloc[1,1:5].plot(kind = "line")
plt.title("Change in Number of Sexual Assault Cases for SA during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2SASo.iloc[2,1:5].plot(kind = "line")
plt.title("Change in Number of Attempted Sexual Offence Cases for SA during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2SASo.iloc[3,1:5].plot(kind = "line")
plt.title("Change in Number of Contact Sexual Offence Cases for SA during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2SASo.iloc[4,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for SA during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()


# In[24]:


#per province
df_q2ProvSo.iloc[0,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for the Eastern Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[1,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for the Eastern Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[2,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for the Eastern Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[3,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for the Eastern Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[4,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for the Eastern Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[5,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for the Free State during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[6,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for the Free State during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[7,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for the Free State during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[8,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for the Free State during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[9,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for the Free State during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[10,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for Gauteng during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[11,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for Gauteng during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[12,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for Gauteng during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[13,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for Gauteng during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[14,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for Gauteng during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[15,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for KwaZulu-Natal during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[16,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for KwaZulu-Natal during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[17,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for KwaZulu-Natal during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[18,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for KwaZulu-Natal during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[19,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for KwaZulu-Natal during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[20,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for Limpopo during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[21,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for Limpopo during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[22,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for Limpopo during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[23,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for Limpopo during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[24,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for Limpopo during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[25,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for Mpumalanga during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[26,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for Mpumalanga during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[27,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for Mpumalanga during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[28,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for Mpumalanga during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[29,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for Mpumalanga during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[30,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for the Northern Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[31,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for the Northern Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[32,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for the Northern Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[33,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for the Northern Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[34,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for the Northern Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[35,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for North West during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[36,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for North West during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[37,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for North West during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[38,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for North West during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[39,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for North West during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[40,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for the Western Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[41,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for the Western Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[42,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for the Western Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[43,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for the Western Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q2ProvSo.iloc[44,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for the Western Cape during Quarter 2")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()


# In[25]:


#comparing sandton and tembisa
df_q2Sandton.iloc[0,1:5].plot(kind = "line")
df_q2Tembisa.iloc[0,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Rape Cases For Sandton and Tembisa in Gauteng for Quarter 2")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q2Sandton.iloc[1,1:5].plot(kind = "line")
df_q2Tembisa.iloc[1,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Sexual Assault Cases For Sandton and Tembisa in Gauteng for Quarter 2")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q2Sandton.iloc[2,1:5].plot(kind = "line")
df_q2Tembisa.iloc[2,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Attempted Sexual Offence Cases For Sandton and Tembisa in Gauteng for Quarter 2")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q2Sandton.iloc[3,1:5].plot(kind = "line")
df_q2Tembisa.iloc[3,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Contact Sexual Offence Cases For Sandton and Tembisa in Gauteng for Quarter 2")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q2Sandton.iloc[4,1:5].plot(kind = "line")
df_q2Tembisa.iloc[4,1:5].plot(kind = "line", color = "red")
plt.title("Change in Total Number of Sexual Offence Cases For Sandton and Tembisa in Gauteng for Quarter 2")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()


# In[26]:


#read Q3 SAPS
df_q3SASo = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q3SASo.xlsx")
df_q3ProvSo = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q3ProvSo.xlsx")
df_q3SSo = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q3SSo.xlsx")
df_q3Tembisa = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q3Tembisa.xlsx")
df_q3Sandton = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\Q3Sandton.xlsx")


# In[27]:


#clean data
df_q3Sandton["% Change"] = df_q3Sandton["% Change"].replace("0 Cases", 0)


# In[28]:


#stats for SA sexual offences
q3SAstats = df_q3SASo.iloc[0:4,0:5].describe()
print("Basic Statistics for South Africa for Quarter 3:\n",q3SAstats)

#Stats per province
q3provstats = df_q3ProvSo.iloc[[0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18,20,21,22,23,25,26,27,28,30,31,32,33,35,36,37,38,40,41,42,43],[0,1,2,3,4,5,8]].groupby(["Province"]).describe()
print("Basic Statistics for South Africa Provinces for Quarter 3:\n",q3provstats)

#Sexual Offence Stats for Top 30 Stations
q3Stat30  = df_q3SSo.iloc[:, 1:8].groupby(["Province"]).describe()
print("Basic Statistics per Province for the Top 30 Stations for Quarter 3:\n", q3Stat30)


# In[29]:


#Stats for low income area in Gauteng (Tembisa)
q3Tembisa = df_q3Tembisa.iloc[0:4,0:5].describe()
print("Basic Statistics for Tembisa for Quarter 3:\n", q3Tembisa)

#Stats for High income area in Gauteng (Sandton)
q3Sandton = df_q3Sandton.iloc[0:4, 0:5].describe()
print("Basic Statistics for Sandton for Quarter 3:\n",q3Sandton)


# In[30]:


#Charts for SA
df_q3SASo.iloc[0,1:5].plot(kind = "line")
plt.title("Change in Number of Rape Cases for SA during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3SASo.iloc[1,1:5].plot(kind = "line")
plt.title("Change in Number of Sexual Assault Cases for SA during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3SASo.iloc[2,1:5].plot(kind = "line")
plt.title("Change in Number of Attempted Sexual Offence Cases for SA during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3SASo.iloc[3,1:5].plot(kind = "line")
plt.title("Change in Number of Contact Sexual Offence Cases for SA during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3SASo.iloc[4,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for SA during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()


# In[31]:


#per province
df_q3ProvSo.iloc[0,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for the Eastern Cape during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[1,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for the Eastern Cape during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[2,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for the Eastern Cape during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[3,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for the Eastern Cape during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[4,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for the Eastern Cape during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[5,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for the Free State during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[6,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for the Free State during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[7,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for the Free State during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[8,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for the Free State during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[9,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for the Free State during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[10,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for Gauteng during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[11,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for Gauteng during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[12,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for Gauteng during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[13,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for Gauteng during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[14,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for Gauteng during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[15,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for KwaZulu-Natal during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[16,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for KwaZulu-Natal during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[17,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for KwaZulu-Natal during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[18,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for KwaZulu-Natal during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[19,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for KwaZulu-Natal during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[20,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for Limpopo during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[21,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for Limpopo during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[22,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for Limpopo during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[23,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for Limpopo during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[24,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for Limpopo during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[25,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for Mpumalanga during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[26,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for Mpumalanga during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[27,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for Mpumalanga during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[28,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for Mpumalanga during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[29,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for Mpumalanga during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[30,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for the Northern Cape during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[31,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for the Northern Cape during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[32,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for the Northern Cape during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[33,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for the Northern Cape during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[34,1:5].plot(kind = "line")
plt.title("Change in the Total Number of Sexual Offence Cases for the Northern Cape during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[35,1:5].plot(kind = "line")
plt.title("Change in the Number of Rape Cases for North West during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[36,1:5].plot(kind = "line")
plt.title("Change in the Number of Sexual Assault Cases for North West during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[37,1:5].plot(kind = "line")
plt.title("Change in the Number of Attempted Sexual Offence Cases for North West during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_q3ProvSo.iloc[38,1:5].plot(kind = "line")
plt.title("Change in the Number of Contact Sexual Offence Cases for North West during Quarter 3")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()


# In[32]:


#Charts for unequal income
df_q3Sandton.iloc[0,1:5].plot(kind = "line")
df_q3Tembisa.iloc[0,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Rape Cases For Sandton and Tembisa in Gauteng for Quarter 3")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q3Sandton.iloc[1,1:5].plot(kind = "line")
df_q3Tembisa.iloc[1,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Sexual Assault Cases For Sandton and Tembisa in Gauteng for Quarter 3")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q3Sandton.iloc[2,1:5].plot(kind = "line")
df_q3Tembisa.iloc[2,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Attempted Sexual Offence Cases For Sandton and Tembisa in Gauteng for Quarter 3")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q3Sandton.iloc[3,1:5].plot(kind = "line")
df_q3Tembisa.iloc[3,1:5].plot(kind = "line", color = "red")
plt.title("Change in Number of Contact Sexual Offence Cases For Sandton and Tembisa in Gauteng for Quarter 3")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_q3Sandton.iloc[4,1:5].plot(kind = "line")
df_q3Tembisa.iloc[4,1:5].plot(kind = "line", color = "red")
plt.title("Change in Total Number of Sexual Offence Cases For Sandton and Tembisa in Gauteng for Quarter 3")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()


# In[33]:


#read Yearly Stats
df_ySASo = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\ySASo.xlsx")
df_yProvSo = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\yProvSo.xlsx")
df_ySSo = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\ySSo.xlsx")
df_yTembisa = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\yTembisa.xlsx")
df_ySandton = pd.read_excel(r"C:\Users\ruveb\Desktop\Assignmnets\GIS311_Assignment1_16062664\ySandton.xlsx")


# In[34]:


#SA yearly stats
#stats for SA sexual offences
ySAstats = df_ySASo.iloc[0:4,0:11].describe()
print("Basic Yearly Statistics for South Africa:\n",ySAstats)


# In[35]:


#SA stats per Province
#Stats per province
yprovstats = df_yProvSo.iloc[[0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18,20,21,22,23,25,26,27,28,30,31,32,33,35,36,37,38,40,41,42,43],[0,1,2,3,4,5,6,7,8,9,10,13]].groupby(["Province"]).describe()
print("Basic Yearly Statistics for South Africa Provinces:\n",yprovstats)


# In[36]:


#Sexual Offence Stats for Top 30 Stations
yStat30  = df_ySSo.iloc[:, 0:11].groupby(["Province"]).describe()
print("Basic Yearly Statistics per Province for the Top 30 Stations:\n", yStat30)


# In[37]:


#Stats for low income area in Gauteng (Tembisa)
yTembisa = df_yTembisa.iloc[0:4,0:11].describe()
print("Basic Yearly Statistics for Tembisa:\n", yTembisa)

#Stats for High income area in Gauteng (Sandton)
ySandton = df_ySandton.iloc[0:4, 0:11].describe()
print("Basic Yearly Statistics for Sandton:\n",ySandton)


# In[38]:


#charts
df_ySASo.iloc[0,1:11].plot(kind = "line")
plt.title("Change in Yearly Number of Rape Cases for SA")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_ySASo.iloc[1,1:11].plot(kind = "line")
plt.title("Change in Yearly Number of Sexual Assault Cases for SA")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_ySASo.iloc[2,1:11].plot(kind = "line")
plt.title("Change in Yearly Number of Attempted Sexual Offence Cases for SA")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_ySASo.iloc[3,1:11].plot(kind = "line")
plt.title("Change in Yearly Number of Contact Sexual Offence Cases for SA")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_ySASo.iloc[4,1:11].plot(kind = "line")
plt.title("Change in the Yearly Total Number of Sexual Offence Cases for SA")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()


# In[39]:


#stats per province
df_yProvSo.iloc[0,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Rape Cases for the Eastern Cape")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[1,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Sexual Assault Cases for the Eastern Cape")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[2,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Attempted Sexual Offence Cases for the Eastern Cape")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[3,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Contact Sexual Offence Cases for the Eastern Cape during")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[4,1:11].plot(kind = "line")
plt.title("Change in the Yearly Total Number of Sexual Offence Cases for the Eastern Cape")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[5,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Rape Cases for the Free State")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[6,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Sexual Assault Cases for the Free State")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[7,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Attempted Sexual Offence Cases for the Free State")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[8,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Contact Sexual Offence Cases for the Free State")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[9,1:11].plot(kind = "line")
plt.title("Change in the Yearly Total Number of Sexual Offence Cases for the Free State")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[10,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Rape Cases for Gauteng")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[11,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Sexual Assault Cases for Gauteng")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[12,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Attempted Sexual Offence Cases for Gauteng")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[13,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Contact Sexual Offence Cases for Gauteng")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[14,1:11].plot(kind = "line")
plt.title("Change in the Yearly Total Number of Sexual Offence Cases for Gauteng")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[15,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Rape Cases for KwaZulu-Natal")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[16,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Sexual Assault Cases for KwaZulu-Natal")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[17,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Attempted Sexual Offence Cases for KwaZulu-Natal")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[18,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Contact Sexual Offence Cases for KwaZulu-Natal")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[19,1:11].plot(kind = "line")
plt.title("Change in the Yearly Total Number of Sexual Offence Cases for KwaZulu-Natal")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[20,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Rape Cases for Limpopo")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[21,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Sexual Assault Cases for Limpopo")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[22,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Attempted Sexual Offence Cases for Limpopo")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[23,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Contact Sexual Offence Cases for Limpopo")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[24,1:11].plot(kind = "line")
plt.title("Change in the Yearly Total Number of Sexual Offence Cases for Limpopo")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[25,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Rape Cases for Mpumalanga")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[26,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Sexual Assault Cases for Mpumalanga")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[27,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Attempted Sexual Offence Cases for Mpumalanga")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[28,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Contact Sexual Offence Cases for Mpumalanga")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[29,1:11].plot(kind = "line")
plt.title("Change in the Yearly Total Number of Sexual Offence Cases for Mpumalanga")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[30,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Rape Cases for the Northern Cape")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[31,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Sexual Assault Cases for the Northern Cape")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[32,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Attempted Sexual Offence Cases for the Northern Cape")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[33,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Contact Sexual Offence Cases for the Northern Cape")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[34,1:11].plot(kind = "line")
plt.title("Change in the Yearly Total Number of Sexual Offence Cases for the Northern Cape")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[35,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Rape Cases for North West")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[36,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Sexual Assault Cases for North West")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[37,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Attempted Sexual Offence Cases for North West")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()

df_yProvSo.iloc[38,1:11].plot(kind = "line")
plt.title("Change in the Yearly Number of Contact Sexual Offence Cases for North West")
plt.xlabel('Date')
plt.ylabel("Number of Cases")
plt.xticks(rotation = 90)
plt.show()


# In[40]:


#comparing sandton and tembisa
df_ySandton.iloc[0,1:11].plot(kind = "line")
df_yTembisa.iloc[0,1:11].plot(kind = "line", color = "red")
plt.title("Change in the Yearly Number of Rape Cases For Sandton and Tembisa in Gauteng")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_ySandton.iloc[1,1:11].plot(kind = "line")
df_yTembisa.iloc[1,1:11].plot(kind = "line", color = "red")
plt.title("Change in the Yearly Number of Sexual Assault Cases For Sandton and Tembisa in Gauteng")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_ySandton.iloc[2,1:11].plot(kind = "line")
df_yTembisa.iloc[2,1:11].plot(kind = "line", color = "red")
plt.title("Change in the Yearly Number of Attempted Sexual Offence Cases For Sandton and Tembisa in Gauteng")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_ySandton.iloc[3,1:11].plot(kind = "line")
df_yTembisa.iloc[3,1:11].plot(kind = "line", color = "red")
plt.title("Change in the Yearly Number of Contact Sexual Offence Cases For Sandton and Tembisa in Gauteng")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()

df_ySandton.iloc[4,1:11].plot(kind = "line")
df_yTembisa.iloc[4,1:11].plot(kind = "line", color = "red")
plt.title("Change in the Yearly Total Number of Sexual Offence Cases For Sandton and Tembisa in Gauteng")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.xticks(rotation = 90)
plt.legend(["Sandton", "Tembisa"])
plt.show()


# In[ ]:




