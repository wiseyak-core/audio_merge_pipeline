import json

# Load words from JSON files
with open('/home/bumblebee/wiseyak_backup/aakriti/TTS/census_sheet.json', 'r', encoding='utf-8') as freq_file:
    frequent_words = json.load(freq_file)["word_frequencies"]

with open('/home/bumblebee/wiseyak_backup/aakriti/TTS/pronunciations.json', 'r', encoding='utf-8') as pronun_file:
    pronunciations = json.load(pronun_file)

# Extract incorrect words from the pronunciations.json with id 2
incorrect_words = pronunciations[3]["words"].keys()

# Extract correct words from frequent_words
correct_words = {}
for word, frequency in frequent_words.items():
    if word not in incorrect_words:
        correct_words[word] = frequency

# Save correct words and their frequency to a new JSON file
with open('/home/bumblebee/wiseyak_backup/aakriti/TTS/census_correct_words.json', 'w', encoding='utf-8') as correct_file:
    json.dump(correct_words, correct_file, indent=4, ensure_ascii=False)

print("Correct words have been successfully saved to correct_words.json")
