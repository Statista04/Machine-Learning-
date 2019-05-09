from pandas_datareader import data
#name the company and source
symbol= 'RBC'
data_source= 'yahoo'
start_date= '2019-01-01'
end_date= '2019-01-04'

df= data.DataReader(symbol, data_source, start_date, end_date)
#print(df.head())
df.to_csv('RBC_stocks.csv')
