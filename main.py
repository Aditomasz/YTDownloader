import os
import pafy

import tkinter as tk

master_window = tk.Tk()
master_window.geometry("300x300")
master_window.title("Sky YT Downloader 1.0")

music_folder = os.path.expanduser("~")+"/Music/"
video_folder = os.path.expanduser("~")+"/Videos/"

def print_data():
    print(string_variable.get())


def downloadVideo():
    video = pafy.new(string_variable.get())
    best = video.getbest()
    best.download(video_folder)


def downloadAudio():
    video = pafy.new(string_variable.get())
    best_audio = video.getbestaudio()
    best_audio.download(music_folder)


string_variable = tk.StringVar(master_window)

label = tk.Label(master_window, text="Enter Link: ")
label.grid(row=0, column=0)

entry = tk.Entry(master_window, textvariable=string_variable)
entry.grid(row=0, column=1)

b1 = tk.Button(master_window, text="Print data", command=print_data)
b1.grid(row=1, column=0, columnspan=2)

b2 = tk.Button(master_window, text="Download Video", command=downloadVideo)
b2.grid(row=2, column=0, columnspan=2)

b3 = tk.Button(master_window, text="Download Audio", command=downloadAudio)
b3.grid(row=3, column=0, columnspan=2)

master_window.mainloop()
