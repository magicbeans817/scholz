# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:24:00 2023

@author: jsuch
"""

import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel("data.xlsx")

# Display the first few rows of the DataFrame
print(df.head())

print(df)

