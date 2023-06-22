import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import time
import ntpath #This is used to extract filename from path
from ftplib import FTP
from tkinter import filedialog
from pathlib import Path
import select
import sys


from playsound import playsound
import pygame
from pygame import mixer

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None

song_counter = 0


def browseFiles():
    global textarea
    global infoLabel

    try:
        filename = filedialog.askopenfilename()
        infoLabel.configure(text=filename)
        HOSTNAME = "127.0.0.1"
        USERNAME = "lftpd"
        PASSWORD = "lftpd"
        ftp_server = FTP(HOSTNAME,USERNAME,PASSWORD)
        ftp_server.encoding("utf-8")
        ftp_server.cwd("shared_files")
        fname = ntpath.basename(filename)
        with open (fname,'rb') as f:
            ftp_server.storbinary(f"STOR {fname}",f)

        ftp_server.dir()
        ftp_server.quit()
    except FileNotFoundError:
        print ("File not found.")



def play():
    global song_selected
    global infoLabel
    
    song_selected = listbox.get(ANCHOR)
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if (song_selected != ""):
        infoLabel.configure(text="Now Playing: "+song_selected)
    else:
        infoLabel.configure (text="")


def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure (text="")


def resume ():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()   


def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()



def musicWindow():

   
    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("300x330")
    window.configure(bg='LightSkyBlue')

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel
    global song_counter
    global infoLabel

    selectlabel = Label(window, text= "Select Song", bg='LightSkyBlue', font = ("Calibri",8))
    selectlabel.place(x=2, y=1)

    listbox = Listbox(window, height=10,width = 39, activestyle = "dotbox",bg='LightSkyBlue',borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10,y=18)

    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter = song_counter + 1




     

    ResumeButton = Button(window, text="Resume", width=10,bd=1,bg='SkyBlue',font = ("Calibri",10), command= resume)
    ResumeButton.place(x=30, y=250)

    PauseButton = Button(window, text="Pause", width=10,bd=1,bg='SkyBlue',font = ("Calibri",10), command= pause)
    PauseButton.place(x=200,y=250)




    scrollbarl = Scrollbar(listbox)
    scrollbarl.place(relheight=1, relx=1) 
    scrollbarl.config(command=listbox.yview)

    PlayButton = Button(window, text="Play", width=10, bd=1,bg="SkyBlue",font=("Calibri",10), command= play)
    PlayButton.place(x=30,y=200)

    Stop = Button(window, text="Stop",bd=1,width=10,bg="SkyBlue", font=("Calibri",10), command= stop)
    Stop.place(x=200,y=200)

    Upload = Button(window, text="Upload",width=10, bd=1,bg='SkyBlue', font=("Calibri", 10), command=browseFiles)
    Upload.place(x=30,y=290)

    Download = Button(window, text="Download",width=10,bd=1,bg='SkyBlue', font=("Calibri",10))
    Download.place(x=200,y=290)

    infoLabel = Label(window, text="", fg="blue", font=("Calibri",8))
    infoLabel.place (x=4, y=280)
    
    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    musicWindow()

setup()