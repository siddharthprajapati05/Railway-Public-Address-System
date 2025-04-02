import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from src.preprocessing.preprocess import preprocess_data
from src.generation.announcement import generate_announcement   

def run_system():
    # Define file paths
    schedule_file = "data/raw/train_schedule.csv"
    delay_file = "data/raw/delay_logs.json"
    feedback_file = "data/raw/passenger_feedback.txt"
    
    # Preprocess data
    try:
        processed_data = preprocess_data(schedule_file, delay_file, feedback_file)
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return

    # Debug output
    print("Processed Data Train Numbers:", processed_data["train_no"].tolist())
    print("Processed Data Head:\n", processed_data.head())

    # Start the announcement system
    print("Railway Public Address System ready. Enter a train number (e.g., 123) or 'exit' to quit.")
    while True:
        train_no = input("Enter train number: ").strip()
        if train_no.lower() == "exit":
            print("Exiting system.")
            break
        if not train_no:
            print("Please enter a valid train number.")
            continue
        generate_announcement(train_no, processed_data)

if __name__ == "__main__":
    run_system()