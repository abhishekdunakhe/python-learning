import yt_dlp

# Video URL yahan daal
video_url = 'https://www.youtube.com/watch?v=UrsmFxEIp5k&t=10146s'  # <-- Replace with your link

# Options for high-quality download
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Best quality video + audio
    'merge_output_format': 'mp4',          # Output file format
    'outtmpl': '%(title)s.%(ext)s',        # Save as video title
    'quiet': False                         # Show progress
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
