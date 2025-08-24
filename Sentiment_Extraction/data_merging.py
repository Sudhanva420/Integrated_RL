import pandas as pd
#maps the quarterly sentiment onto each and every row in the same quarter 
def merge_report_sentiment(daily_df, quarterly_map):
    daily_df['report_sentiment'] = daily_df['quarter'].map(quarterly_map)
    return daily_df

def save_dataframe_to_csv(df, path):
    df.to_csv(path, index=False)



