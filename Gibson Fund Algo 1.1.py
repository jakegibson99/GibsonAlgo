"""
Created on Sat Aug  1 00:35:12 2020

Gibson Fund Algo v1.1

@author: Jake Gibson
"""

# Principle Value

principle = 10000

# Get Tickers


import yfinance as yf
import matplotlib as plt
import pandas as pd
import numpy as np

'''

Not currently using this part of the code. 

I need to be able to create a list of tickers and adjust the start date as a global variable

!!! Ask Cameron Pfifer if it's ok to use start and end dates as global variables

tickers = ['AAPL','TRNO',' CRM',' VYM','DEO','STZ','TSLA','AMZN','GOOG','INTC','EA']

start = "2018-7-31"
end = "2020-7-31"
# add these to the download call below

'''



# Download data on the tickers of interst
# Manually adjust the tickers in the first argument of yf.download

tickers1 = yf.download('AAPL TRNO CRM VYM DEO STZ TSLA AMZN GOOG INTC EA IEF', start = "2012-07-31", end = "2020-07-31", intervals = '1mo').pct_change(periods = 1)

annuals = tickers1.groupby(tickers1.index.dt.year)
# group data by year

fund = tickers1['Adj Close'].dropna()
# create a fund variable with the adjusted closes a percentage change from prior weekly close

# Set Weights. In this case we are using equal weights. We need to make the fund variable before because we drop
# everything except the 'Adj Close' value

n = fund.shape[1]

weight = [1 / n] * n
print(sum(weight))
# equal weighting across every postion


# Calculate Fund Expected Return
avg1 = fund.mean()
avg2 = avg1 * weight
fundavg = avg2.sum()
print(fundavg)
print(f'The funds expected annual return is {round(fundavg,6)}')
# why is my annual return so low???

fundrets = fund * 100
avg3 = fundrets.mean()
avg4 = avg3 * weight
fundpercentavg = avg4.sum()
# fund rate in percentage form
print(f'The Funds expected return is {round(fundpercentavg,4)}%')
# turn the fund returns into percentage form


# Weighted Returns
# https://www.codingfinance.com/post/2018-04-05-portfolio-returns-py/

weighted_returns = (weight * fund)
print(weighted_returns)

fund_ret = weighted_returns.sum(axis = 1)
print(fund_ret)

total_return = sum(fund_ret)
print(f'The total return over this period was {total_return*100}%')
# the above formulas give the same fund expected weighted return

fund_std = fund_ret.std()
print(fund_std)

RRR = .08
# Create a required rate of return in percentage terms
# the Required Rate of Return is currently set to 8%


# download the risk free rate. In this case, we are using the IEF ETF as a proxy until we can
# get the actual T-Note data
riskfree = fund["IEF"]
print(riskfree)

rfrpercent = riskfree.mean() * 100
# risk free rate in percentage form
print(rfrpercent)

# make sure and use fundpercentavg and rfrpercent to have sharpe in % form
sharpe = (fundpercentavg - rfrpercent) / fund_std
print(f'Portoflio Expected Return: {fundpercentavg}')
print(f'Risk Free Return {rfrpercent}')
print(f'Portoflio Standard Deviation: {fund_std}')
print(f'Portfoli Sharpe Ratio: {sharpe}')





'''

!!!     Extra code to come back to     !!!!
Use the code below if you want all data to be in percentage terms. Ie 10% = 10
rfr1 = (rrf1.dropna() * 100).mean()
# pull 5yr treasury note to use as the risk free rate times 100 to get into percentages
print(rrf)
print(f'The current risk free rate has an expected return of {rfr}')


# fund variance and covariance
cov = fundrets.cov()
cor = fundrets.corr()
# var = fundrets.var()
print(cov)
print(cor)
# use individual variances and weights to calculate the fund variance

mean = fundrets.mean()*100
exprets = (mean * weights).sum()
print(exprets)
fundmean = sum(mean) / len(mean)

sharpe = (fundmean - riskfree) / fundvar

'''


