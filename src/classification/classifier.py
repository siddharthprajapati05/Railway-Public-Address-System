import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from src.utils.utils import load_csv, save_model, load_model

def train_classifier(data_file):
    df = load_csv(data_file)
    X = df[["delay_mins", "sentiment"]]  # Features: delay duration and feedback sentiment
    y = df["delay_mins"].apply(lambda x: "delay" if x > 0 else "routine")  # Label
    
    clf = RandomForestClassifier(n_estimators=10)
    clf.fit(X, y)
    
    model_file = "data/models/classifier_model.pkl"
    save_model(clf, model_file)
    return clf

def classify_announcement(features):
    model_file = "data/models/classifier_model.pkl"
    clf = load_model(model_file)
    prediction = clf.predict([features])[0]
    return prediction

# Connection: train_classifier called by main.py, classify_announcement used per input
# If path not detected: Place this file in src/classification/, ensure data/models/ exists
if __name__ == "__main__":
    data_file = "../../data/processed/processed_data.csv"  # Relative to src/classification/
    train_classifier(data_file)
    sample_features = [20, -0.5]  # 20 mins delay, negative sentiment
    print(classify_announcement(sample_features))