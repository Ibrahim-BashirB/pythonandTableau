#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 19:52:36 2022

@author: ibrahimbashir
"""

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

#read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#another way to read json data
#with open('loan_data_json.json') as json_file:
    #data = json.load(json_file)
    
#transform to dataframe
loan_data = pd.DataFrame(data)

#finding unique data
loan_data.purpose.unique()

#describe the data
loan_data.describe()

#describe the data for specific column
loan_data.fico.describe()

loan_data.info()

#getting the exponent of the log annual income
income = np.exp(loan_data['log.annual.inc'])
loan_data['annual_income'] = income

#using for loop to categories the fico column
length = len(loan_data)
ficocat = []

for x in range(0, length):
    category = loan_data['fico'][x]
    try:
        if category >=300 and category <400:
            cat = 'very poor'
        elif category >=400 and category <600:
            cat = 'poor'
        elif category >=601 and category <660:
            cat = 'fair'
        elif category >=660 and category <700:
            cat = 'good'
        elif category >=700:
            cat = 'excellent'
        else:         
            cat = 'invalid'
    except:
        cat = 'error'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)

loan_data['fico.category'] = ficocat

#new column to tell if interest rate is high or low
loan_data['itr.rate.category'] = loan_data['int.rate'].apply(lambda x: 'high' if x>=0.12 else 'low')


catplot = loan_data["fico.category"].value_counts()
catplot.plot.bar()
plt.show()

purpose_count = loan_data.groupby(['purpose']).size()
purpose_count.plot.bar(color ='red', width = 0.5)

#write to csv
loan_data.to_csv('loan_data_cleaned.csv', index = True)


