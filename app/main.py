import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.search import search_youtube
from app.downloader import download_audio_from_youtube

if __name__ == "__main__":
    # Get the song name from the user
    song_name = input("Enter the name of the song: ")

    # Search YouTube for the song and get the first result URL
    video_url = search_youtube(song_name)

    if video_url:
        # Download the YouTube video as audio
        audio_file = download_audio_from_youtube(video_url)

        # Check if download was successful
        if audio_file:
            print(f"Downloaded audio file: {audio_file}")
        else:
            print("Audio download failed.")
    else:
        print("Could not find the song on YouTube.")
