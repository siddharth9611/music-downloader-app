import yt_dlp
import os

def download_audio_from_youtube(song_name, cookies_path=None):
    # Define the output directory for downloaded audio files
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'downloaded-songs')
    os.makedirs(output_dir, exist_ok=True)

    # Define FFmpeg path for yt-dlp configuration
    ffmpeg_path = os.path.join(os.path.dirname(__file__), 'ffmpeg', 'ffmpeg.exe')

    # Output template for the downloaded audio file
    output_template = os.path.join(output_dir, '%(title)s.%(ext)s')

    # Define options for yt-dlp, including FFmpeg location
    ydl_opts = {
        'format': 'bestaudio/best',            # Best available audio quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',       # Extract audio using FFmpeg
            'preferredcodec': 'mp3',           # Save the audio as MP3
            'preferredquality': '192',         # Set the quality to 192kbps
        }],
        'outtmpl': output_template,            # Set the output file template
        'noplaylist': True,                    # Only download a single video
        'retries': 5,                          # Retry download if it fails
        'postprocessor_args': ['-ar', '44100', '-ac', '2'],  # Audio settings
        'ffmpeg_location': ffmpeg_path         # Specify FFmpeg executable location
    }

    # If a cookies path is provided, add it to yt-dlp options
    if cookies_path:
        ydl_opts['cookiefile'] = cookies_path

    try:
        # Initialize yt-dlp with the specified options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Attempting to download: {song_name}")
            result = ydl.extract_info(f"ytsearch:{song_name}", download=True)

        # Get the downloaded file path
        if "entries" in result:
            result = result["entries"][0]  # Use the first result if multiple entries are returned

        downloaded_file = ydl.prepare_filename(result).replace('.webm', '.mp3')

        # Return the downloaded file path if it exists
        if os.path.exists(downloaded_file):
            print(f"File downloaded to: {downloaded_file}")
            return downloaded_file
        else:
            print("Download successful, but file not found.")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Usage
if __name__ == "__main__":
    # Get the cookies file path from an environment variable or external source
    cookies_path = os.getenv("YOUTUBE_COOKIES_FILE")  # Pass the path as an environment variable

    # Example: download a song with a cookies file for authentication
    download_audio_from_youtube("sample song name", cookies_path)
