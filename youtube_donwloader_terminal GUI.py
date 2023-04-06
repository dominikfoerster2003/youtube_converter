from pytube import YouTube
import os
from pydub import AudioSegment
import tarfile
import urllib
import sys
import progressbar
from tkinter import messagebox as tkm
from tkinter import ttk
import tkinter as tk



path2= os.path.expanduser('~\\Downloads')
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
    tar_file = install_path+"/ffmpeg.tar"
    urllib.request.urlretrieve(url, install_path+'ffmpeg', show_progress)
    print("Unzip FFmpeg...")
    print("Installing FFmpeg...")
    with tarfile.open(tar_file) as tar:
        tar.extractall(path=install_path)
    os.remove(install_path+"/ffmpeg.tar")
    
def FFmpegInstallationMacos():
    print("Downloading FFmpeg...")
    os.system("brew install ffmpeg")

if os.name == "nt":
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
    

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Youtube Downloader")

        self.url_label = tk.Label(master, text="Youtube URL:")
        self.url_label.grid(row=0, column=0)

        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.grid(row=0, column=1)
        
        self.format_label_text = tk.Label(master, text="Format: ")
        self.format_label_text.grid(row=1, column=0)

        self.format_label = tk.Entry(ttk.Combobox(master, values=[
            'mp3',
            'mp4'
        ])row=1,column=1)
        self.format_label.grid(row=1, column=0)

        #self.format_entry = tk.Entry(master, width=50)
        #self.format_entry.grid(row=1, column=1)

        self.download_button = tk.Button(master, text="Download", command=self.download)
        self.download_button.grid(row=2, column=1)

    def download(self):
        url = self.url_entry.get()
        format = self.format_entry.get()

        yt = YouTube(url)

        if format == "mp3":
            self.download_video_as_mp3(yt)
        elif format == "mp4":
            self.download_video_as_mp4(yt)
        else:
            print("Invalid format")
            
    def download_video_as_mp4(self, yt):
        formats = yt.streams.filter(progressive=True, file_extension='mp4')
        video = max(formats, key=lambda x: x.resolution)
        file_path = os.path.expanduser('~\\Downloads')
        print("Downloading "+yt.title+" as MP4")
        video.download(file_path)
        tkm.showinfo(title="Download complete", message="Video saved in "+file_path)

    def download_video_as_mp3(self, yt):
        formats = yt.streams.filter(progressive=True, file_extension='mp4')
        video = max(formats, key=lambda x: x.resolution)
        file_path = os.path.expanduser('~\\Downloads')
        print("Downloading "+yt.title+"...")
        video.download(file_path)
        mp4_file = file_path+"/"+video.default_filename
        mp3_file = video.default_filename.replace('.mp4', '.mp3')
        audio = AudioSegment.from_file(file_path+"/"+video.default_filename, format='mp4')
        print("Converting "+mp4_file+" to mp3...")
        audio.export(file_path+"/"+mp3_file, format='mp3')
        os.remove(mp4_file)
        tkm.showinfo(title="Download complete", message="Audio saved in "+file_path)


root = tk.Tk()
gui = GUI(root)
root.mainloop()