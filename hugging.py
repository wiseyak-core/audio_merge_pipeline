from huggingface_hub import HfApi, HfFolder
import os

# Replace with your actual access token
ACCESS_TOKEN = "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"

# Set the token for authentication
HfFolder.save_token(ACCESS_TOKEN)
api = HfApi()

# Repository details
USER_NAME = "Wiseyak"
REPO_NAME = "Global_NTC_KeywordsTTS"

# Directory containing the files to upload
FILES_DIR = "/home/bumblebee/wiseyak_backup/aakriti/TTS/Banking"

# Create the repository if it does not exist
try:
    api.create_repo(repo_id=f"{USER_NAME}/{REPO_NAME}", repo_type="dataset", private=False)
    print(f"Repository '{REPO_NAME}' created successfully!")
except Exception as e:
    print(f"Repository '{REPO_NAME}' might already exist: {e}")

# Upload files to the repository
for root, _, files in os.walk(FILES_DIR):
    for file in files:
        file_path = os.path.join(root, file)
        relative_path = os.path.relpath(file_path, FILES_DIR)
        
        try:
            api.upload_file(
                path_or_fileobj=file_path,
                path_in_repo=relative_path,
                repo_id=f"{USER_NAME}/{REPO_NAME}",
                repo_type="dataset"
            )
            print(f"Uploaded: {relative_path}")
        except Exception as e:
            print(f"Failed to upload {relative_path}: {e}")

print("File upload completed!")
