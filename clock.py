
from tkinter import *
import time
clk=Tk()
clk.title("clock")
clk.geometry("1350x700+0+0")
clk.config(bg="grey")

def clock():
    current_time = time.localtime()
    hr = int(current_time.tm_hour)  # Convert hr to an integer
    mn = int(current_time.tm_min)    # Convert mn to an integer
    sc = int(current_time.tm_sec)    # Convert sc to an integer

    # Update the time labels
    lb_hr.config(text=str(hr).zfill(2))
    lb_mn.config(text=str(mn).zfill(2))
    lb_sec.config(text=str(sc).zfill(2))

    if hr >= 12:
        lb_dm.config(text="PM")
    else:
        lb_dm.config(text="AM")

    # Schedule the function to run again after 1000 milliseconds (1 second)
    lb_hr.after(1000, clock)


lb_hr =Label(clk,text = "12" , font = ("Times 20 bold",75, "bold"),bg = "white",fg ="black")
lb_hr.place(x=350,y=200, width =150, height =150)

lb_hr_txt= Label(clk, text= "HOUR",font =("Times 20 bold",20,"bold"),bg ="black",fg="white")
lb_hr_txt.place(x=350, y=360, width=150, height=50)


lb_mn = Label(clk, text= "12" , font = ("Times 20 bold",75, "bold"),bg = "white",fg ="black")
lb_mn.place(x=520,y=200, width =150, height =150)

lb_mn_txt= Label(clk, text= "MINUTE",font =("Times 20 bold",20,"bold"),bg ="black",fg="white")
lb_mn_txt.place(x=520, y=360, width =150, height =50)


lb_sec = Label(clk,text = "12" , font = ("Times 20 bold",75, "bold"),bg = "white",fg ="black")
lb_sec.place(x=690,y=200, width =150, height =150)

lb_sec_txt= Label(clk, text= "SECONDS",font =("Times 20 bold",20,"bold"),bg ="black",fg="white")
lb_sec_txt.place(x=690, y=360, width =150, height =50)


lb_dm = Label(clk,text = "AM" , font = ("Times 20 bold",70, "bold"),bg = "#9F0646",fg ="white")
lb_dm.place(x=860,y=200, width =150, height =150)

lb_dm_txt= Label(clk, text= "NOON",font =("Times 20 bold",20,"bold"),bg ="#9F0646",fg="white")
lb_dm_txt.place(x=860, y=360, width =150, height =50)

clock()
clk.mainloop()