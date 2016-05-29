## pandas input output (io)

import pandas as pd

df = pd.read_csv('/Users/Gavin/Desktop/py/pyProg/DataAnalysis/ZILL-Z77006_MLP (1).csv')
df.set_index('Date', inplace = True)

print(df.head())

df.to_csv('newcsv2.csv')

df = pd.read_csv('/Users/Gavin/Desktop/py/pyProg/DataAnalysis/newcsv2.csv')
print(df.head())

##set index as you read csv in
df = pd.read_csv('/Users/Gavin/Desktop/py/pyProg/DataAnalysis/newcsv2.csv', index_col=0)
print(df.head())

##rename columns
df.columns = ['Austin_HPI']
print(df.head())

df.to_csv('newcsv3.csv')

##safe to file without headers
df.to_csv('newcsv4.csv', header=False)

##read csv in that doesn't have any headers
df = pd.read_csv('newcsv4.csv', names = ['Date', 'Austin_HPI'], index_col=0)
print(df.head())

df.to_html('example.html')

df = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'])

df.rename(columns={'Austin_HPI': '77006_HPI'}, inplace=True)
print(df.head())
