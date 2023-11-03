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
    t = t.lower()
    t = t.split(" ")
    clips=[]
    i = 0
    while i < (len(t)):
        s = t[i]
        s = s.capitalize()
        j = len(s)
        bp = "D:\\ISL\\"
        vido = len(clips)
        for x in range(j, 2, -1):
            p = os.path.join(bp, s[0], s[0], s[0:x] + ".mp4")
            pa = os.path.join(bp, s[0], s[0], s[0:x] + ".mpg")
            if os.path.exists(p):
                vid = VideoFileClip(p)
                vid = vid.without_audio()
                clips.append(vid)
                for k in range(2, 6):
                    p1 = os.path.join(bp, s[0], s[0], s[0:x] + "_(Sign_" + str(k) + ").mp4")
                    p2 = os.path.join(bp, s[0], s[0], s[0:x] + "_(Sign_" + str(k) + ").mpg")
                    if os.path.exists(p1):
                        vid = VideoFileClip(p1)
                        vid = vid.without_audio()
                        clips.append(vid)
                    elif os.path.exists(p2):
                        vid = VideoFileClip(p2)
                        vid = vid.without_audio()
                        clips.append(vid)
                    else:
                        break
                    break
                break
            elif os.path.exists(pa):
                vid = VideoFileClip(pa)
                vid = vid.without_audio()
                clips.append(vid)
                for k in range(2, 6):
                    p1 = os.path.join(bp, s[0], s[0], s[0:x] + "_(Sign_" + str(k) + ").mp4")
                    p2 = os.path.join(bp, s[0], s[0], s[0:x] + "_(Sign_" + str(k) + ").mpg")
                    if os.path.exists(p1):
                        vid = VideoFileClip(p1)
                        vid = vid.without_audio()
                        clips.append(vid)
                    elif os.path.exists(p2):
                        vid = VideoFileClip(p2)
                        vid = vid.without_audio()
                        clips.append(vid)
                    else:
                        break
                    break
                break
            else:
                l = ["ly", "ward", "ways", "wise", "able", "ac", "acity", "ocity", "ade", "age", "aholic", "oholic",
                     "al", "algia", "an", "ian", "ance", "ant", "ar", "ard", "arian", "arium", "orium", "ary",
                     "ate", "ation", "ative", "cide", "cracy", "crat", "cule", "cy", "cycle", "dom", "dox",
                     "ectomy", "ed", "ee", "eer", "emia", "en", "ence", "ency", "ent", "er", "ern", "escence",
                     "ese", "esque", "ess", "est", "etic", "ette", "ful", "fy", "gam", "gamy", "gon", "gonic",
                     "hood", "ial", "iasis", "iatric", "ible", "ic", "ical", "ile", "ily", "ine", "ing", "ion",
                     "ious", "ish", "ist", "ite", "itis", "ity", "ive", "ization", "ize", "less", "let", "like",
                     "ling", "loger", "logist", "log", "ly", "ment", "ness", "oid", "ology", "oma", "onym", "opia",
                     "opsy", "or", "ory", "osis", "ostomy", "otomy", "ous", "path", "pathy", "phile", "phobia",
                     "phone", "phyte", "plegia", "plegic", "pnea", "scopy", "scope", "scribe", "script", "sect",
                     "ship", "sion", "some", "sophy", "sophic", "th", "thing", "tome", "tomy", "trophy", "tude",
                     "ty", "ular", "uous", "ure", "ward", "ware", "y","e","s"]
                for z in range(len(l)):
                    p = os.path.join(bp, s[0], s[0], s[0:x] + l[z] + ".mp4")
                    pa = os.path.join(bp, s[0], s[0], s[0:x] + l[z] + ".mpg")
                    if os.path.exists(p):
                        vid = VideoFileClip(p)
                        vid = vid.without_audio()
                        clips.append(vid)
                        for k in range(2, 6):
                            p1 = os.path.join(bp, s[0], s[0], s[0:x] + l[z] + "_(Sign_" + str(k) + ").mp4")
                            p2 = os.path.join(bp, s[0], s[0], s[0:x] + l[z] + "_(Sign_" + str(k) + ").mpg")
                            if os.path.exists(p1):
                                vid = VideoFileClip(p1)
                                vid = vid.without_audio()
                                clips.append(vid)
                            elif os.path.exists(p2):
                                vid = VideoFileClip(p2)
                                vid = vid.without_audio()
                                clips.append(vid)
                            else:
                                break
                            break
                        break
                    elif os.path.exists(pa):
                        vid = VideoFileClip(pa)
                        vid = vid.without_audio()
                        clips.append(vid)
                        for k in range(2, 6):
                            p1 = os.path.join(bp, s[0], s[0], s[0:x] + l[z] + "_(Sign_" + str(k) + ").mp4")
                            p2 = os.path.join(bp, s[0], s[0], s[0:x] + l[z] + "_(Sign_" + str(k) + ").mpg")
                            if os.path.exists(p1):
                                vid = VideoFileClip(p1)
                                vid = vid.without_audio()
                                clips.append(vid)
                            elif os.path.exists(p2):
                                vid = VideoFileClip(p2)
                                vid = vid.without_audio()
                                clips.append(vid)
                            else:
                                break
                            break
                        break
                    else:
                        if vido < len(clips):
                            break
                        else:
                            z += 1
        if vido < len(clips):
            i += 1
        else:
            p = os.path.join(bp, s[0], s[0], s + ".mp4")
            pa = os.path.join(bp, s[0], s[0], s + ".mpg")
            if os.path.exists(p):
                vid = VideoFileClip(p)
                vid = vid.without_audio()
                clips.append(vid)
                for k in range(2, 6):
                    p1 = os.path.join(bp, s[0], s[0], s + "_(Sign_" + str(k) + ").mp4")
                    p2 = os.path.join(bp, s[0], s[0], s + "_(Sign_" + str(k) + ").mpg")
                    if os.path.exists(p1):
                        vid = VideoFileClip(p1)
                        vid = vid.without_audio()
                        clips.append(vid)
                    elif os.path.exists(p2):
                        vid = VideoFileClip(p2)
                        vid = vid.without_audio()
                        clips.append(vid)
                    else:
                        break
            elif os.path.exists(pa):
                vid = VideoFileClip(pa)
                vid = vid.without_audio()
                clips.append(vid)
                for k in range(2, 6):
                    p1 = os.path.join(bp, s[0], s[0], s + "_(Sign_" + str(k) + ").mp4")
                    p2 = os.path.join(bp, s[0], s[0], s + "_(Sign_" + str(k) + ").mpg")
                    if os.path.exists(p1):
                        vid = VideoFileClip(p1)
                        vid = vid.without_audio()
                        clips.append(vid)
                    elif os.path.exists(p2):
                        vid = VideoFileClip(p2)
                        vid = vid.without_audio()
                        clips.append(vid)
                    else:
                        break
            else:
                s = s.upper()
                for z in s:
                    if z in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        p = os.path.join(bp, "Alphabets", z + ".mp4")
                        vid = VideoFileClip(p)
                        vid = vid.without_audio()
                        clips.append(vid)
                    elif z in "0123456789":
                        p = os.path.join(bp, "Numbers", "Numbers", z + ".mp4")
                        vid = VideoFileClip(p)
                        vid = vid.without_audio()
                        clips.append(vid)
                    else:
                        clips = clips
            i += 1


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
