import json

def fix_transliterations(input_file, output_file):
    try:
        # Load the input JSON file
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Access the "word_frequencies" dictionary
        word_frequencies = data.get("word_frequencies", {})

        # Modify transliterations ending with "ra"
        corrected_frequencies = {}
        for nepali_word, transliteration in word_frequencies.items():
            if transliteration.endswith("ta"):
                transliteration = transliteration[:-2] + "t"  # Replace "ra" with "r"
            corrected_frequencies[nepali_word] = transliteration

        # Prepare the output structure
        output_data = {"word_frequencies": corrected_frequencies}

        # Save the corrected JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)
        
        print(f"Corrected transliterations saved successfully to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    input_file_path = '/home/bumblebee/wiseyak_backup/aakriti/TTS/NepaliToEnglishFixed.json'
    output_file_path = '/home/bumblebee/wiseyak_backup/aakriti/TTS/NepaliToEnglishFixed.json'
    
    # Fix transliterations and save the corrected JSON
    fix_transliterations(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
