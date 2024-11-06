from flask import Flask, render_template, request, send_from_directory
import os
from downloader import download_audio_from_youtube  # Ensure this function is in your downloader.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    song_name = request.form.get('song_name')
    print(f"Received song name: '{song_name}'")  # Debugging line

    if not song_name:
        return "Error: No song name provided."

    # Sanitize the song name if needed
    song_name = song_name.strip()  # Remove leading/trailing whitespace
    print(f"Sanitized song name: '{song_name}'")  # Debugging line

    # Call the downloader function to download MP3
    downloaded_file = download_audio_from_youtube(song_name)
    print(f"Downloaded file path: {downloaded_file}")  # Debugging line

    if downloaded_file and os.path.exists(downloaded_file):
        filename = os.path.basename(downloaded_file)
        print(f"Serving file: {filename} from {os.path.dirname(downloaded_file)}")  # Debugging line
        return send_from_directory(
            os.path.dirname(downloaded_file),
            filename,
            as_attachment=True
        )
    else:
        print(f"File not found: {downloaded_file}")  # Debugging line
        return "Error: The file could not be downloaded. Please check the song name and try again."

if __name__ == '__main__':
    app.run(debug=True, port=5000)
