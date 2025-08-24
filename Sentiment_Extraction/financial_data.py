import yfinance as yf
import pandas as pd

#Collects daily stock data from yfinance API and adds a 'quarter' column in order to make it easier for merging with quarterly sentiment
def fetch_daily_financial_data(ticker, start_date, end_date):

    df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
    df = df.reset_index()
    df['quarter'] = pd.PeriodIndex(df['Date'], freq='Q-MAR').astype(str)
    return df


