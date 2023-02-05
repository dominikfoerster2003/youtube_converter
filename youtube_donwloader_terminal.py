from pytube import YouTube
import os
from pydub import AudioSegment
import tarfile
import urllib
import sys

#path2=os.path.dirname(os.path.abspath(__file__))
path2= os.path.expanduser('~\\Downloads')
path= new_string = path2.replace("\\", "/")
install_path= "C:/"

def FFmpegInstallationWindows():
    print("Downloading FFmpeg...")
    url = "http://ubuntuerfurt.zapto.org/ffmpeg/ffmpeg.tar"
    tar_file = install_path+"/ffmpeg.tar"
    urllib.request.urlretrieve(url, install_path+'ffmpeg')
    print("Unzip FFmpeg...")
    print("Installing FFmpeg...")
    with tarfile.open(tar_file) as tar:
        tar.extractall(path=install_path)
    os.remove(install_path+"/ffmpeg.tar")
    
def FFmpegInstallationMacos():
    print("Downloading FFmpeg...")
    os.system("brew install ffmpeg")

if os.name == "nt":
    if os.path.exists(install_path+"/ffmpeg.tar"):
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
    video.download(path)
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

