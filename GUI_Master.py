from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,roc_curve
root = tk.Tk()
root.title("Predictive Modelling of Drugs")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open('img8.jpeg')

image2 = image2.resize((1380, 700), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image



background_label.place(x=0, y=40)  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Predictive Modelling of Drugs", font=('times', 35,' bold '), height=1, width=55,bg="#D1F2EB",fg="black")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++



def Data_Preprocessing():
    data = pd.read_csv("new_file2.csv",encoding='latin-1')
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['Age'] = le.fit_transform(data['Age'])
    data['Gender'] = le.fit_transform(data['Gender'])
    data['Symptoms'] = le.fit_transform(data['Symptoms'])
    data['Diseases'] = le.fit_transform(data['Diseases'])
   

    """Feature Selection => Manual"""
    x = data.drop(['Drugs'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Drugs']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="#D1F2EB",
                    foreground="black", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=200, y=80)


def Model_Training():
    data = pd.read_csv("new_file2.csv", encoding='latin-1')
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    data['Age'] = le.fit_transform(data['Age'])
    data['Gender'] = le.fit_transform(data['Gender'])
    data['Symptoms'] = le.fit_transform(data['Symptoms'])
    data['Diseases'] = le.fit_transform(data['Diseases'])
  

    """Feature Selection => Manual"""
    x = data.drop(['Drugs'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Drugs']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=123)

    
    from sklearn.naive_bayes import GaussianNB
    nb_classifier = GaussianNB()
    nb_classifier.fit(x_train, y_train)

    y_pred = nb_classifier.predict(x_test)
    print(y_pred)
    

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
    
    
    
    label4 = tk.Label(root,text =str(repo),width=120,height=30,bg='#D1F2EB',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as new2.joblib",width=65,height=2,bg='#D1F2EB',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=445)
    from joblib import dump
    dump (nb_classifier,"new2.joblib")
    print("Model saved as new2.joblib")



def call_file():
   from subprocess import call
   call(["python","prediction_ya.py"])

def Benefits():
   from subprocess import call
   call(["python","Benefits.py"])
   

def window():
    root.destroy()

button2 = tk.Button(root, foreground="black", background="#D1F2EB", font=("Tempus Sans ITC", 14, "bold"),
                    text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
button2.place(x=5, y=90)

button3 = tk.Button(root, foreground="black", background="#D1F2EB", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model Training", command=Model_Training, width=15, height=2)
button3.place(x=5, y=170)

button4 = tk.Button(root, foreground="black", background="#D1F2EB", font=("Tempus Sans ITC", 14, "bold"),
                    text="Recommend Drugs", command=call_file, width=15, height=2)
button4.place(x=5, y=250)

button4 = tk.Button(root, foreground="black", background="#D1F2EB", font=("Tempus Sans ITC", 14, "bold"),
                    text="Benefits", command=Benefits, width=15, height=2)
button4.place(x=5, y=330)


exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="#48C9B0",fg="#D1F2EB")
exit.place(x=5, y=430)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''