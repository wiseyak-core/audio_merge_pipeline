# TTS_model
# Text-to-Speech (TTS) Audio Generator for Nepali Words

This Python script generates TTS audio files for words in Nepali using an external TTS API. The script processes words in batches, saves the audio files, and displays them in a Jupyter notebook.

## Key Steps:

1. **API Setup**: The script sends a request to the TTS API (`http://fs.wiseyak.com:8026/xtts_text`) with each word to generate audio in Nepali.
2. **Loading Word Frequencies**: The word frequencies are loaded from a JSON file (`test.json`), and each word is processed in batches of 250.
3. **Audio Generation**: For each word, a POST request is sent to the API, and the resulting audio is saved as a `.wav` file in the specified directory.
4. **Displaying Audio**: After each batch, the generated audio files are displayed in the Jupyter notebook using IPython's `Audio` widget.
5. **Batch Processing**: After processing 250 words, the script clears the notebook output to keep it clean, and continues to the next batch.

## Required Libraries:

- `requests`: To send HTTP requests to the TTS API.
- `json`: To load the word frequencies from the JSON file.
- `os`: To manage file paths and directories.
- `IPython.display`: To display audio files in Jupyter notebooks.

## Usage:

1. Set the `word_frequencies_json_path` to your word frequency file.
2. Ensure the TTS API URL is correct and reachable.
3. Run the script to generate and display the audio for each word.

## Error Handling:

If the TTS request fails, the error is logged, and the process continues for the remaining words.

