import json
import csv

# Input and output file paths
json_file_path = "/home/bumblebee/wiseyak_backup/aakriti/TTS/Banking/banking_final_sentences.json"
csv_file_path = "/home/bumblebee/wiseyak_backup/aakriti/TTS/Banking/banking_final_sentences.csv"

# Read the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Define the CSV column headers
csv_columns = ["id", "name", "file_path", "audio_path", "correct_text", "text"]

# Write the data to a CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(data)

print(f"CSV file has been created at {csv_file_path}")
