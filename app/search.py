from youtubesearchpython import VideosSearch

# Function to search YouTube for a video by song name
def search_youtube(song_name):
    try:
        print(f"Searching YouTube for '{song_name}'...")
        videos_search = VideosSearch(song_name, limit=1)
        result = videos_search.result()
        video_info = result['result'][0]
        
        # Get the video URL
        video_url = video_info['link']
        print(f"Found video: {video_info['title']} (URL: {video_url})")
        
        return video_url

    except Exception as e:
        print(f"Error searching YouTube: {str(e)}")
        return None
