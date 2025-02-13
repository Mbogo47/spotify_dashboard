import pandas as pd
import json


# Load the JSON files (replace 'video.json' and 'audio.json' with actual file paths)
video_file = "C:/Users/Ivy/Downloads/Spotify Extended Streaming History/Streaming_History_Video_2023-2025.json"
audio_file = "C:/Users/Ivy/Downloads/Spotify Extended Streaming History/Streaming_History_Audio_2023-2025.json"


with open(video_file, "r", encoding="utf-8") as f:
    video_data = json.load(f)

with open(audio_file, "r", encoding="utf-8") as f:
    audio_data = json.load(f)

# Convert JSON to DataFrames
video_df = pd.DataFrame(video_data)
audio_df = pd.DataFrame(audio_data)

# Select relevant columns
columns_to_keep = [
    "ts", "platform", "ms_played", "conn_country", "master_metadata_track_name",
    "master_metadata_album_artist_name", "master_metadata_album_album_name",
    "spotify_track_uri", "shuffle", "skipped", "reason_start", "reason_end"
]

video_df = video_df[columns_to_keep]
audio_df = audio_df[columns_to_keep]

# Merge video and audio data
merged_df = pd.concat([video_df, audio_df], ignore_index=True)

# Convert timestamp to datetime format
merged_df["ts"] = pd.to_datetime(merged_df["ts"])

# Sort by timestamp
merged_df = merged_df.sort_values(by="ts")

# Show cleaned data preview
merged_df.columns = merged_df.columns.str.replace(r'[^\w\s]', '', regex=True)  # Remove special characters
merged_df["ts"] = pd.to_datetime(merged_df["ts"]).dt.strftime("%Y-%m-%d %H:%M:%S")
# Drop unnecessary columns
merged_df = merged_df.drop(columns=["reason_start", "reason_end"])

# Save the cleaned data
merged_df.to_csv("cleaned_spotify_data.csv", index=False, encoding="utf-8")


print("Finished cleaning data.")