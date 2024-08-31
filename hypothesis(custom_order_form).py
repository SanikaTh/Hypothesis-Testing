# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:24:44 2024

@author: HP
"""
'''
Telecall uses 4 centers around the globe to process customer order forms. 
They audit a certain % of the customer order forms. Any error in order form 
renders it defective and must be reworked before processing. The manager wants 
to check whether the defective % varies by center. Please analyze the data at 5% 
significance level and help the manager draw appropriate inferences 
File: Customer OrderForm.csv

Business Objectives :- To determine if the defective percentage varies by center and draw 
appropriate inferences

Business Constraints:
Perform the analysis at a 5% significance level.
Ensure the analysis is statistically interpretable.

Minimize :- minimize the defective percentage across all centers. If there are significant
differences among the centers, identifying the center with the lowest defective percentage
can help in understanding best practices.
 
Miximze:-To maximize efficiency and effectiveness in processing customer order forms
'''




import pandas as pd
import numpy as np
import scipy
from scipy import stats
from scipy.stats import chi2_contingency


# Load the data from the CSV file
data = pd.read_csv("D:/Documents/Datasets/customorderform.csv")
data
'''
 Phillippines   Indonesia       Malta       India
0     Error Free  Error Free   Defective  Error Free
1     Error Free  Error Free  Error Free   Defective
2     Error Free   Defective   Defective  Error Free
3     Error Free  Error Free  Error Free  Error Free
4     Error Free  Error Free   Defective  Error Free
..           ...         ...         ...         ...
295   Error Free  Error Free  Error Free  Error Free
296   Error Free  Error Free  Error Free  Error Free
297   Error Free  Error Free   Defective  Error Free
298   Error Free  Error Free  Error Free  Error Free
299   Error Free   Defective   Defective  Error Free

'''
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 300 entries, 0 to 299
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype 
---  ------        --------------  ----- 
 0   Phillippines  300 non-null    object
 1   Indonesia     300 non-null    object
 2   Malta         300 non-null    object
 3   India         300 non-null    object
dtypes: object(4)
memory usage: 9.5+ KB


'''
# Display the first few rows of the data to understand its structure
print(data.head())

data.Phillippines.value_counts()
data.Indonesia.value_counts()
data.Malta.value_counts()
data.India.value_counts()

# Make a contingency table
obs=np.array([[271,267,269,280],[29,33,31,20]])
obs
# Chi2 contengency independence test
chi_sq=scipy.stats.chi2_contingency(obs)
chi_sq

# Perform chi-square test for independence
crosstab = pd.crosstab(index=data['Phillippines'], columns=data['Indonesia'])

# Print the contingency table
print(crosstab)

# Perform chi-square test for independence
chi2, p_value, _, _ = chi2_contingency(crosstab)
# Print the chi-square test statistic and p-value
print("Chi-square test statistic:", chi_sq)
print(p_value)
# Compare p-value to significance level (alpha = 0.05)
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant relationship between center and defective percentage.")
else:
    print("Fail to reject the null hypothesis: There is no significant relationship between center and defective percentage.")

############################################################

