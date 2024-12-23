import requests
import json
import os
import sys

# -----------------------------
# Configuration
# -----------------------------

# API details
API_URL = "http://fs.wiseyak.com:8026/xtts_text"
HEADERS = {
    'accept': 'application/json'
}

# Path to the JSON file
JSON_FILE_PATH = "/home/bumblebee/wiseyak_backup/aakriti/TTS/chatGPT_global/GPT_global.json"

# Directory to save audio files
AUDIO_SAVE_PATH = "/home/bumblebee/wiseyak_backup/aakriti/TTS/chatGPT_global/GPT_global_audio"
os.makedirs(AUDIO_SAVE_PATH, exist_ok=True)

# ID range for which to generate audio
START_ID = 1
END_ID = 2300

# -----------------------------
# Functions
# -----------------------------

def generate_tts_audio(sentence, audio_name):
    """
    Generates TTS audio for a given sentence and saves it as a .wav file.

    Args:
        sentence (str): The text to convert to speech.
        audio_name (str): The name to assign to the audio file (without extension).

    Returns:
        str or None: Path to the saved audio file if successful, else None.
    """
    try:
        # Sending request to the TTS API
        response = requests.post(API_URL, headers=HEADERS, data={"text": sentence, "language": "nepali"})
        response.raise_for_status()

        # Saving the audio file
        audio_filename = f"{audio_name}.wav"
        audio_path = os.path.join(AUDIO_SAVE_PATH, audio_filename)
        with open(audio_path, "wb") as audio_file:
            audio_file.write(response.content)

        print(f"✅ Successfully generated audio for '{audio_name}' and saved to {audio_path}")
        return audio_path
    except requests.exceptions.RequestException as e:
        print(f"❌ Error generating audio for '{audio_name}': {e}")
        return None

def load_json(json_path):
    """
    Loads JSON data from the specified file.

    Args:
        json_path (str): Path to the JSON file.

    Returns:
        list: List of JSON entries.
    """
    if not os.path.isfile(json_path):
        print(f"❌ Error: The file '{json_path}' does not exist.")
        sys.exit(1)

    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        print(f"📂 Successfully loaded JSON data from '{json_path}'. Total entries: {len(data)}")
        return data
    except json.JSONDecodeError as e:
        print(f"❌ Error decoding JSON from '{json_path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error while loading JSON: {e}")
        sys.exit(1)

def filter_entries(dataset, start_id, end_id):
    """
    Filters the dataset to include only entries with IDs between start_id and end_id (inclusive).

    Args:
        dataset (list): List of JSON entries.
        start_id (int): Starting ID.
        end_id (int): Ending ID.

    Returns:
        list: Filtered list of entries.
    """
    filtered = [entry for entry in dataset if start_id <= entry.get("id", -1) <= end_id]
    print(f"🔍 Filtered entries from ID {start_id} to {end_id}. Entries to process: {len(filtered)}")
    return filtered

# -----------------------------
# Main Execution
# -----------------------------

def main():
    # Load the JSON data
    dataset = load_json(JSON_FILE_PATH)

    # Filter entries for IDs between 90 and 168
    filtered_dataset = filter_entries(dataset, START_ID, END_ID)

    # Check if there are entries to process
    if not filtered_dataset:
        print(f"⚠️ No entries found with IDs between {START_ID} and {END_ID}. Exiting.")
        sys.exit(0)

    # Process each filtered entry
    for entry in filtered_dataset:
        entry_id = entry.get("id")
        name = entry.get("name", f"unknown_{entry_id}")
        correct_text = entry.get("correct_text", "")

        if not correct_text:
            print(f"⚠️ Entry ID {entry_id} ('{name}') has no 'correct_text'. Skipping.")
            continue

        generate_tts_audio(correct_text, name)

    print("🎉 Audio generation process completed.")

if __name__ == "__main__":
    main()
