"""
sentiment_analysis.py

Performs sentiment analysis using TextBlob.
"""

from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
    """
    Returns polarity score from TextBlob sentiment analysis.
    """
    return TextBlob(text).sentiment.polarity

def apply_sentiment(df, column):
    """
    Applies sentiment analysis to a specified text column.
    Adds a new 'sentiment' column with polarity scores.
    """
    df["sentiment"] = df[column].astype(str).apply(analyze_sentiment)
    return df
