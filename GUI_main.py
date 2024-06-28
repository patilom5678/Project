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
root.title("Predictive Modelling of Drugs")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('img3.jpg')
image2 = image2.resize((1800, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) 


 # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Predictive Modelling of Drugs",font=("Algerian", 35, 'bold'),
                    background="#283593", fg="white", width=55, height=1)
label_l1.place(x=0, y=0)


def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=tk.Canvas(root,bg="#283593")
canvas.pack()
canvas.place(x=0, y=600)
text_var="provide a list of relevant drugs based on the patient's disease conditions "
text=canvas.create_text(0,-2000,text=text_var,font=('Times',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 50
canvas['width']=width
canvas['height']=height
fps=200    #Change the fps to make the animation faster/slower
shift()   #Function Calling





def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Login", command=log, width=17, height=1,font=('times', 20, ' bold '), bg="white", fg="grey")
button1.place(x=400, y=200)

button2 = tk.Button(root, text="Register",command=reg,width=17, height=1,font=('times', 20, ' bold '), bg="white", fg="grey")
button2.place(x=400, y=300)

button3 = tk.Button(root, text="Exit",command=window,width=17, height=1,font=('times', 20, ' bold '), bg="white", fg="grey")
button3.place(x=400, y=400)

root.mainloop()