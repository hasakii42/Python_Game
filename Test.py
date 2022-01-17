from neww import Game

g = Game()
while g.running:
    g.playing = True

    g.game_loop()
"""
from tkinter import *
import pygame
from tkinter import messagebox as mbox

root = Tk()
my_menu = Menu(root)
root.title("The Death Note")
root.iconbitmap(r'death_AD5_icon.ico')
root.geometry("800x500")
root.config(menu=my_menu)

attempts = 3
file = "Duniyaa.mp3"  # ADD Music File


def game():
    def sub():
        global text
        global attempts
        attempts -= 1
        name = ["harsh", "jay", "jayesh"]
        guess = wind.get()
        if guess == "":
            mbox.showerror("Error", "Enter name ")
        elif guess == name[0]:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            text.set("You win")
            button1.pack_forget()
        elif guess != name:
            mbox.showerror(title="rules", message="Yuo")
        elif attempts == 0:
            text.set("You lose")
            button1.pack_forget()

    filename1 = PhotoImage(file="Back.png")
    background_label = Label(root, image=filename1)
    background_label.pack()

    filename = PhotoImage(file="Kira.png")
    but1 = Button(root, text="Button", image=filename, compound=LEFT)
    but1.place(x=290, y=10)

    filename = PhotoImage(file="L.png")
    but1 = Button(root, text="Button", image=filename, compound=LEFT)
    but1.place(x=290, y=10)

    label = Label(root, text="Write The Name", font=("Arial Bold", 10))
    label.place(x=290, y=10)

    wind = Entry(root, width=20, borderwidth=5, justify="center")
    wind.place(x=280, y=50)

    button1 = Button(root, text="Eradicate", command=sub, font=("Arial Bold", 10), cursor="pencil")
    button1.place(x=290, y=80)

    button2 = Button(root, text="Quit", command=root.destroy, font=("Arial Bold", 10), cursor="pencil")
    button2.place(x=370, y=80)

    text = StringVar()
    text.set("You have 3 attempts")

    attempt = Label(root, textvariable=text)
    attempt.place(x=290, y=120)
    frame.pack()


file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="nem", command=game)
file_menu.add_command(label="Exit", command=root.quit)

frame = Frame(root, width=300, height=300)

root.mainloop"""
