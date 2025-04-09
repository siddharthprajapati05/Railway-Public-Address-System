import os
from gtts import gTTS

def generate_announcement(train_no, processed_data):
    try:
        train_no = int(train_no)
    except ValueError:
        return f"Invalid train number: {train_no}. Please enter a valid number."

    train_data = processed_data[processed_data["train_no"] == train_no]
    if train_data.empty:
        return f"Train {train_no} not found. Please try again."

    row = train_data.iloc[0]
    destination = row["destination"]
    delay = row["delay_mins"]
    reason = row["reason"]
    sentiment = row["sentiment"]

    if delay == 0 and not reason:
        announcement_text = (
            f"Announcement for Train {train_no}: "
            f"Train {train_no} to {destination} is on time. "
            f"Have a pleasant journey!"
        )
    else:
        announcement_text = (
            f"Announcement for Train {train_no}: "
            f"Train {train_no} to {destination} is delayed by {delay} minutes due to {reason}. "
            f"We apologize for the inconvenience."
        )

    tts = gTTS(announcement_text, lang="en")
    audio_file = f"announcement_{train_no}.mp3"
    tts.save(audio_file)
    os.system(f"open {audio_file}")  # macOS; use 'start' for Windows, 'xdg-open' for Linux
    return announcement_text