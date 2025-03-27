import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from src.preprocessing.preprocess import preprocess_data
from src.generation.announcement import generate_announcement

def run_system():
    schedule_file = "data/raw/train_schedule.csv"
    delay_file = "data/raw/delay_logs.json"
    feedback_file = "data/raw/passenger_feedback.txt"
    processed_data = preprocess_data(schedule_file, delay_file, feedback_file)
    print("Processed Data Train Numbers:", processed_data["train_no"].tolist())
    print("Processed Data Head:\n", processed_data.head())

    print("Railway Public Address System ready. Enter a train number (e.g., 123) or 'exit' to quit.")
    while True:
        train_no = input("Enter train number: ")
        if train_no.lower() == "exit":
            print("Exiting system.")
            break
        generate_announcement(train_no, processed_data)

if __name__ == "__main__":
    run_system()