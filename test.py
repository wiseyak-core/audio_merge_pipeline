import json
import os
import sys

def filter_census_sentences(input_file, output_file, start_id, end_id):
    """
    Filters census sentences from the input JSON file based on ID range and writes them to the output JSON file.

    Parameters:
    - input_file (str): Path to the input JSON file.
    - output_file (str): Path to the output JSON file.
    - start_id (int): Starting ID (inclusive).
    - end_id (int): Ending ID (inclusive).
    """
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    try:
        # Read the input JSON file
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file. {e}")
        sys.exit(1)

    # Verify that data is a list
    if not isinstance(data, list):
        print("Error: The JSON data is not a list of dictionaries.")
        sys.exit(1)

    # Filter the data based on ID range
    filtered_data = []
    for entry in data:
        # Ensure each entry is a dictionary and has an 'id' key
        if isinstance(entry, dict) and 'id' in entry:
            try:
                entry_id = int(entry['id'])
                if start_id <= entry_id <= end_id:
                    filtered_data.append(entry)
            except ValueError:
                print(f"Warning: Skipping entry with non-integer ID: {entry['id']}")
        else:
            print("Warning: Skipping invalid entry (not a dict or missing 'id').")

    # Check if any entries were found
    if not filtered_data:
        print(f"No entries found with IDs from {start_id} to {end_id}.")
        sys.exit(0)

    # Write the filtered data to the output JSON file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=4)
        print(f"Successfully wrote {len(filtered_data)} entries to '{output_file}'.")
    except Exception as e:
        print(f"Error: Failed to write to '{output_file}'. {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Define the input and output file paths
    INPUT_FILE = "/home/bumblebee/wiseyak_backup/aakriti/TTS/final_sentence.json"
    OUTPUT_FILE = "/home/bumblebee/wiseyak_backup/aakriti/TTS/Voting_sentences_filtered.json"

    # Define the ID range
    START_ID = 90
    END_ID = 168

    # Call the filtering function
    filter_census_sentences(INPUT_FILE, OUTPUT_FILE, START_ID, END_ID)
