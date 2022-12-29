import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

data = pd.read_csv('C:/Users/Singhanart/Desktop/Weather_Udacity/venv/results.csv')
df =  pd.DataFrame(data)
avg_tempbkk = df.iloc[:, 2]
avg_tempGlobal = df.iloc[:,1]



def movingaverage (avg,window,count,maArr):
    for i in avg:
        startPos = count - window
        ma = np.mean((avg[startPos:count]))
        maArr.append(ma)
        count += 1
    return maArr

maArrBkk =[]
maArrGlobal =[]
window = 10

finalBkkMa = movingaverage(avg_tempbkk,window,1,maArrBkk)
finalGlobalMa =movingaverage(avg_tempGlobal,window,1,maArrGlobal)

df['BKK_ma_temp'] = finalBkkMa
df['Global_ma_temp'] = finalGlobalMa


plt.plot(df['year'], df['BKK_ma_temp'], color='red', label = "Bangkok")
plt.plot(df['year'], df['Global_ma_temp'], color='blue', label = "Global")
plt.title('Year vs Moving Average Temperature Comparision(Bangkok and Global)', fontsize=8)
plt.xlabel('Year', fontsize=8)
plt.ylabel('Moving Average Temperature (°C)', fontsize=8)
plt.grid(True)
plt.legend()
plt.show()

plt.plot(df['year'], df['BKK_ma_temp'], color='red')
plt.title('Year vs Moving Average Temperature(Bangkok)', fontsize=8)
plt.xlabel('Year', fontsize=8)
plt.ylabel('Moving Average Temperature (°C)', fontsize=8)
plt.grid(True)
plt.show()

plt.plot(df['year'], df['Global_ma_temp'], color='blue')
plt.title('Year vs Moving Average Temperature(Global)', fontsize=8)
plt.xlabel('Year', fontsize=8)
plt.ylabel('Moving Average Temperature (°C)', fontsize=8)
plt.grid(True)
plt.show()