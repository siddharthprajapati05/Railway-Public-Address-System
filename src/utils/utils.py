import pandas as pd
import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Set NLTK data path to local directory
nltk.data.path.append('/Users/siddharthprajapati/nltk_data')  # Your path
sid = SentimentIntensityAnalyzer()  # Initialize without downloading

def load_csv(file_path):
    return pd.read_csv(file_path)

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def load_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def save_csv(df, file_path):
    df.to_csv(file_path, index=False)

def get_sentiment(text):
    return sid.polarity_scores(text)["compound"]