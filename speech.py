''' Copyrights Reserved with
Ashutosh Kapoor STUDENT OF BBDEC LKO 2021-2025 BATCH'''
import os
import tkinter
from tkinter import *
from tkinter import Tk,PhotoImage
from tkinter import filedialog
import speech_recognition as sr
from moviepy.editor import concatenate_videoclips, VideoFileClip
from pydub import AudioSegment
from googletrans import Translator
win = Tk()
win.title("TEXT/AUDIO TO SIGN LANGUAGE")
win.geometry("1920x1080")
win.configure(bg="#FEF6B8")
win.resizable(True, True)
image=PhotoImage(file="IMAGE2.png")
lable=tkinter.Label(win,image=image,border=0)

lable.pack()
label=tkinter.Label(win,text="PLEASE USE HINDI OR ENGLISH LANGUAGE ONLY",font=("Goudy Old Style",15,'bold'),bg="#FEF6B8",fg="#C43125")
label.pack()
def conv1(t):
    ''' CHOOSE SIGN AND MERGE ITS VIDEO ACCORDING TO SENTENCE AND PLAY IT
    I HAVE WRITTEN THE ALGORITHM BUT NOT PROVIDED IT'''
                


    else:
        if len(clips) != 0:
            f = concatenate_videoclips(clips, method="compose")
            f.write_videofile("meged.mp4")
            video_path=r"D:\ISL\meged.mp4"
            os.system(video_path)
def speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        ad = r.record(source, duration=5)
    try:
        txt = r.recognize_google(ad)
        translator=Translator()
        trans=translator.translate(txt,src='hi',dest='en')
        result.insert(END, "Recognized Text...\n")
        result.insert(END, txt, END)
        conv1(trans.text)
    except:
        result.insert(END,"\nUNABLE TO RECOGNIZE",END)
def audio():
    ad = filedialog.askopenfilenames(initialdir="Music/", title="Choose an audio", filetypes=(("mp3 file", "*.mp3"), ("wav files", "*.wav"), ("aiff files", "*.aiff" or "*aif"), ("aiff-c files", "*aifc"),("flac files", "*.flac"), ("m4a files", "*.m4a"),))
    aud=""
    for item in ad:
        aud=aud+item
    tst = "test.wav"
    sound = AudioSegment.from_file(aud)
    sound.export(tst, format="wav")
    r = sr.Recognizer()
    with sr.AudioFile(tst) as source:
        ad = r.record(source)
        txt = r.recognize_google(ad)
    try:
        translator = Translator()
        trans = translator.translate(txt, src='hi', dest='en')
        result.insert(END, "Recognized Text...\n")
        result.insert(END, txt, END)
        conv1(trans.text)
    except:
        result.insert(END,"\nUNABLE TO RECOGNIZE",END)
def text():
    global entry
    txt=entry.get()
    translator = Translator()
    trans = translator.translate(txt, src='hi', dest='en')
    conv1(trans.text)
entry = Entry(win,width=100,bg="white",fg="#C43125",font=("Goudy Old Style",12))
entry.configure()
entry.focus_set()
entry.pack()
b1= tkinter.Button(win,text="CONVERT",bg="#ED1C24",fg="white",font=("Goudy Old Style",10),width=20,command=text).pack()
b2=tkinter.Button(win,text="CHOOSE AUDIO FILE",bg="#ED1C24",fg="white",font=("Goudy Old Style",10),width=20,command=audio).pack(pady=10)
b3=tkinter.Button(win,text="SPEECH",bg="#ED1C24",fg="white",font=("Goudy Old Style",10),width=20,command=speak).pack()
result = Text(height=6,bg="#FEF6B8",fg="#C43125",border=0,font=("Goudy Old Style",10))
result.pack()
win.mainloop()
