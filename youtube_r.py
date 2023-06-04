import os
import subprocess
from tkinter import StringVar, Entry, Tk, END, Label, Button
# from tkinter import *
from pytube import YouTube
from PIL import ImageTk, Image

root = Tk()
root.geometry('600x130')
root.title("Скачать видео с YouTube")
root["bg"] = "#3c3f41"
link = StringVar()
entry_text = "Вставьте ссылку на видео"
link_enter = Entry(root, width=44, textvariable=link)
link_enter.place(x=20, y=20)
root.resizable(False, False)  # Запретить изменение размера окна

youtube_logo = Image.open("youtube_logo.png")
youtube_logo = youtube_logo.resize((50, 50))
youtube_logo = ImageTk.PhotoImage(youtube_logo)
logo_label = Label(root, image=youtube_logo, bg=root["bg"])
logo_label.place(x=500, y=65)


def on_entry_click(event):
    if link_enter.get() == entry_text:
        link_enter.delete(0, END)
        link_enter.configure(fg="black")


def on_entry_leave(event):
    if link_enter.get() == '':
        link_enter.insert(0, entry_text)
        link_enter.configure(fg="gray")


link_enter.insert(0, entry_text)
link_enter.configure(fg="gray")
link_enter.bind('<FocusIn>', on_entry_click)
link_enter.bind('<FocusOut>', on_entry_leave)


def YouTubeDownloader():
    if link.get() != "" and link.get() != entry_text:
        url = YouTube(str(link.get()))
        video = url.streams.get_highest_resolution()
        video.download()
        file_path = os.path.join(os.getcwd())  # , video.default_filename)
        file_size = os.path.getsize(file_path)
        quality = f"{video.resolution} ({video.mime_type})"
        text_info = 'arial 10'
        Label(root, text=f'Видео скачено: {file_path}', font=text_info, bg="#D55B06", fg="white").place(x=20, y=60)
        Label(root, text=f'Размер файла: {file_size / 1000} Мб', font=text_info, bg=root["bg"], fg="white").place(x=20, y=80)
        Label(root, text=f'Качество видео: {quality}', font=text_info, bg=root["bg"], fg="white").place(x=20, y=100)
        subprocess.call(["xdg-open", file_path])
    else:
        Label(root, text='Cсылка пуста!', font='arial 10', bg=root["bg"], fg="red").place(x=20, y=60)


text_button = 'arial 12 bold'
clear_button = Button(root, text='Очистить', font=text_button, bg='white', fg="black", command=lambda: link.set('')).place(x=380, y=20)
Button(root, text='Скачать', font=text_button, bg='white', fg="black", command=YouTubeDownloader).place(x=486, y=20)

root.mainloop()
