from flask import Flask, render_template, request, send_from_directory
import os
from app.downloader import download_audio_from_youtube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    song_name = request.form.get('song_name')
    
    if not song_name:
        return "Error: No song name provided."

    # Sanitize and download the song
    song_name = song_name.strip()
    downloaded_file = download_audio_from_youtube(song_name)

    # Serve the downloaded file if it exists
    if downloaded_file and os.path.exists(downloaded_file):
        filename = os.path.basename(downloaded_file)
        return send_from_directory(
            os.path.dirname(downloaded_file),
            filename,
            as_attachment=True
        )
    else:
        return "Error: The file could not be downloaded. Please check the song name and try again."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
