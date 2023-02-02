from pytube import YouTube

path= "/Users/dominikforster/Downloads"

print("Youtube URl:")
url= input()

yt = YouTube(url)

formats = yt.streams.filter(progressive=True, file_extension='mp4')
video = max(formats, key=lambda x: x.resolution)

yt_video_info = (
    "Title: "+yt.title+"\n"+
    "Channel: "+yt.author+"\n"+
    "Length: "+yt.length+"\n"
)

print(yt_video_info)
print("downloading...")
video.download(path)
print("Finished!")

