import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file=input(' Enter fb_sentiment_analysis xlsx file name: ')
xl=pd.ExcelFile(file)#Read from Excel
dfs=xl.parse(xl.sheet_names[0])#Parsing Excel Sheet to Data Frame
dfs=list(dfs['Timeline'])#Removes the blank rows from the Data Frame
print(dfs)
sid=SentimentIntensityAnalyzer()
str1="am"
str2="pm"
for data in dfs:
    a=data.find(str1)
    b=data.find(str2)
    if(a==-1 or b==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])
