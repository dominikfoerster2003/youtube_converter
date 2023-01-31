from pytube import YouTube
from tkinter import *
import tkinter as tk

def yt_link():
    input_link = input_field.get()
    print(input_link)

def mp3():
    mp3 = True
    mp4 = False

def mp4():
    mp4 = True 
    mp3 = False



root = tk.Tk()
root.title("Youtube Converter")
root.geometry('550x200')


label = tk.Label(root, text="Enter Youtube URL: ")
label.pack()

input_field = tk.Entry(root, width=150)
input_field.pack()

label = tk.Label(root, text="Choose Format: ")
label.pack()

mp3_button = tk.Button(root, text="mp3", command=mp3)
mp3_button.pack()

mp4_button = tk.Button(root, text="mp4", command=mp4)
mp4_button.pack()

confirm_button = tk.Button(root, text="confirm",command=yt_link)

root.mainloop()