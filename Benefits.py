# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:10:41 2024

@author: admin
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms

##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Gear Deffected System")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('bg_for_all.png')
image2 = image2.resize((1360, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) 


 # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Benefits of yoga ",font=("Algerian", 35, 'bold'),
                    background="white", fg="black", width=50, height=1)
label_l1.place(x=0, y=10)

image2 = Image.open('Sarvangasana.png')
image2 = image2.resize((260, 260), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=60, y=100)


label_l1 = tk.Label(root, text="Sarvangasana",font=("Times New Roman", 18),
                    background="white", fg="black", width=20, height=1)
label_l1.place(x=60, y=350)


image2 = Image.open('Sirsasana.png')
image2 = image2.resize((260, 260), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=500, y=100)


label_l1 = tk.Label(root, text="Sirsasana",font=("Times New Roman", 18),
                    background="white", fg="black", width=20, height=1)
label_l1.place(x=500, y=350)

image2 = Image.open('Utthita Trikonasana.png')
image2 = image2.resize((260, 260), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=970, y=100)


label_l1 = tk.Label(root, text="Utthita Trikonasana",font=("Times New Roman", 18),
                    background="white", fg="black", width=20, height=1)
label_l1.place(x=970, y=350)

image2 = Image.open('Chaturanga Dandasana.png')
image2 = image2.resize((260, 260), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=60, y=400)


label_l1 = tk.Label(root, text="Chaturanga Dandasana",font=("Times New Roman", 18),
                    background="white", fg="black", width=20, height=1)
label_l1.place(x=60, y=650)


image2 = Image.open('Crescent Lunge.png')
image2 = image2.resize((260, 260), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=500, y=400)


label_l1 = tk.Label(root, text="Crescent Lunge",font=("Times New Roman", 18),
                    background="white", fg="black", width=20, height=1)
label_l1.place(x=500, y=650)


image2 = Image.open('malasana.png')
image2 = image2.resize((260, 260), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=970, y=400)


label_l1 = tk.Label(root, text="malasana",font=("Times New Roman", 18),
                    background="white", fg="black", width=20, height=1)
label_l1.place(x=970, y=650)


#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])


def log():
    from subprocess import call
    call(["python","GUI_main.py"])
    
def window():
  root.destroy()




button3 = tk.Button(root, text="GUI_main",command=log,width=12, height=1,font=('times', 10, ' bold '), bg="#A9CCE3", fg="white")
button3.place(x=1200, y=30)

root.mainloop()