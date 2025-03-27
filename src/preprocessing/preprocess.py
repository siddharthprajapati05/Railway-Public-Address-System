import pandas as pd
from src.utils.utils import load_csv, load_json, load_text, save_csv, get_sentiment

def preprocess_data(schedule_file, delay_file, feedback_file):
    # Load raw data
    schedule_df = load_csv(schedule_file)
    delay_data = load_json(delay_file)
    feedback_text = load_text(feedback_file)

    # Convert train_no to integer in both DataFrames
    schedule_df["train_no"] = schedule_df["train_no"].astype(int)
    delay_df = pd.DataFrame(delay_data)
    delay_df["train_no"] = delay_df["train_no"].astype(int)

    # Merge schedule and delay data
    merged_data = schedule_df.merge(delay_df, on="train_no", how="left")

    # Parse feedback and match to trains
    feedback_lines = feedback_text.split("\n")
    feedback_dict = {}
    for line in feedback_lines:
        if "Train" in line:
            train_no = line.split("Train")[1].split()[0]  # Extract train_no
            feedback_dict[train_no] = line.strip()

    # Add feedback and sentiment columns
    merged_data["feedback"] = merged_data["train_no"].apply(
        lambda x: feedback_dict.get(str(x), "No feedback available")
    )
    merged_data["sentiment"] = merged_data["feedback"].apply(get_sentiment)

    # Fill NaN delays with 0 and empty reasons with ""
    merged_data["delay_mins"] = merged_data["delay_mins"].fillna(0)
    merged_data["reason"] = merged_data["reason"].fillna("")

    # Save processed data
    output_file = "data/processed/processed_data.csv"
    save_csv(merged_data, output_file)
    return merged_data

if __name__ == "__main__":
    # Use paths relative to project root
    schedule_file = "data/raw/train_schedule.csv"
    delay_file = "data/raw/delay_logs.json"
    feedback_file = "data/raw/passenger_feedback.txt"
    preprocess_data(schedule_file, delay_file, feedback_file)