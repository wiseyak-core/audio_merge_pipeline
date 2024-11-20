import json
import pandas as pd
import os
from datasets import load_dataset
from huggingface_hub import login
import glob

# Define the path to the JSON file and the directory to save CSV files
json_path = "/home/bumblebee/wiseyak_backup/aakriti/aakriti/datasets.json"
csv_dir = "/home/bumblebee/wiseyak_backup/aakriti/aakriti/"  # Directory to save CSV files
merged_csv_path = os.path.join(csv_dir, "merged_filtered_data.csv")  # Path for the merged CSV file

# Ensure the directory exists
os.makedirs(csv_dir, exist_ok=True)

# Function to log in to Hugging Face
def login_to_huggingface():
    token = "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"  # Replace with your Hugging Face token
    login(token=token)
    print("Successfully logged in to Hugging Face")

# Function to load datasets from JSON file
def load_datasets_from_json(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    all_datasets = {}
    for dataset_name, dataset_info in data["datasets"].items():
        dataset_path = dataset_info[0]
        lang = dataset_info[1] if len(dataset_info) > 1 else None
        all_datasets[dataset_name] = (dataset_path, lang)
    return all_datasets

# Function to load all datasets, add language info, and save individual filtered CSV files
def load_all_datasets(datasets):
    for dataset_name, (dataset_path, lang) in datasets.items():
        try:
            # Load the dataset
            dataset = load_dataset(dataset_path, lang, split="train") if lang else load_dataset(dataset_path, split="train")
            
            # Convert the dataset to DataFrame and print the head to understand the structure
            df = dataset.to_pandas()
            print(f"Dataset structure for {dataset_name}:\n{df.head()}\n")
            
            # Extract only the required columns: index_no, sentence, audio_id, duration
            data = []
            for idx, example in enumerate(dataset):
                if 'sentence' in example and 'audio' in example:
                    transcript = example['sentence']
                    utterance_id = example['client_id'] if 'client_id' in example else f"{dataset_name}_{idx}"
                    duration = len(example['audio']['array']) / example['audio']['sampling_rate'] if 'array' in example['audio'] else None
                    index_no = idx
                    data.append([index_no, transcript, utterance_id, duration, lang, dataset_name])  # Add language info
            
            # Convert to DataFrame
            df_filtered = pd.DataFrame(data, columns=["index_no", "transcript", "utterance_id", "duration", "language","dataset_name"])
            output_path = f"{csv_dir}{dataset_name}_filtered_data.csv"
            
            # Save required columns to the CSV file
            df_filtered.to_csv(output_path, index=False, encoding="utf-8")
            print(f"Filtered data CSV created for {dataset_name} at {output_path}")

        except Exception as e:
            print(f"Error loading {dataset_name}: {str(e)}")
    return True

# Function to merge all filtered CSV files
def merge_filtered_csv_files(csv_directory, output_path):
    all_files = glob.glob(os.path.join(csv_directory, "*_filtered_data.csv"))
    combined_df = pd.concat((pd.read_csv(file) for file in all_files), ignore_index=True)
    combined_df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"All filtered CSV files have been merged into {output_path}")

# Main execution
if __name__ == "__main__":
    # Log in to Hugging Face
    login_to_huggingface()
    
    # Load datasets from JSON and process each
    datasets = load_datasets_from_json(json_path)
    loaded_datasets = load_all_datasets(datasets)
    
    # Merge all filtered CSV files into a single CSV
    merge_filtered_csv_files(csv_dir, merged_csv_path)
