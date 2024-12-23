import pandas as pd
import json

# Input CSV file path
csv_file_path = '/home/bumblebee/wiseyak_backup/aakriti/TTS/chatGPT_global/chat_gpt_cleaned.csv'
# Output JSON file path
json_file_path = '/home/bumblebee/wiseyak_backup/aakriti/TTS/chatGPT_global/chat_gpt_sentences.json'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Create a dictionary to store the sentences in the required format
sentences_dict = {}

# Iterate over the rows and add to the dictionary
for index, row in df.iterrows():
    sentence_id = f"GPT_sentences_{index + 1}"  # Generate the sentence ID
    sentence = row['sentence']  # Get the sentence
    sentences_dict[sentence_id] = sentence  # Add to the dictionary

# Write the dictionary to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(sentences_dict, json_file, ensure_ascii=False, indent=4)

print(f"JSON file created successfully at {json_file_path}.")
