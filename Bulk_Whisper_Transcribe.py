import os
import whisper

# Folder path containing the audio files
folder_path = "<file Path>"

# Load the whisper model
model = whisper.load_model("tiny.en")

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an audio file
    if filename.endswith(".mp3"):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Transcribe the audio file
        result = model.transcribe(file_path)
        
        # Extract the file name without extension
        file_name_without_ext = os.path.splitext(filename)[0]
        
        # Create a text file name
        output_file = os.path.join(folder_path, f"{file_name_without_ext}.txt")
        
        # Save the transcription to a text file
        with open(output_file, "w") as f:
            f.write(result["text"])
            
        print(f"Transcription saved for {filename}")
