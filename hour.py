import pandas as pd
import os
from datetime import datetime, timedelta

# Load the CSV file
file_path = '/home/oem/wiseyak_backup/global_audio_data/Aakriti/global-ime.csv'
data = pd.read_csv(file_path)

# Function to calculate duration in seconds
def calculate_duration(row):
    start = datetime.strptime(row['start_time'], "%H:%M:%S")
    end = datetime.strptime(row['end_time'], "%H:%M:%S")
    return (end - start).total_seconds()

# Add a column for duration
data['duration'] = data.apply(calculate_duration, axis=1)

# Split the data into multiple files based on a 1-hour duration limit
output_dir = '/home/oem/wiseyak_backup/global_audio_data/Aakriti/split_files'
os.makedirs(output_dir, exist_ok=True)

current_file_duration = 0
current_file_data = []
file_index = 1

for _, row in data.iterrows():
    if current_file_duration + row['duration'] > 3600:  # 1 hour = 3600 seconds
        # Save the current file
        output_file = os.path.join(output_dir, f'split_file_{file_index}.csv')
        pd.DataFrame(current_file_data).to_csv(output_file, index=False)
        file_index += 1
        current_file_duration = 0
        current_file_data = []

    current_file_data.append(row)
    current_file_duration += row['duration']

# Save any remaining data to a new file
if current_file_data:
    output_file = os.path.join(output_dir, f'split_file_{file_index}.csv')
    pd.DataFrame(current_file_data).to_csv(output_file, index=False)

print(f"CSV files have been split and saved in {output_dir}")
