#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 18:00:35 2022

@author: ibrahimbashir
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = pd.read_excel('articles.xlsx')

data.describe()

data.info()

data.source_id.value_counts()

#counting the number of articles per source using groupby
data.groupby(['source_id'])['article_id'].count()


#no. of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()


#dropping a column
data = data.drop('engagement_comment_plugin_count', axis = 1)


#creating a keyword flag
keyword = 'crash'

length = len(data)
keyword_flag = []
#a forloop to isolate each title row
for x in range(0, length):
    heading = data['title'][x]
    if keyword in heading:
        flag  = 1
    else:
        flag = 0
        
    keyword_flag.append(flag)
    
    
#creating a function
def keyword_flag(keyword):
    length = len(data)
    keyword_flag = []

    for x in range(0, length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag  = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag = keyword_flag('crash')

#creating a new column in dataframe
data['keyword_flag'] = pd.Series(keywordflag)
    
    
#SentimentIntensityAnalyzer 
sent_int = SentimentIntensityAnalyzer()
text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#using a forloop to extract sentiments for every title
title_neg_sentiment = []
title_neu_sentiment = []
title_pos_sentiment = []
length = len(data)

for x in range(0, length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_neu_sentiment.append(neu)
    title_pos_sentiment.append(pos)
    
    
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)


data['title_neg_sentiment'] = title_neg_sentiment
data['title_neu_sentiment'] = title_neu_sentiment
data['title_pos_sentiment'] = title_pos_sentiment


data.to_excel('blogme_cleaned.xlsx',  sheet_name = 'blogmedata', index = False)