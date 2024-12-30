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

1. **Install dependencies**:

```bash
pip install pandas pydub


**filetr.py**
# CSV Cleaning and Duration Calculation

This script processes an input CSV file, cleans the data by selecting specific columns, and calculates the duration for each audio clip based on the start and end times. The cleaned data is then saved to a new CSV file.

## Features
- **Input CSV Processing**: Loads an input CSV file containing audio clip metadata.
- **Time Parsing**: Handles time strings with or without fractional seconds and parses them into datetime format.
- **Duration Calculation**: Calculates the duration of each audio clip by subtracting the `start_time` from the `end_time`.
- **Output CSV**: Saves the cleaned data (with calculated durations) into a new CSV file.

## Code Breakdown

### 1. **Set File Paths**

```python
input_csv = "/home/oem/wiseyak_backup/global_audio_data/Aakriti/transcribe_annotation/transcibe_annotation.csv"
output_csv = "/home/oem/wiseyak_backup/global_audio_data/Aakriti/transcribe_annotation/transcibe_annotation_cleaned.csv"
The input and output CSV file paths are defined. The input file contains metadata about audio clips, and the output file will store the cleaned data.
2. Load Input CSV into DataFrame
python
Copy code
df = pd.read_csv(input_csv)
The input CSV file is loaded into a DataFrame using pandas.
3. Select Required Columns
python
Copy code
df_cleaned = df[['chunk_id', 'file_path', 'transcribe', 'start_time', 'end_time']]
A new DataFrame df_cleaned is created by selecting specific columns from the original DataFrame (chunk_id, file_path, transcribe, start_time, end_time).
4. Time Parsing Function
python
Copy code
def parse_time(time_str):
    if '.' in time_str:
        return pd.to_datetime(time_str, format='%H:%M:%S.%f', errors='coerce')
    else:
        return pd.to_datetime(time_str + '.000000', format='%H:%M:%S.%f', errors='coerce')
The parse_time function parses time strings. It handles time with or without fractional seconds by checking for the presence of a dot (.). If no fractional seconds are present, .000000 is added to the string.
5. Apply Time Parsing
python
Copy code
df_cleaned['start_time_parsed'] = df_cleaned['start_time'].apply(parse_time)
df_cleaned['end_time_parsed'] = df_cleaned['end_time'].apply(parse_time)
The parse_time function is applied to both the start_time and end_time columns to convert them into proper datetime format.
6. Calculate Duration
python
Copy code
df_cleaned['duration'] = (df_cleaned['end_time_parsed'] - df_cleaned['start_time_parsed']).dt.total_seconds()
The duration for each clip is calculated by subtracting start_time from end_time and converting the result into total seconds.
7. Save Cleaned Data to Output CSV
python
Copy code
df_cleaned[['chunk_id', 'file_path', 'transcribe', 'duration']].to_csv(output_csv, index=False)
The cleaned DataFrame with chunk_id, file_path, transcribe, and duration is saved to the specified output CSV file.
8. Final Print Statement
python
Copy code
print(f"CSV file cleaned and saved to: {output_csv}")
A message is printed to indicate that the CSV file has been cleaned and saved.
Example Output
The output CSV file (transcibe_annotation_cleaned.csv) will contain the following columns:

chunk_id: Unique identifier for the audio chunk.
file_path: Path to the audio file.
transcribe: The transcription for the audio clip (if available).
duration: The calculated duration of the audio clip in seconds.
Notes
The script ensures proper time handling by accounting for fractional seconds and ensures that the duration is calculated correctly.
The output CSV contains only the relevant columns and the calculated duration.
Usage
Update the input_csv and output_csv variables to point to your input and output files.
Run the script, and the cleaned CSV with durations will be saved to the output path.



Here’s an ASCII-style explanation of the code in a `README.md` format:

```markdown
# CSV File Splitting Based on Duration

This script reads a CSV file containing audio clip metadata, calculates the duration of each audio clip, and splits the data into multiple smaller CSV files based on a duration limit (1 hour). Each split file contains audio clips that together have a total duration of up to 1 hour.

## Features
- **Duration Calculation**: Calculates the duration of each audio clip based on `start_time` and `end_time` columns in the CSV.
- **Splitting**: Splits the data into multiple smaller CSV files, ensuring that the total duration of each file does not exceed 1 hour.
- **Output Files**: Saves the split files in a specified directory with filenames like `split_file_1.csv`, `split_file_2.csv`, etc.

## Code Breakdown

### 1. **Load CSV File**

```python
file_path = '/home/oem/wiseyak_backup/global_audio_data/Aakriti/global-ime.csv'
data = pd.read_csv(file_path)
```

- The script loads the input CSV file into a `DataFrame` using `pandas`. The CSV contains audio clip metadata, including `start_time` and `end_time`.

### 2. **Calculate Duration**

```python
def calculate_duration(row):
    start = datetime.strptime(row['start_time'], "%H:%M:%S")
    end = datetime.strptime(row['end_time'], "%H:%M:%S")
    return (end - start).total_seconds()
```

- The `calculate_duration` function calculates the duration in seconds for each audio clip by parsing the `start_time` and `end_time` as `datetime` objects and calculating the difference.

### 3. **Add Duration Column**

```python
data['duration'] = data.apply(calculate_duration, axis=1)
```

- The `apply` function is used to apply the `calculate_duration` function to each row in the `DataFrame`, adding a new column `duration` to the data.

### 4. **Create Output Directory**

```python
output_dir = '/home/oem/wiseyak_backup/global_audio_data/Aakriti/split_files'
os.makedirs(output_dir, exist_ok=True)
```

- The output directory is created (if it doesn't already exist) to store the split CSV files.

### 5. **Split the Data into Multiple Files**

```python
current_file_duration = 0
current_file_data = []
file_index = 1

for _, row in data.iterrows():
    if current_file_duration + row['duration'] > 3600:  # 1 hour = 3600 seconds
        output_file = os.path.join(output_dir, f'split_file_{file_index}.csv')
        pd.DataFrame(current_file_data).to_csv(output_file, index=False)
        file_index += 1
        current_file_duration = 0
        current_file_data = []

    current_file_data.append(row)
    current_file_duration += row['duration']
```

- The script iterates over each row in the `DataFrame` and adds audio clips to the current split file until the total duration exceeds 1 hour (3600 seconds).
- When the limit is exceeded, the current data is saved to a new CSV file, and the process starts again for the next file.

### 6. **Save Remaining Data**

```python
if current_file_data:
    output_file = os.path.join(output_dir, f'split_file_{file_index}.csv')
    pd.DataFrame(current_file_data).to_csv(output_file, index=False)
```

- After the loop finishes, if there is any remaining data that hasn't been saved, it is written to the last split CSV file.

### 7. **Final Output Message**

```python
print(f"CSV files have been split and saved in {output_dir}")
```

- A message is printed to indicate that the CSV files have been successfully split and saved in the specified directory.

## Example Output

The script will save the split CSV files in the `split_files` directory with filenames like:
- `split_file_1.csv`
- `split_file_2.csv`
- ...

Each CSV file will contain a subset of the original data, where the total duration of the clips in each file does not exceed 1 hour.

## Notes

- The script assumes that the `start_time` and `end_time` columns in the input CSV file are formatted as `HH:MM:SS` (with or without fractional seconds).
- The output files are named incrementally, starting from `split_file_1.csv`.
- If the total duration of the clips in the CSV exceeds 1 hour, they will be distributed across multiple files.
```
