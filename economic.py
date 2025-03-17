#!/usr/bin/python3
"""\
This Script parses the economic data excel file and outputs a 
correlation coefficient for the borrowing rate and inflation rate.
A projection of the inflation rate will be provided based on different 
borrowing rate yields. 

Usage: python3 economic.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sunkit_image.time_lag import cross_correlation, get_lags, time_lag
from astropy import units as u

df = pd.DataFrame(pd.read_excel("economic-data.xlsx"))

# Clean columns and rows
df.columns = [df.iloc[10, 0], df.iloc[10, 1], df.iloc[10, 2], df.iloc[10, 3], df.iloc[10, 4], 0, 0]
df = df.iloc[11:, :5]

print(f'Inflation Average: {df.iloc[:,1].mean()*100:.2f}%')
print(f'Overnight Rate Average: {df.iloc[:,2].mean()*100:.2f}% stdev: {df.iloc[:,2].std()*100:.2f}')
print(f'1yr Spot Average: {df.iloc[:,3].mean()*100:.2f}%')
print(f'10yr Spot Average: {df.iloc[:,4].mean()*100:.2f}%')

print(df.corr())

plt.plot(df['Year'], df['Inflation'], label="Inflation")
plt.plot(df['Year'], df['Government of Tarrodan Overnight Rate'], label="Government of Tarrodan Overnight Rate")
plt.xlabel("Year")
plt.ylabel("%")
plt.legend()
plt.show()

year = df['Year'].values * u.year
lags = get_lags(year)
cc = cross_correlation(df['Government of Tarrodan Overnight Rate'], df['Inflation'], lags)
plt.plot(lags, cc, color='green')
plt.xlabel("Lag [Year]")
plt.ylabel("Cross-correlation, Inflation-BorrowingRate")
plt.show()

tl = time_lag(df['Government of Tarrodan Overnight Rate'], df['Inflation'], year)
print('Borrowing Rate -> Inflation: ', tl)