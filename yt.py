#https://developers.google.com/youtube/v3 - YouTube official API

#pip install pytube
#https://pytube.io/en/latest/user/quickstart.html#downloading-a-video
from pytube import YouTube

folder = "B:/pyx/SDA/SDA_52"
youtube_url = "https://www.youtube.com/watch?v=mBStK_vj6j4&ab_channel=UFDTech"

yt_video = YouTube(youtube_url) #obiectul Youtube creat din url-ul video-ului
print(yt_video.title)

for stream in yt_video.streams:
    print(stream)

video_tag = 137
stream = yt_video.streams.get_by_itag(video_tag)
stream.download(output_path= f"{folder}/{yt_video.title}")

audio_tag = 251
stream = yt_video.streams.get_by_itag(audio_tag)
stream.download(output_path= f"{folder}/{yt_video.title}")