import pandas as pd
from src.preprocessing.preprocess import preprocess_data

def test_preprocess():
    schedule_file = "../data/raw/train_schedule.csv"  # Relative to tests/
    delay_file = "../data/raw/delay_logs.json"
    feedback_file = "../data/raw/passenger_feedback.txt"
    result = preprocess_data(schedule_file, delay_file, feedback_file)
    assert isinstance(result, pd.DataFrame)
    assert "train_no" in result.columns
    assert "sentiment" in result.columns
    print("Preprocessing test passed!")

# Connection: Tests preprocess.py
# If path not detected: Place this file in tests/, ensure data/raw/ exists
if __name__ == "__main__":
    test_preprocess()