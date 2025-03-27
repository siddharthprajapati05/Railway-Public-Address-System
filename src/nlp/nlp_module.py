import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(delay_text, feedback_text):
    # Combine delay and feedback for richer context
    combined_text = f"{delay_text}. {feedback_text}"
    doc = nlp(combined_text)
    
    entities = {"train_no": None, "delay": None, "reason": None}
    
    for ent in doc.ents:
        if ent.label_ == "CARDINAL" and "mins" in combined_text.lower():
            entities["delay"] = ent.text
        elif ent.text.isdigit():
            entities["train_no"] = ent.text
    
    # Extract reason from delay text
    if "due to" in delay_text.lower():
        entities["reason"] = delay_text.split("due to")[-1].strip()
    
    return entities

# Connection: Called by main.py with delay and feedback text
# If path not detected: Place this file in src/nlp/
if __name__ == "__main__":
    delay_text = "Train 123 delayed by 20 mins due to signal failure"
    feedback_text = "Train 123 is always late, terrible service!"
    print(extract_entities(delay_text, feedback_text))