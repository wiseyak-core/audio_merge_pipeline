import json
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def transliterate_json(input_file, output_file):
    try:
        # Load the input JSON file
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Access the "word_frequencies" dictionary
        word_frequencies = data.get("word_frequencies", {})

        # Transliterate each Nepali word to English
        transliterated_frequencies = {}
        for nepali_word in word_frequencies.keys():
            english_transliteration = transliterate(nepali_word, sanscript.DEVANAGARI, sanscript.ITRANS)
            transliterated_frequencies[nepali_word] = english_transliteration.lower().capitalize()

        # Prepare the output structure
        output_data = {"word_frequencies": transliterated_frequencies}

        # Save the output JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)
        
        print(f"Transliterated data saved successfully to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    input_file_path = '/home/bumblebee/wiseyak_backup/aakriti/TTS/NepaliNameDatasetKaggle.json'
    output_file_path = '/home/bumblebee/wiseyak_backup/aakriti/TTS/NepaliToEnglishTransliterated.json'
    
    # Transliterate and save the JSON
    transliterate_json(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
