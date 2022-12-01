from tkinter import *
from tkinter.ttk import *
import time
import random
from tkinter import messagebox
import jarvis

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        rand = random.randint(0, 2)
        time.sleep(rand)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" < Completed.")
        if download == 100:
            print("Installation Complete.")
            messagebox.showinfo("Installation Complete.", "Installation Complete.")
            time.sleep(2)
            window.destroy()
            jarvis.StartJarvis()
            
        else:
            print("%" + download)
            
        window.update_idletasks()

window = Tk()
window.geometry("400x150")
window.title("Jarvis - INSTALL")

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="Start installation",command=start, width="20").pack()

window.mainloop()