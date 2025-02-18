#!/usr/bin/python3
"""\
This Script parses the economic data excel file and outputs a 
correlation coefficient for the borrowing rate and inflation rate.
A projection of the inflation rate will be provided based on different 
borrowing rate yields. 

Usage: python3 economic.py
"""

import pandas as pd

df = pd.DataFrame(pd.read_excel("economic-data.xlsx"))

print(df)