from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

root=Tk()
root.title("BMI Calculator")
root.geometry("470x580")
root.resizable(False,False)
root.configure(bg="#f0f1f5")

def BMI():
    h=float(Height.get())
    w=float(Weight.get())

    #convert height into meter
    m=h/100
    bmi=round(float(w/m**2),1)
    label1.config(text=bmi)

    if bmi<=18.5:
        label2.config(text="Underweight!")

    elif bmi>18.5 and bmi<25:
        label2.config(text="Normal!")

    elif bmi>25 and bmi<=29.5:
        label2.config(text="Overweight!")

    else:
        label2.config(text="Obese!")

#icon
image_icon=PhotoImage(file='icon.png')
root.iconphoto(False,image_icon)

#top
top=PhotoImage(file="top.png")
top_image=Label(root,image=top,background="#f0f1f5")
top_image.place(x=-10,y=-10)

#bottom box
Label(root,width=72,height=18,bg="lightblue").pack(side=BOTTOM)

#two boxes
box=PhotoImage(file="box.png")
Label(root,image=box).place(x=20,y=100)
Label(root,image=box).place(x=240,y=100)

#scale
scale=PhotoImage(file="scale.png")
Label(root,image=scale,bg="lightblue").place(x=20,y=310)

#####slider1#####
current_value= tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_changed(event):
    Height.set(get_current_value())

#command to change the color of scale
style= ttk.Style()
style.configure("TScale",background='white')
slider = ttk.Scale(root,from_=0,to=220,orient='horizontal',style='TScale',command=slider_changed,variable=current_value)
slider.place(x=80,y=250)

#####slider2##########

current_value2= tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def slider_changed2(event):
    Weight.set(get_current_value2())

#command to change the color of scale
style2= ttk.Style()
style2.configure("TScale",background='white')
slider2 = ttk.Scale(root,from_=0,to=200,orient='horizontal',style='TScale',command=slider_changed2,variable=current_value2)
slider2.place(x=300,y=250)

#entry box
Button(root,text='Height',width=10, height=2,font='arial 13 bold',bg='white',fg='black').place(x=75,y=120)
Height=StringVar()
Weight=StringVar()
height=Entry(root,textvariable=Height,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)
height.place(x=35,y=160)
Height.set(get_current_value())
Button(root,text='Weight',width=10, height=2,font='arial 13 bold',bg='white',fg='black').place(x=300,y=120)
weight=Entry(root,textvariable=Weight,width=5,font='arial 50',bg="#fff",fg="#000",bd=0,justify=CENTER)
weight.place(x=225,y=160)
Weight.set(get_current_value2())

Button(root,text='View Report',width=15, height=2,font='arial 10 bold',bg='#1f6e68',fg='white',command=BMI).place(x=280,y=340)

label1=Label(root,font="arial 60 bold",bg="lightblue",fg="#fff")
label1.place(x=125,y=305)

label2=Label(root,font="arial 20 bold",bg="lightblue",fg="#3b3a3a")
label2.place(x=160,y=430)

root.mainloop()