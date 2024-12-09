# Required imports
import requests
import json
import os
from IPython.display import Audio, display, clear_output

# API details
api_url = "http://fs.wiseyak.com:8026/xtts_text"
headers = {
    'accept': 'application/json'
}

# Load word frequencies from JSON file
word_frequencies_json_path = "/home/bumblebee/wiseyak_backup/aakriti/TTS/test.json"
with open(word_frequencies_json_path, "r", encoding="utf-8") as f:
    word_frequencies_data = json.load(f)

# Directory to save audio files
audio_save_path = "/home/bumblebee/wiseyak_backup/aakriti/TTS/audio_files"
os.makedirs(audio_save_path, exist_ok=True)

# Function to generate TTS audio for each word
def generate_tts_audio(word, word_key):
    try:
        # Sending request to the TTS API
        response = requests.post(api_url, headers=headers, data={"text": word, "language": "nepali"})
        response.raise_for_status()

        # Saving the audio file
        audio_filename = f"{word_key}.wav"
        audio_path = os.path.join(audio_save_path, audio_filename)
        with open(audio_path, "wb") as audio_file:
            audio_file.write(response.content)

        print(f"Successfully generated audio for '{word_key}': '{word}' and saved to {audio_path}")
        return audio_path
    except requests.exceptions.RequestException as e:
        print(f"Error generating audio for '{word_key}': {e}")
        return None

# Generate and save audio for each word and display it
batch_size = 250
current_batch = 0
words_processed = 0

word_items = list(word_frequencies_data["word_frequencies"].items())

# Iterate over word items in batches of 250
for word_key, frequency in word_items:
    audio_path = generate_tts_audio(word_key, word_key)
    if audio_path:
        # Display the audio in Jupyter notebook
        display(Audio(audio_path))
    
    words_processed += 1

    # Clear output every 250 words
    if words_processed >= batch_size:
        words_processed = 0
        current_batch += 1
        print(f"Completed batch {current_batch}. Clearing output to proceed...")
        clear_output(wait=True)

# Final output message when all batches are done
print("All audio files have been generated and displayed successfully.")
