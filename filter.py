import pandas as pd

# Path to the input CSV file
input_csv = "/home/oem/wiseyak_backup/global_audio_data/Aakriti/transcribe_annotation/transcibe_annotation.csv"
# Path to the output CSV file
output_csv = "/home/oem/wiseyak_backup/global_audio_data/Aakriti/transcribe_annotation/transcibe_annotation_cleaned.csv"

# Load the input CSV file into a DataFrame
df = pd.read_csv(input_csv)

# Create a new DataFrame with the required columns: 'chunk_id', 'file_path', 'transcribe', 'start_time', 'end_time'
df_cleaned = df[['chunk_id', 'file_path', 'transcribe', 'start_time', 'end_time']]

# Function to parse time and handle fractional seconds correctly
def parse_time(time_str):
    # Check if the time string contains fractional seconds (i.e., '.' is present)
    if '.' in time_str:
        return pd.to_datetime(time_str, format='%H:%M:%S.%f', errors='coerce')
    else:
        # Add .000000 if fractional seconds are missing
        return pd.to_datetime(time_str + '.000000', format='%H:%M:%S.%f', errors='coerce')

# Apply the function to parse 'start_time' and 'end_time'
df_cleaned['start_time_parsed'] = df_cleaned['start_time'].apply(parse_time)
df_cleaned['end_time_parsed'] = df_cleaned['end_time'].apply(parse_time)

# Calculate the duration by subtracting start_time from end_time and adding it as a new column
df_cleaned['duration'] = (df_cleaned['end_time_parsed'] - df_cleaned['start_time_parsed']).dt.total_seconds()

# Save the cleaned DataFrame to the output CSV file with the selected columns
df_cleaned[['chunk_id', 'file_path', 'transcribe', 'duration']].to_csv(output_csv, index=False)

print(f"CSV file cleaned and saved to: {output_csv}")
