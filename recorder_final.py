import sounddevice
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo,showwarning
from tkinter.filedialog import askdirectory

add=""

def file_path():
    global add
    add = askdirectory()
    print(add)
    
def save_file():
    try:
       time = int(sec.get())
       addr=add+"/"+"record_file.wav"
       showinfo(title="Start",message="Recording Start")
       rec=sounddevice.rec((time*44100),samplerate=44100,channels=2)
       sounddevice.wait()
       write(addr,44100,rec)
       showinfo(title="End",message="Recording Stop")
    except:
        showwarning(title="Time",message="Wrong format time")

def main_window():
    global sec
    win = Tk()
    win.geometry("500x350")
    win.resizable(True,True)
    win.title("Voice recorder")
    win.config(bg="black")
    
    
    img1 = PhotoImage(file="Signal.png")
    l1 = Label(win,image=img1)
    l1.place(x=75,y=20,height=90,width=350)
    
    sec = Entry(win,font=(20))
    sec.place(x=150,y=150,height=30,width=170)
    
    l2 = Label(win,text="Enter time in sec", font=("Bold",10),bg="white")
    l2.place(x=180,y=195,height=20,width=110)
    
    b = Button(win,text="Path",font=("Time New Roman",15),command=file_path)
    b.place(x=325,y=151,height=30,width=50)
    
    img2 = PhotoImage(file="mic.png")
    start=Button(win,image=img2,command=save_file)
    start.place(x=195,y=230,height=80,width=80)
    
    
    win.mainloop()
    
main_window()
