import streamlit as st
from src.preprocessing.preprocess import preprocess_data
from src.generation.announcement import generate_announcement
import os
import sys

# Set page config
st.set_page_config(page_title="Railway Public Address System", layout="wide")

# Load processed data
@st.cache_data
def load_data():
    return preprocess_data(
        "data/raw/train_schedule.csv",
        "data/raw/delay_logs.json",
        "data/raw/passenger_feedback.txt"
    )

processed_data = load_data()

# UI
st.title("Railway Public Address System")

# Input and button at the top
col1, col2 = st.columns([3, 1])  # Layout: wider input, smaller button
with col1:
    train_no = st.text_input("Enter Train Number:", key="train_input")
with col2:
    if st.button("Generate Announcement"):
        if train_no:
            announcement_text = generate_announcement(train_no, processed_data)
            if "not found" in announcement_text or "Invalid" in announcement_text:
                st.error(announcement_text)
            elif "on time" in announcement_text:
                st.success(announcement_text)
            else:
                st.error(announcement_text)
            
            # Play audio
            audio_file = f"announcement_{train_no}.mp3"
            if os.path.exists(audio_file):
                st.audio(audio_file)
        else:
            st.warning("Please enter a train number.")

# Display announcement (if generated)
if "announcement_text" in locals():
    st.write("Last Announcement:", announcement_text)

# Train data at the bottom
st.subheader("Train Data")
st.dataframe(processed_data, use_container_width=True)

# Stop application button
if st.button("Stop Application"):
    st.write("Stopping the application...")
    # Workaround: Use os._exit() to force stop (not ideal but functional)
    os._exit(0)  # Stops the Streamlit server