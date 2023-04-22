from tkinter import *
from pytube import YouTube

screen = Tk()
screen.title("YT video Downloader")
screen.geometry("800x800")
f = "arial 15 bold"


Label(screen, text = "Video YT downloader" , font= f).pack()
Label(screen , text = "Enter link here " , font= f).pack()
link = StringVar()
enter_link = Entry(screen , width= 45 , textvariable=link).pack()




def Downloader():
    Label(screen , text="Downloading" , font=f).pack()
    yt = YouTube(str(link.get()))
    video = yt.streams.get_highest_resolution()
    video.download()
    Label(screen , text = "Download succesful"  , font=f).pack()

Button(screen , font=f , text = "Download",command=Downloader , padx= 2 , width=30  ).place(x=220, y=180)
screen.mainloop()
