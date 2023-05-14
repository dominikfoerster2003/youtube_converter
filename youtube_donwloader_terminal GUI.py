from pytube import YouTube
import os
from pydub import AudioSegment
import tarfile
import urllib
import sys
import progressbar
import json
import tkinter as tk

#path2=os.path.dirname(os.path.abspath(__file__))
path2= os.path.expanduser("~") + "/Downloads/"
path= new_string = path2.replace("\\", "/")
install_path= "C:/"

pbar = None


def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

def FFmpegInstallationWindows():
    print("Downloading FFmpeg...")
    url = "http://ubuntuerfurt.zapto.org/ffmpeg/ffmpeg.tar"
    tar_file = install_path+"ffmpeg.tar"
    urllib.request.urlretrieve(url, install_path+'ffmpeg.tar', show_progress)
    print("Unzip FFmpeg...")
    print("Installing FFmpeg...")
    with tarfile.open(tar_file) as tar:
        tar.extractall(path=install_path)
    os.remove(install_path+"/ffmpeg.tar")
    
def FFmpegInstallationMacos():
    print("Downloading FFmpeg...")
    os.system("brew install ffmpeg")

if os.name == "nt":
    AudioSegment.ffmpeg = "C:/FFmpeg/bin/ffmpeg.exe"
    if os.path.exists(install_path+"/ffmpeg"):
        print("")
    else:
        def InstallFFmpegWindows():
            print("FFmpeg required\nYou want to install it ?...(y/n)")
            install_answer=input()
            if install_answer == "y" and "Y":
                FFmpegInstallationWindows()
            else:
                print('Canceled!')
                sys.exit(1)

if os.name == "posix":
    if os.path.exists("/opt/homebrew/Cellar/ffmpeg/5.1.2_4/bin/"):
        print("")
    else:
        def InstallFFmpegMacOS():
            print("FFmpeg required\nYou want to install it ?...(y/n)")
            install_answer=input()
            if install_answer == "y" and "Y":
                FFmpegInstallationMacos()
            else:
                print('Canceled!')
                sys.exit(1)
            
if os.name == "nt":
    AudioSegment.ffmpeg = "C:/FFmpeg/bin/ffmpeg.exe"
    
def ChangePath():
    print("Enter your Path:")
    path = input()
    print("Changed path to "+path)


def VideoInfo():
    yt_video_info = (
        "Title: "+yt.title+"\n"+
        "Channel: "+yt.author+"\n"+
        "Release: "+str(yt.publish_date)+"\n"   
        "Views: "+str(yt.views)+"\n"+
        "Format: "+format
    )
    return(yt_video_info)

def submit():
    url = entry.get()
    format = var.get()
    yt = YouTube(url) 
    yt_video_info = ()
    info_window = tk.Toplevel(root)
    info_window.title("Video Info")
    label = tk.Label(info_window, text="Title: "+yt.title+"\n"+
        "Channel: "+yt.author+"\n"+
        "Release: "+str(yt.publish_date)+"\n"   
        "Views: "+str(yt.views)+"\n"+
        "Format: "+format)
    label.pack()
    if format == "MP4":
        yt = YouTube(url) 
        formats = yt.streams.filter(progressive=True, file_extension='mp4')
        video = max(formats, key=lambda x: x.resolution)
        print("Downloading "+yt.title+" as MP4")
        print(path)
        video.download(path)
        print("Finished!")

    if format == "MP3":
        formats = yt.streams.filter(progressive=True, file_extension='mp4')
        video = max(formats, key=lambda x: x.resolution)
        print("Downloading "+yt.title+"...")
        video.download(path)
        mp4_file = path+"/"+video.default_filename
        mp3_file = video.default_filename.replace('.mp4', '.mp3')
        audio = AudioSegment.from_file(path+"/"+video.default_filename, format='mp4')
        print("Convert "+mp4_file+" to mp3...")
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