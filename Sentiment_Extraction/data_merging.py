import pandas as pd

#This function adds a 'report_sentiment' column to daily_df after mapping its 'quarter' to quarterly_map

def merge_report_sentiment(daily_df, quarterly_map):
    daily_df['report_sentiment'] = daily_df['quarter'].map(quarterly_map)
    return daily_df

def save_dataframe_to_csv(df, path):
    df.to_csv(path, index=False)


