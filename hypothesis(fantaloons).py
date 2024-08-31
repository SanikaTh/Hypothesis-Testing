# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:37:27 2024

@author: HP
"""

'''
Fantaloons Sales managers commented that % of males versus females walking into 
the store differ based on day of the week. Analyze the data and determine whether
 there is evidence at 5 % significance level to support this hypothesis. 
File: Fantaloons.csv

Business Objectives -Determine if there is a significant difference in the percentage of males versus females
visiting the store based on the day of the week. This understanding can help in optimizing tailoring marketing strategies.

Business Constraints :-Perform hypothesis testing at a 5% significance level to ensure the results are statistically
valid and reliable.
Minimize -  to minimize any differences in the percentage of males versus females walking into the store across
different days of the week. 
Maximize - to maximize operational efficiency
'''

import pandas as pd
from scipy.stats import chi2_contingency

# Load the data from the CSV file
data = pd.read_csv("D:/Documents/Datasets/Fantaloons.csv")

# Display the first few rows of the data to understand its structure
print(data.head())
'''
Weekdays Weekend
0     Male  Female
1   Female    Male
2   Female    Male
3     Male  Female
4   Female  Female
'''
data.columns
#Index(['Weekdays', 'Weekend'], dtype='object')

data.describe()
'''
Weekdays Weekend
count       400     400
unique        2       2
top      Female  Female
freq        287     233
'''
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 400 entries, 0 to 399
Data columns (total 2 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   Weekdays  400 non-null    object
 1   Weekend   400 non-null    object
dtypes: object(2)
memory usage: 6.4+ KB
'''
# Perform chi-square test for independence
crosstab = pd.crosstab(index=data['Weekdays'], columns=data['Weekend'])

# Print the contingency table
print(crosstab)

# Perform chi-square test for independence
chi2, p_value, _, _ = chi2_contingency(crosstab)

# Print the chi-square test statistic and p-value
print("Chi-square test statistic:", chi2)
print("P-value:", p_value)

# Compare p-value to significance level (alpha = 0.05)
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant relationship between gender and day of the week.")
else:
    print("Fail to reject the null hypothesis: There is no significant relationship between gender and day of the week.")
