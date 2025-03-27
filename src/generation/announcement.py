import os
from gtts import gTTS

def generate_announcement(train_no, processed_data):
    # Convert train_no to integer to match processed_data
    try:
        train_no = int(train_no)
    except ValueError:
        print(f"Invalid train number: {train_no}. Please enter a valid number.")
        return

    # Check if train exists in processed data
    train_data = processed_data[processed_data["train_no"] == train_no]
    if train_data.empty:
        print(f"Train {train_no} not found. Please try again.")
        return

    # Extract details
    row = train_data.iloc[0]
    destination = row["destination"]
    delay = row["delay_mins"]
    reason = row["reason"]
    sentiment = row["sentiment"]

    # Generate announcement text based on delay and reason
    if delay == 0 and not reason:  # On-time train
        announcement_text = (
            f"Announcement for Train number {train_no}: "
            f"Train number {train_no} to {destination} is on time. "
            f"Have a pleasant journey!"
        )
    else:  # Delayed train
        announcement_text = (
            f"Announcement for Train number {train_no}: "
            f"Train number {train_no} to {destination} is delayed by {delay} minutes due to {reason}. "
            f"We apologize for the inconvenience."
        )
    
    print(announcement_text)

    # Generate voice message
    tts = gTTS(announcement_text, lang="en")
    audio_file = f"announcement_{train_no}.mp3"
    tts.save(audio_file)
    os.system(f"open {audio_file}")  # Play the audio file on macOS