import yt_dlp
import os

def download_audio_from_youtube(song_name):
    # Specify the output directory
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'downloaded-songs')
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Define the output template (download as .mp3)
    output_template = os.path.join(output_dir, '%(title)s.%(ext)s')

    # Define the options for yt-dlp to download and convert to mp3
    ydl_opts = {
        'format': 'bestaudio/best',  # Download best available audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract audio using FFmpeg
            'preferredcodec': 'mp3',      # Save the audio in MP3 format
            'preferredquality': '192',    # Set the quality (bitrate) for MP3
        }],
        'outtmpl': output_template,       # Output file template
        'noplaylist': True,               # Download only a single video
        'retries': 5,                     # Retry downloading
        'postprocessor_args': [
            '-ar', '44100',               # Set audio sample rate
            '-ac', '2',                   # Set audio channels
        ]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Attempting to download: {song_name}")  # Debugging line
            result = ydl.extract_info(f"ytsearch:{song_name}", download=True)
            print(f"Download result: {result}")  # Debugging line

        # Get the first entry from the result (if a playlist is returned, we only want the first audio)
        if "entries" in result:
            result = result["entries"][0]

        downloaded_file = ydl.prepare_filename(result).replace('.webm', '.mp3')  # Ensure it's .mp3
        print(f"File downloaded to: {downloaded_file}")  # Debugging line

        if os.path.exists(downloaded_file):
            print(f"File exists: {downloaded_file}")
            return downloaded_file
        else:
            print(f"File not found after download: {downloaded_file}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
