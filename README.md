# README: Dataset Filtering and Merging Script
main.py
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



create_audio.py
# Audio Merging and Metadata Generation

This script processes and merges audio clips into a single file with a total duration of 18-25 seconds. It also generates metadata for each merged audio file and stores the relevant information in a CSV file.

## Features

- **Shuffling**: Randomizes the order of audio clips.
- **Clip Selection**: Selects audio clips with a total duration between 18 and 25 seconds.
- **Audio Merging**: Merges selected audio clips into a single file.
- **Metadata Generation**: Saves metadata (chunk IDs, transcription, and duration) for each merged audio file into a CSV.
- **CSV Output**: Outputs metadata in a CSV file for easy tracking and management.

## File Structure

- **Input CSV**: 
  The script expects an input CSV (`transcibe_annotation_cleaned.csv`) containing the following columns:
  - `chunk_id`: Unique ID for each audio chunk.
  - `file_path`: Path to the audio file.
  - `duration`: Duration of the audio clip in seconds.
  - `transcribe`: The transcription for the audio clip (optional).

- **Output**:
  - Merged audio files are saved in the directory specified by `audio_transcribe`.
  - Metadata about each merged file is stored in the CSV file (`transcribe_metadat.csv`).

## Installation
# Audio Dataset Processing and Merging Scripts

This repository consists of four Python scripts that handle audio dataset processing, filtering, merging, and CSV file management. Below is a concise overview of each script's functionality.

## 1. `main.py` - Dataset Loading and Merging
This script automates the process of loading datasets from Hugging Face, filtering the relevant fields, and merging them into a single CSV file.

### Features:
- **Hugging Face Integration**: Authenticates with Hugging Face using an API token.
- **Dataset Loading**: Loads datasets dynamically from a JSON configuration.
- **Data Filtering**: Filters `transcript`, `utterance_id`, `duration`, and `language`.
- **CSV Export**: Saves filtered data as CSV files.
- **CSV Merging**: Merges all filtered CSVs into a single file.

### Key Functions:
- `login_to_huggingface()`: Logs in to Hugging Face.
- `load_datasets_from_json()`: Loads datasets from the JSON file.
- `load_all_datasets()`: Filters and saves data as CSV.
- `merge_filtered_csv_files()`: Merges CSVs into a single file.

---

## 2. `filter.py` - Data Cleaning and Duration Calculation
This script processes an input CSV file, cleans the data, and calculates the duration for each audio clip based on start and end times.

### Features:
- **Time Parsing**: Handles time parsing with or without fractional seconds.
- **Duration Calculation**: Computes audio clip duration in seconds.
- **Output CSV**: Saves cleaned data with calculated durations.

### Key Functions:
- `parse_time()`: Parses time in HH:MM:SS format.
- **Data Processing**: Loads CSV, calculates durations, and outputs cleaned CSV.

---

## 3. `hour.py` - CSV Splitting Based on Duration
This script reads a CSV, calculates audio clip durations, and splits the data into smaller CSV files where the total duration does not exceed 1 hour (3600 seconds).

### Features:
- **Duration Calculation**: Calculates total duration for each clip.
- **Splitting**: Splits data into multiple files with a duration limit of 1 hour.
- **Output**: Saves split files with filenames like `split_file_1.csv`.

### Key Functions:
- **CSV Splitting**: Iterates through data, splits into files when the duration exceeds 1 hour.
- **File Saving**: Saves each split file incrementally.

---

## 4. `create_audio.py` - Audio Merging and Metadata Generation
This script merges audio clips to create files with a duration between 18-25 seconds and generates metadata in a CSV.

### Features:
- **Shuffling**: Randomizes the order of audio clips.
- **Clip Selection**: Selects clips with a total duration between 18-25 seconds.
- **Audio Merging**: Merges selected clips into a single file.
- **Metadata Generation**: Outputs metadata to a CSV file.

### Key Functions:
- **Audio Merging**: Merges clips into one file.
- **Metadata Saving**: Saves metadata like chunk ID, transcription, and duration.

---

## Example Directory Structure
---

## Detailed Breakdown of Script Functions

### `main.py` - Dataset Loading and Merging

This script ensures the loading, filtering, and merging of multiple datasets into a single CSV. It simplifies the process of combining language datasets from Hugging Face.

- **Loading datasets**: It loads datasets dynamically based on the JSON configuration, making it flexible to handle various datasets.
- **Filtering data**: Essential fields like `transcript`, `utterance_id`, and `duration` are extracted from each dataset.
- **Merging CSVs**: After filtering each dataset, they are combined into a final CSV for further processing.

### `filter.py` - Data Cleaning and Duration Calculation

This script handles the preprocessing of audio metadata CSV files:
- **Time Parsing**: Converts time fields (start_time, end_time) into a standardized format.
- **Duration Calculation**: Computes the total duration for each audio clip by subtracting start time from end time.
- **Cleaned Output**: After cleaning and calculating the durations, the data is saved into a new CSV file.

### `hour.py` - CSV Splitting Based on Duration

For datasets with audio clips, this script ensures that no CSV file exceeds a total duration of 1 hour:
- **Duration Calculation**: It sums the durations of audio clips and keeps track of the total duration.
- **File Splitting**: When the duration limit is exceeded, it starts a new CSV file, ensuring each split file stays within the 1-hour limit.
- **File Management**: Outputs split files and ensures that no data is lost due to duration constraints.

### `create_audio.py` - Audio Merging and Metadata Generation

This script takes multiple audio clips, merges them, and generates metadata:
- **Audio Shuffling**: The order of the clips is randomized to prevent biases in the merging process.
- **Clip Selection**: Clips are chosen so that their total duration falls between 18-25 seconds.
- **Metadata Generation**: For each merged audio file, a metadata CSV is generated with chunk IDs, transcriptions, and durations.

---

## Example Use Case

### Merging English and Nepali Audio
Suppose you have separate datasets for English and Nepali audio clips. You want to merge them into multilingual audio files, ensuring that the final audio file has a duration of around 25 seconds (e.g., 10 seconds of English, 15 seconds of Nepali). The scripts facilitate this by:

1. **Loading datasets** from Hugging Face (using `main.py`).
2. **Cleaning data** (with `filter.py`) and calculating the duration of each clip.
3. **Splitting data** based on duration if required (using `hour.py`).
4. **Merging audio clips** (with `create_audio.py`) into a final file and generating corresponding metadata.

### Workflow Example
1. **JSON Config**: The `datasets.json` defines paths to Hugging Face datasets and language codes.
2. **Data Filtering**: Use `main.py` to load datasets, filter essential data fields, and save them as CSV files.
3. **Splitting**: If the CSV file is too large, use `hour.py` to split the data into smaller, manageable parts.
4. **Merging Audio**: Finally, use `create_audio.py` to merge the audio clips into a final multilingual audio file with appropriate metadata.

---

## Final Thoughts

These scripts provide a robust pipeline for handling and processing audio datasets, allowing you to automate:
- Dataset loading and merging.
- Filtering essential data.
- Audio file splitting based on duration.
- Merging audio clips with metadata generation.

By combining these functionalities, users can efficiently manage and process large datasets for multilingual audio tasks or any similar use case that involves audio data processing and organization.

