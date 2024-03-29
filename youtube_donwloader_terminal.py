from pytube import YouTube
import os
from pydub import AudioSegment
import tarfile
import urllib
import sys
import progressbar
import urllib.request
import py7zr

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
    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z"
    zip_file = install_path + "ffmpeg.7z"
    urllib.request.urlretrieve(url, zip_file, show_progress)
    print("Unzipping FFmpeg...")
    with py7zr.SevenZipFile(zip_file, mode='r') as z:
        z.extractall(install_path)
    os.remove(zip_file)
    
def FFmpegInstallationMacos():
    print("Downloading FFmpeg...")
    os.system("brew install ffmpeg")

if os.name == "nt":
    AudioSegment.ffmpeg = "C:/FFmpeg/bin/ffmpeg.exe"
    if os.path.exists(install_path+"/ffmpeg"):
        print("")
    else:
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
    
print('Path:'+path+'\n Wanna change it ? (y/n)')
change_path = input()

if change_path == "y" and "Y":
    ChangePath()

     

print("Youtube URl:")
url= input()
yt = YouTube(url)
format=""

while (format!="mp3") and (format!="mp4"):
    print("Choose Format(mp4/mp3): ")
    format = input()
    



def DownloadVideoAsMp4():
    formats = yt.streams.filter(progressive=True, file_extension='mp4')
    video = max(formats, key=lambda x: x.resolution)
    print("Downloading "+yt.title+" as MP4")
    print(path)
    video.download(path, show_progress)
    print("Finished!")

def DownloadVideoAsMp3(): 
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


def VideoInfo():
    yt_video_info = (
        "Title: "+yt.title+"\n"+
        "Channel: "+yt.author+"\n"+
        "Release: "+str(yt.publish_date)+"\n"   
        "Views: "+str(yt.views)+"\n"+
        "Format: "+format
    )
    print(yt_video_info)

VideoInfo()
print('Confirm Download ? (y/n)')
answer = input()

if answer == "y" and "Y":
    if format == "mp3":
        DownloadVideoAsMp3()
    if format == "mp4":
        DownloadVideoAsMp4()
else:
    print('Canceled!')
    exit
    
print("File saved in "+path)
print("Press a button to exit...")
input()

