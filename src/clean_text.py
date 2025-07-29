"""
clean_text.py

Text cleaning utilities for tweets.
"""

import re
import string
import pandas as pd

# clean tweets
def clean_tweet(text):
    """
    Cleans tweet text by removing mentions, hashtags, URLs, emojis, and punctuation.
    """
    text = re.sub(r"@\w+", "", text)  # remove @mentions
    text = re.sub(r"#\w+", "", text)  # remove hashtags
    text = re.sub(r"http\S+|www\S+", "", text)  # remove URLs
    text = text.encode("ascii", "ignore").decode("utf-8")  # remove emojis
    text = text.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
    text = text.lower().strip()  # lowercase and strip whitespace
    return text

def clean_text_column(df, column):
    """
    Applies clean_tweet to a specified column in the DataFrame.
    """
    df[column] = df[column].astype(str).apply(clean_tweet)
    return df
