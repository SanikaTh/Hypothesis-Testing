# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:12:47 2024

@author: HP
"""
'''
A hospital wants to determine whether there is any difference in the average
 Turn Around Time (TAT) of reports of the laboratories on their preferred list.
 They collected a random sample and recorded TAT for reports of 4 laboratories.
 TAT is defined as sample collected to report dispatch

Business Objectives -The primary objective is to ensure that the hospitals receive reports from laboratories
on their preferred list within a reasonable turnaround time (TAT). Analyzing the TAT helps in assessing the 
quality of service provided by these laboratories.

Business Contraints -Perform hypothesis testing to determine if there is a significant difference in the 
average TAT among the laboratories. This analysis should be conducted at an appropriate significance level 
to ensure the results are statistically meaningful.

Minimize - to minimize the average TAT for reports from laboratories.
Maximize -Maximizing service quality involves ensuring that laboratories on the preferred list.
'''

import pandas as pd
import numpy as np
import scipy
from scipy import stats

# Read TAT data from CSV file
tat_data = pd.read_csv("D:/Documents/Datasets/Cutlets.csv")

tat_data.shape
#(35,2)

print(tat_data.head())
'''
Unit A  Unit B
0  6.8090  6.7703
1  6.4376  7.5093
2  6.9157  6.7300
3  7.3012  6.7878
4  7.4488  7.1522
'''

tat_data.tail()

'''
    Unit A  Unit B
30  6.7794  7.0992
31  7.2783  7.1180
32  7.1561  6.6965
33  7.3943  6.5780
34  6.9405  7.3875'''

tat_data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 35 entries, 0 to 34
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Unit A  35 non-null     float64
 1   Unit B  35 non-null     float64
dtypes: float64(2)
memory usage: 692.0 bytes
'''

tat_data.describe()

'''
Unit A     Unit B
count  35.000000  35.000000
mean    7.019091   6.964297
std     0.288408   0.343401
min     6.437600   6.038000
25%     6.831500   6.753600
50%     6.943800   6.939900
75%     7.280550   7.195000
max     7.516900   7.545900
'''

tat_data.isnull().sum()
'''
Unit A    0
Unit B    0
dtype: int64
'''
tat_data.rename(columns={"Unit A":"Unit_A"})
tat_data.rename(columns={"Unit B":"Unit_B"})
tat_data.columns="Unit_A","Unit_B"

from sklearn.impute import SimpleImputer
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')

tat_data['Unit_A']=pd.DataFrame(mean_imputer.fit_transform(tat_data[['Unit_A']]))
tat_data.Unit_A.isna().sum()
tat_data['Unit_B']=pd.DataFrame(mean_imputer.fit_transform(tat_data[['Unit_B']]))
tat_data.Unit_A.isna().sum()

#let us check the normality of two samples
#H0=data is normal
#H1=data is not normal
print(stats.shapiro(tat_data.Unit_A))
#Data is noram;
print(stats.shapiro(tat_data.Unit_B))
#data is not normal
#apply Mann-Whitney Test
#H0=Diameters of cutlets are same
#H1=Diameters of cutlets are different 
scipy.stats.mannwhitneyu(tat_data.Unit_A,tat_data.Unit_B)
#pvalue=0.1790>0.05,p is high null fly,H0 is true
#Diameter of cutlets are same
#############################################
