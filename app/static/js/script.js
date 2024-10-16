document.addEventListener('DOMContentLoaded', function() {
    const downloadButton = document.getElementById('downloadButton');
    const songNameInput = document.getElementById('songName');

    // Add click event listeners to each song item
    const songItems = document.querySelectorAll('.song-item');
    songItems.forEach(item => {
        item.addEventListener('click', function() {
            songNameInput.value = this.textContent; // Set input value to song name
        });
    });

    downloadButton.addEventListener('click', function() {
        const songName = songNameInput.value;
        if (songName) {
            fetch('/download', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: new URLSearchParams({
                    'song_name': songName
                })
            })
            .then(response => {
                if (response.ok) {
                    return response.blob();
                }
                throw new Error('Download failed');
            })
            .then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = songName + '.mp3'; // Specify the desired file name
                document.body.appendChild(a);
                a.click();
                a.remove();
                window.URL.revokeObjectURL(url);
            })
            .catch(error => console.error('Error:', error));
        } else {
            alert('Please enter a song name.');
        }
    });
});
