# import tkinter module
from tkinter import *

from tkinter import messagebox as mbox


root = Tk()
attempts = 3
# ADD Music File
guess = ""


# ==================================================================
def K_game():
    global text
    global attempts
    global guess
    attempts -= 1
    name = ["harsh", "jay", "jayesh"]
    guess = wind.get()
    if guess == "":
        mbox.showerror("Error", "Enter name ")
    elif guess == name[0]:

        text.set("You win")
        button1.pack_forget()
    elif guess == name[1]:
        text.set("you Lose")
        button1.pack_forget()
    else:
        mbox.showerror("Error", "Not valid ")


def K_game():
    global text
    global attempts
    global guess
    attempts -= 1
    name = ["harsh", "jay", "jayesh"]
    name1 = ["Vikas", "Das", "HOG"]
    name2 = ["abdul", "sam", "Fog"]
    guess = wind.get()
    if guess == "":
        mbox.showerror("Error", "Enter name ")
    elif guess == (name[0] or name1[0] or name2[0]):

        text.set("You win")
        button1.pack_forget()
    elif guess == (name[1] or name[2] or name1[1] or name1[2] or name2[1] or name2[2]):
        text.set("you Lose")
        button1.pack_forget()
    else:
        mbox.showerror("Error", "Not valid ")


'''   if attempts == 0:
        text.set("You lose by attempts")
        button1.pack_forget()'''

root.title("The Death Note")
root.iconbitmap(r'death_AD5_icon.ico')
root.geometry("800x500")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

label = Label(root, text="Write The Name", font=("Arial Bold", 10))
label.place(x=290, y=10)
wind = Entry(root, width=20, borderwidth=5, justify="center")
wind.place(x=280, y=50)
button1 = Button(root, text="Eradicate", command=K_game, font=("Arial Bold", 10), cursor="pencil")
button1.place(x=290, y=80)

button2 = Button(root, text="Quit", command=root.destroy, font=("Arial Bold", 10), cursor="pencil")
button2.place(x=370, y=80)


'''photo = PhotoImage(file="rival.gif")
label = Label(root, image=photo)

label.image = photo
label.pack(fill=BOTH)'''

text = StringVar()
text.set("You have 3 attempts")

attempt = Label(root, textvariable=text)
attempt.place(x=290, y=120)
'''
timer = Label(root, text="you have 1 minute")
timer.grid(column=0, row=6, columnspan=6)
tick()
root.after(120000, quit_pro)'''
root.mainloop()

"""
import cv2

cap = cv2.VideoCapture("Kiragotcaught.mp4")
while True:
    ret, frame = cap.read()

    cv2.imshow("Kira", frame)
    if cv2.waitKey(15) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()"""
