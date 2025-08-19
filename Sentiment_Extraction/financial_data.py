import yfinance as yf
import pandas as pd

#downloads daily stock data and adds a 'quarter' column
def fetch_daily_financial_data(ticker, start_date, end_date):

    df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
    df = df.reset_index()
    df['quarter'] = pd.PeriodIndex(df['Date'], freq='Q-MAR').astype(str)
    return df

