#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 20:14:12 2022

@author: ibrahimbashir
"""

import pandas as pd

data = pd.read_csv('transaction.csv')

#we need to add a comma separator
data = pd.read_csv('transaction.csv', sep=';')

#make sure to always navigate to my working directory 
#whenever i re-open spyder

#summary of the data
data.info()

#calculations

#defining variables
cost_per_item = 11.73
selling_price_per_item = 21.11
num_of_items_purchased = 6

#math operations on Tableau
profit_per_item = selling_price_per_item - cost_per_item

profit_per_transaction = num_of_items_purchased * profit_per_item

cost_per_transaction = cost_per_item * num_of_items_purchased

selling_price_per_transaction = selling_price_per_item * num_of_items_purchased



#cost_per_transaction = cost_per_item * num_of_items_purchased
cost_per_item = data['CostPerItem']
num_of_items_purchased = data['NumberOfItemsPurchased']
cost_per_transaction = cost_per_item * num_of_items_purchased

#add new column to dataframe
data['CostPerTransaction'] = cost_per_transaction
#another way of doing the line above
#data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#sales per transaction
data['SalesByTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit
data['ProfitPerTransaction'] = data['SalesByTransaction'] - data['CostPerTransaction']

#markup = sale - cost / cost
data['Markup'] = data['SalesByTransaction'] - data['CostPerTransaction'] / data['CostPerTransaction']


#round markup column to 2 decimal places
data['Markup'] = round(data['Markup'], 2)

#combine multiple columns into one
#my_date = data['Day']+'/'+data['Month']+'/'+data['Year']
#data['Date'] = my_date

#change column data type
day = data['Day'].astype(str)
print(day+'/')

year = data['Year'].astype(str)
print(year+'/')

month = data['Month'].astype(str)
print(month+'/')

my_date = day+'/'+month+'/'+year

data['Date'] = my_date

#using iloc to view specific columns/rows
#data.iloc[0] #views the row with index 0
five = data.iloc[0:5] #views first 5 rows

data.iloc[:,5]

data.info()


#splitting
split_col = data['ClientKeywords'].str.split(',' , expand=True)

#adding new columns from split of client key words
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]


#using replace function
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')


#using the lower function
data['ItemDescription'] = data['ItemDescription'].str.lower()


#how to merge files bringing in a new dataset
#read the file with pandas dataframe

#seasons = pd.read_csv('/Users/ibrahimbashir/Documents/python+Tableau bootcamp/3.4 value_inc_seasons.csv', sep=';')

#merge_df = pd.merge(df_old, df_new, on = 'key')
#data = pd.merge(data, seasons, on = 'Month')


#dropping columns
data = data.drop('ClientKeywords', axis=1)
data = data.drop(['Day','Month', 'Year'], axis=1)



#export into csv
data.to_csv('ValueInc_Cleaned.csv', index = False)

