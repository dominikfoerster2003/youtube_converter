from pytube import YouTube
import os
from pydub import AudioSegment
import tarfile
import urllib
import sys
import progressbar
import tkinter as tk



path2= os.path.expanduser("~") + "/Downloads/"
path= new_string = path2.replace("\\", "/")
install_path= "C:/"
            
if os.name == "nt":
    AudioSegment.ffmpeg = "C:/FFmpeg/bin/ffmpeg.exe"

def submit():
    url = entry.get()
    format = var.get()
    yt = YouTube(url) 
    yt_video_info = ()
    
    if format == "MP4":
        formats = yt.streams.filter(progressive=True, file_extension='mp4')
        video = max(formats, key=lambda x: x.resolution)
        video_path = video.download(path)
        print("Finished!")
    elif format == "MP3":
        formats = yt.streams.filter(progressive=True, file_extension='mp4')
        video = max(formats, key=lambda x: x.resolution)
        mp4_file = video.download(path)
        mp3_file = video.default_filename.replace('.mp4', '.mp3')
        audio = AudioSegment.from_file(mp4_file, format='mp4')
        audio.export(path+"/"+mp3_file, format='mp3')
        os.remove(mp4_file)
        print("Finished!")

        

root = tk.Tk()

label = tk.Label(root, text="Eingabe:")
label.pack()

entry = tk.Entry(root)
entry.pack()

label = tk.Label(root, text="Auswahl:")
label.pack()

var = tk.StringVar(value="MP4")
option1 = tk.Radiobutton(root, text="MP4", variable=var, value="MP4")
option1.pack()
option2 = tk.Radiobutton(root, text="MP3", variable=var, value="MP3")
option2.pack()

button = tk.Button(root, text="Bestätigen", command=submit)
button.pack()

entry.pack(fill=tk.X)

root.geometry("500x200")
root.mainloop()