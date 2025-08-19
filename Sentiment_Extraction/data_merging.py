import pandas as pd

def merge_report_sentiment(daily_df, quarterly_map):
    """
    Adds a 'report_sentiment' column to daily_df by mapping its 'quarter' to quarterly_map.
    """
    daily_df['report_sentiment'] = daily_df['quarter'].map(quarterly_map)
    return daily_df

def save_dataframe_to_csv(df, path):
    df.to_csv(path, index=False)

