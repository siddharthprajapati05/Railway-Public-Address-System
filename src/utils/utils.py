import pandas as pd
import json
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon for sentiment analysis (runs once)
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

def load_csv(file_path):
    return pd.read_csv(file_path)

def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def load_text(file_path):
    with open(file_path, "r") as f:
        return f.read()

def save_csv(df, file_path):
    df.to_csv(file_path, index=False)

def save_model(model, file_path):
    with open(file_path, "wb") as f:
        pickle.dump(model, f)

def load_model(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)

def get_sentiment(text):
    # Returns compound sentiment score (-1 to 1)
    scores = sid.polarity_scores(text)
    return scores["compound"]

# Connection: Used by preprocess.py, classifier.py, and main.py for file I/O and sentiment analysis