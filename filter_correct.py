import json
import os

# Define file paths
pronunciations_path = "/home/bumblebee/wiseyak_backup/aakriti/TTS/pronunciations.json"
merged_sentences_path = "/home/bumblebee/wiseyak_backup/aakriti/TTS/chatGPT_global/chat_gpt_sentences.json"
output_path = "/home/bumblebee/wiseyak_backup/aakriti/TTS/chatGPT_global/GPT_global.json"

# Load the pronunciations JSON
def load_pronunciations(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
    # Extract the "words" for the entry with "id": 1
    id_1_entry = next((entry for entry in data if entry.get("id") == 1), None)
    if id_1_entry:
        return id_1_entry.get("words", {})
    raise ValueError("No valid entry with id=1 found in the pronunciations.json file.")

# Load the merged sentences JSON
def load_sentences(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

# Process sentences to generate the required structure
def process_sentences(sentences, words_map):
    processed_data = []
    for idx, (name, text) in enumerate(sentences.items(), start=1):
        audio_path = f"/home/bumblebee/wiseyak_backup/aakriti/TTS/chatGPT_global/GPT_global_audio/{name}"
        corrected_text = text
        if text:
            for word, pronunciation in words_map.items():
                corrected_text = corrected_text.replace(word, pronunciation)
        # Set correct_text to the original text if no replacements were made, and text to None
        if corrected_text == text:
            processed_data.append({
                "id": idx,
                "name": name,
                "file_path": merged_sentences_path,
                "audio_path": audio_path,
                "correct_text": text,
                "text": None
            })
        else:
            processed_data.append({
                "id": idx,
                "name": name,
                "file_path": merged_sentences_path,
                "audio_path": audio_path,
                "correct_text": corrected_text,
                "text": text
            })
    return processed_data

# Save updated sentences to a new JSON file
def save_updated_sentences(filepath, updated_data):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(updated_data, file, ensure_ascii=False, indent=4)

# Main function
def main():
    if not os.path.exists(pronunciations_path):
        print(f"Pronunciations file not found: {pronunciations_path}")
        return

    if not os.path.exists(merged_sentences_path):
        print(f"Merged sentences file not found: {merged_sentences_path}")
        return

    try:
        words_map = load_pronunciations(pronunciations_path)
        sentences = load_sentences(merged_sentences_path)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return

    processed_data = process_sentences(sentences, words_map)

    try:
        save_updated_sentences(output_path, processed_data)
        print(f"Processed data saved to: {output_path}")
    except Exception as e:
        print(f"Error saving JSON file: {e}")

if __name__ == "__main__":
    main()
