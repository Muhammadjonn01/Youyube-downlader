from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def download_video():
    video_url = entry.get()
    save_location = filedialog.askdirectory()
    selected_quality = quality_var.get()

    yt = YouTube(video_url)
    streams = yt.streams.filter(adaptive=True)
    
    selected_stream = streams.filter(res=selected_quality).first()
    if selected_stream:
        selected_stream.download(output_path=save_location)
        label.config(text='Video downloaded successfully!')
    else:
        label.config(text=f'Video with resolution {selected_quality} is not available.')

root = tk.Tk()
root.title('YouTube Video Downloader')
root.geometry('400x200')
root.resizable(False, False)
root.configure(bg='black')

label = tk.Label(root, text='Enter the YouTube video link:', font=('Arial', 12), fg='white', bg='black')
label.pack(pady=10)

entry = tk.Entry(root, width=50, font=('Arial', 12))
entry.pack(pady=5)

quality_var = tk.StringVar()
quality_var.set("720p")  # Default quality selection

quality_dropdown = ttk.Combobox(root, textvariable=quality_var)
quality_dropdown['values'] = ["144p", "240p", "360p", "480p", "720p", "1080p"]
quality_dropdown.pack(pady=5)

btn = tk.Button(root, text='Download', command=download_video, font=('Arial', 12), bg='white', fg='black')
btn.pack(pady=10)

root.mainloop()