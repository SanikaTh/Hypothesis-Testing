# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:26:53 2024

@author: HP
"""

'''
Analyze the data and determine whether there is any difference in average TAT among
 the different laboratories at 5% significance level. 
File: LabTAT.csv 
 
Business Objectives:-  the primary objective could be to minimize the average TAT across all laboratories.
Shorter TAT can lead to improved customer satisfaction and operational efficiency.

Business Constraints :- 
Perform the analysis at a 5% significance level to ensure statistical confidence.
Ensure the analysis is statistically valid and interpretable
'''

import pandas as pd
from scipy import stats
import scipy
from scipy.stats import chi2_contingency

# Load the data from LabTAT.csv file
data = pd.read_csv("D:/Documents/Datasets/lab_tat_updated.csv")
data

''' Laboratory_1  Laboratory_2  Laboratory_3  Laboratory_4
0          185.35        165.53        176.70        166.13
1          170.49        185.91        198.45        160.79
2          192.77        194.92        201.23        185.18
3          177.33        183.00        199.61        176.42
4          193.41        169.57        204.63        152.60
..            ...           ...           ...           ...
115        160.25        170.66        193.80        172.68
116        176.08        183.98        215.25        177.64
117        202.48        174.54        211.22        170.27
118        182.40        197.18        194.52        150.87
119        182.09        215.17        221.49        162.21

[120 rows x 4 columns]'''

data.shape
#(120, 4)

# print first few rows

print("First few rows of the dataset:")
print(data.head())
'''
Laboratory_1  Laboratory_2  Laboratory_3  Laboratory_4
0        185.35        165.53        176.70        166.13
1        170.49        185.91        198.45        160.79
2        192.77        194.92        201.23        185.18
3        177.33        183.00        199.61        176.42
4        193.41        169.57        204.63        152.60

'''
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 120 entries, 0 to 119
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Laboratory_1  120 non-null    float64
 1   Laboratory_2  120 non-null    float64
 2   Laboratory_3  120 non-null    float64
 3   Laboratory_4  120 non-null    float64
dtypes: float64(4)
memory usage: 3.9 KB
'''
data.describe()
'''
Laboratory_1  Laboratory_2  Laboratory_3  Laboratory_4
count    120.000000    120.000000    120.000000     120.00000
mean     178.257333    178.902917    200.210167     163.68275
std       13.919668     14.957114     15.794801      15.08508
min      140.250000    140.550000    170.580000     124.06000
25%      170.267500    168.025000    190.182500     154.05000
50%      179.055000    178.870000    198.610000     164.42500
75%      187.222500    189.112500    211.197500     172.88250
max      216.390000    217.860000    238.700000     205.18000
'''

data.columns="Laboratory_1","Laboratory_2","Laboratory_3","Laboratory_4"
data.head()
data.isna().sum()

stats.shapiro(data.Laboratory_1)
#pvalue=0.4231 >0.05 hence data is normal
stats.shapiro(data.Laboratory_2)
#pvalue=0.8637 >0.05 hence data is normal
stats.shapiro(data.Laboratory_3)
#pvalue=0.0654 >0.05 hence data is normal
stats.shapiro(data.Laboratory_4)

scipy.stats.levene(data.Laboratory_1,data.Laboratory_2,data.Laboratory_3,data.Laboratory_4)
#pvalue=0.3810>0.05 hence p high null fly,there is equal variance
#H0:All the labs are having equal TAT
#H1:At least one is having different TAT

F,pval=stats.f_oneway(data.Laboratory_1,data.Laboratory_2,data.Laboratory_3,data.Laboratory_4)
pval
#2.143740909435053e-58<0.05,p low null go,H1 is true,at least one
#lab has got different TAT

#################################################################################
