from pytubefix import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        print(f"🎬 Title: {yt.title}")
        print("📥 Downloading...")
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("✅ Download completed!")
    except Exception as e:
        print("❌ Error:", e)

# Example usage
video_url = input("Enter YouTube video URL: ")
download_video(video_url)