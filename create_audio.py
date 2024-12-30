import pandas as pd
import os
from pydub import AudioSegment

# File paths
input_csv_path = "/home/oem/wiseyak_backup/global_audio_data/Aakriti/transcribe_annotation/transcibe_annotation_cleaned.csv"
audio_output_dir = "/home/oem/wiseyak_backup/global_audio_data/Aakriti/transcribe_annotation/audio_transcribe"
metadata_csv_path = "/home/oem/wiseyak_backup/global_audio_data/Aakriti/transcribe_annotation/transcribe_metadat.csv"

# Create the audio output directory if it doesn't exist
os.makedirs(audio_output_dir, exist_ok=True)

print("Loading input CSV...")
df = pd.read_csv(input_csv_path)

print("Shuffling dataframe rows...")
shuffled_df = df.sample(frac=1).reset_index(drop=True)

used_ids = set()

# Check if metadata file exists
metadata_exists = os.path.isfile(metadata_csv_path)

# If metadata does not exist, create an empty file with headers
if not metadata_exists:
    print("Metadata file does not exist. Creating with headers.")
    pd.DataFrame(columns=['id', 'chunk_id', 'file_path', 'transcribe', 'Total Duration (s)'])\
      .to_csv(metadata_csv_path, index=False)

iteration_count = 0

while not shuffled_df.empty:
    iteration_count += 1
    print(f"\nStarting iteration {iteration_count}...")
    current_duration = 0
    selected_clips = []

    print("Selecting clips until total duration is between 18-25 seconds...")
    for index, row in shuffled_df.iterrows():
        clip_duration = row['duration']
        if current_duration + clip_duration <= 25:
            selected_clips.append(row)
            current_duration += clip_duration
        if 18 <= current_duration <= 25:
            break

    # If no clips are selected, we are done
    if not selected_clips:
        print("No clips selected. Stopping.")
        break

    # Merge selected audio clips
    print(f"Selected {len(selected_clips)} clips. Merging audio...")
    merged_audio = AudioSegment.empty()
    merged_chunk_ids = []
    merged_transcribes = []

    for clip in selected_clips:
        audio = AudioSegment.from_file(clip['file_path'])
        merged_audio += audio
        merged_chunk_ids.append(str(clip['chunk_id']))
        merged_transcribes.append(str(clip['transcribe']) if not pd.isna(clip['transcribe']) else "")

    # Save merged audio with row iteration count as name
    merged_audio_id = f"transcribe_row_{iteration_count}"
    output_file_path = os.path.join(audio_output_dir, f"{merged_audio_id}.wav")
    print(f"Exporting merged audio to {output_file_path}...")
    merged_audio.export(output_file_path, format="wav")

    # Combine transcription of all selected clips into one
    combined_transcription = " ".join([t for t in merged_transcribes if t.strip() != ""])

    metadata_record = {
        'id': iteration_count,  # Using iteration count as the id
        'chunk_id': ",".join(merged_chunk_ids),
        'file_path': output_file_path,
        'transcribe': combined_transcription,
        'Total Duration (s)': current_duration
    }

    print("Appending metadata to CSV...")
    pd.DataFrame([metadata_record]).to_csv(metadata_csv_path, mode='a', header=False, index=False)

    # Mark the selected clips as used
    used_ids.update(merged_chunk_ids)

    # Remove used clips from the dataframe
    print("Removing used clips from the list...")
    shuffled_df = shuffled_df[~shuffled_df['chunk_id'].isin(used_ids)].reset_index(drop=True)

print("Merging completed. Metadata saved successfully.")
