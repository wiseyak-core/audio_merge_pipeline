# README: Dataset Filtering and Merging Script

## Overview
This script is designed to automate the process of loading datasets from Hugging Face, filtering relevant fields, and merging the filtered data into a single CSV file. The script provides end-to-end functionality, including logging into Hugging Face, dataset loading, data filtering, and merging different language audios to create a multilingual(english ,  nepali and hindi) langauge dataset.

---

## Features
- **Hugging Face Integration**: Automatically authenticates with Hugging Face using an API token.
- **Dataset Loading**: Dynamically loads datasets specified in a JSON configuration file.
- **Data Filtering**: Filters datasets to include essential fields such as `transcript`, `utterance_id`, `duration`, `language`, and `dataset_name`.
- **CSV Export**: Saves filtered data as individual CSV files for each dataset.
- **CSV Merging**: Combines all filtered CSV files into a single, consolidated CSV file.

---

## Prerequisites
1. **Python Environment**: Python 3.8 or above.
2. **Required Libraries**:
   - `json`
   - `pandas`
   - `os`
   - `glob`
   - `datasets` (Hugging Face library)
   - `huggingface_hub`

   Install missing libraries using:



3. **Hugging Face Token**: Obtain your token from [Hugging Face](https://huggingface.co/settings/tokens).

---

## Directory Structure
- **Input JSON File**:  
Location: `/home/bumblebee/wiseyak_backup/aakriti/aakriti/datasets.json`  
Contains metadata for datasets to load.

- **Output CSV Directory**:  
Location: `/home/bumblebee/wiseyak_backup/aakriti/aakriti/`  
Stores individual filtered CSV files for each dataset and the final merged CSV.

---

## Configuration
### JSON Format
The JSON file must include dataset names, paths, and optional language configurations:


- `dataset1_name`: Name of the dataset (used as identifier).
- `dataset1_path`: Hugging Face dataset path.
- `language_code`: (Optional) Language configuration for the dataset.

---

## Script Functionality
### 1. Login to Hugging Face
- **Function**: `login_to_huggingface()`
- Logs into Hugging Face using a predefined API token.

### 2. Load Datasets
- **Function**: `load_datasets_from_json(json_file)`
- Reads the JSON file and prepares a dictionary of datasets with paths and language info.

### 3. Filter Datasets
- **Function**: `load_all_datasets(datasets)`
- Loads each dataset, filters relevant fields, and saves the output to individual CSV files.

### 4. Merge Filtered Data
- **Function**: `merge_filtered_csv_files(csv_directory, output_path)`
- Merges all filtered CSV files into a single CSV file.

---

## How to Use
1. **Set Up Environment**:
   - Place the JSON configuration file in the specified directory.
   - Ensure datasets are accessible through Hugging Face.

2. **Run the Script**:
   Execute the script from the terminal:


3. **Outputs**:
- Filtered CSV files for each dataset in the specified directory.
- A merged CSV file: `merged_filtered_data.csv`.

---

## Output
### Filtered CSV Structure
Each filtered CSV file contains:
- `index_no`: Index of the dataset entry.
- `transcript`: The transcript/sentence from the dataset.
- `utterance_id`: Unique identifier for the audio.
- `duration`: Duration of the audio in seconds.
- `language`: Language of the dataset (if specified).
- `dataset_name`: Name of the dataset.

### Merged CSV Structure
The merged CSV combines all individual datasets, retaining the same columns.

---

## Example Usage
### JSON Configuration Example


### Execution Output
- Individual filtered CSVs:
  - `/home/bumblebee/wiseyak_backup/aakriti/aakriti/common_voice_en_filtered_data.csv`
  - `/home/bumblebee/wiseyak_backup/aakriti/aakriti/common_voice_ne_filtered_data.csv`
  
- Merged CSV:
  - `/home/bumblebee/wiseyak_backup/aakriti/aakriti/merged_filtered_data.csv`

---

## Error Handling
- If a dataset fails to load, the script logs the error and continues with the next dataset.






