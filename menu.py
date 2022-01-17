#===========================TEST CODE ==============================================

from tkinter import *
import pygame
from tkinter import messagebox as mbox
import cv2


root = Tk()
root.geometry("900x500")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

attempts = 3
root.title("The Death Note")
root.iconbitmap(r'death_AD5_icon.ico')

file_T = "Deathnote theme.mp3"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file_T)
pygame.mixer.music.play()
def play():
    file3 = "Deathnote theme.mp3"
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file3)
    pygame.mixer.music.play()


def play1():
    file1 = "ThemeL.mp3"
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file1)
    pygame.mixer.music.play()

def play2():
    file2 = "KIRAtheme.mp3"
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file2)
    pygame.mixer.music.play()

def game_K():
    global text_1
    global attempts
    attempts -= 1
    name = ["Michel", "LindL", "Mello"]
    name1 = ["Samuel", "Ryuzaki", "Saitama"]
    name2 = ["Richard", "Light", "Genos"]
    guess1 = wind1.get()
    if guess1 == "":
        mbox.showerror("Error", "Enter name ")
    elif guess1 == name1[0] or guess1 == name[0] or guess1 == name2[0]:
        if guess1 == name[0]:

            cap = cv2.VideoCapture("V1Criminal 2 dies.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("Criminal 1 died")
            button1.pack_forget()
        elif guess1 == name1[0]:

            cap = cv2.VideoCapture("V2Criminal1 dies.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("Criminal 2 died")
            button1.pack_forget()
        elif guess1 == name2[0]:

            cap = cv2.VideoCapture("V3Ldied.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("L died you won")
            button1.pack_forget()
    elif guess1 == name[1] or guess1 == name[2] or guess1 == name1[1] or guess1 == name1[2] \
            or guess1 == name2[1] or guess1 == name2[2]:
        if guess1 == name[1] or guess1 == name[2]:

            cap = cv2.VideoCapture("V5LtricksKira.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("L tricked you now he knows you location")
            button1.pack_forget()
        elif guess1 == name1[1] or guess1 == name1[2]:
            cap = cv2.VideoCapture("V6Lgetsthebook.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("L got the notebook")
            button1.pack_forget()
        elif guess1 == name2[1] or guess1 == name2[2]:

            cap = cv2.VideoCapture("V7KIRAdied.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("You died")
            button1.pack_forget()
    else:
        mbox.showerror("Error", "Criminal image should be present")


def game_L():
    global text
    global attempts
    attempts -= 1
    names = ["Michel", "LindL", "Mello"]
    names1 = ["Samuel", "Ryuzaki", "Saitama"]
    names2 = ["Richard", "Light", "Genos"]
    guess = wind.get()
    if guess == "":
        mbox.showerror("Error", "Enter name ")
    elif guess == names[0] or guess == names2[0] or guess == names1[0]:
        if guess == names[0]:

            cap = cv2.VideoCapture("V5LtricksKira.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("You Tricked Kira He is in japan")
            button1.pack_forget()
        elif guess == names1[0]:

            cap = cv2.VideoCapture("V6Lgetsthebook.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("This the death note which kills the person name written in it")
            button1.pack_forget()
        elif guess == names2[0]:

            cap = cv2.VideoCapture("V7KIRAdied.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("KIRA died you won")
            button1.pack_forget()
    elif guess == names[1] or guess == names[2] or guess == names1[1] or guess == names1[2] \
            or guess == names2[1] or guess == names2[2]:
        if guess == names[1] or guess == names[2]:

            cap = cv2.VideoCapture("V5LtricksKira.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("L tricked you now he knows you location")
            button1.pack_forget()
        elif guess == names1[1] or guess == names1[2]:
            cap = cv2.VideoCapture("V6Lgetsthebook.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("L got the notebook")
            button1.pack_forget()
        elif guess == names2[1] or guess == names2[2]:

            cap = cv2.VideoCapture("V7KIRAdied.mp4")
            while True:
                ret, frame_1 = cap.read()

                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_1.set("You died")
            button1.pack_forget()
    else:
        mbox.showerror("Error", "Criminal image should be present")




def show_frame(frame):
    frame.tkraise()



frame1 = Frame(root)
frame2 = Frame(root,background="Black")
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)

for frame in (frame1, frame2, frame3, frame4, frame5,):
    frame.grid(row=0, column=0, sticky="nsew")




'''Frame one'''''
photo = PhotoImage(file="Back2.png")
label = Label(frame1, image=photo)
label.image = photo
label.pack(fill=BOTH)

frame1_btn = Button(frame1, text="Start", width=12, height=2,relief=FLAT, font=("Terminal", 10),
                    command=lambda: show_frame(frame2))
frame1_btn.place(x=0,y=200)
frame1_btn = Button(frame1, text="Instruction", width=12, height=2,relief=FLAT, font=("Terminal", 10),
                    command=lambda: show_frame(frame4))

frame1_btn.place(x=0, y=250)
frame1_btn = Button(frame1, text="Quit", width=12, height=2,  font=("Terminal", 10), relief=FLAT,command=quit)
frame1_btn.place(x=0, y=300)

'''Frame Two has whole Game of KIRA'''
photo = PhotoImage(file="Back.png")
label = Label(frame3, image=photo)
label.image = photo
label.pack(fill=BOTH)


label = Label(frame3, text="Write The Name", font=("Terminal", 10))
label.place(x=290, y=10)

wind1 = Entry(frame3, width=20, borderwidth=5, justify="center", cursor="pencil")
wind1.place(x=280, y=50)

button1 = Button(frame3, text="Eradicate", command=game_K, relief=FLAT, font=("Terminal", 10), cursor="pencil")
button1.place(x=283, y=80)

button2 = Button(frame3, text="Quit", command=root.destroy, relief=FLAT , font=("Terminal", 10), cursor="pencil")
button2.place(x=373, y=80)


text_1= StringVar()
text_1.set("You have 3 attempts")

attempt = Label(frame3, textvariable=text_1)
attempt.place(x=290, y=120)


frame2_btn = Button(frame3, text="HOME", command=lambda: [show_frame(frame1),play()])
frame2_btn.place(x=0,y=0)


filename_C1 = PhotoImage(file="criminal1.png")
crim = Label(frame3, text="crimi", compound=BOTTOM,font=("Terminal", 10),image=filename_C1)
crim.place(x=0,y=300)
filename_C2 = PhotoImage(file="criminal2.png")
crim1 = Label(frame3,compound=BOTTOM, text="crmi",font=("Terminal", 10),image=filename_C2)
crim1.place(x=100,y=300)
filename_C3 = PhotoImage(file="criminal3.png")
crim2 = Label(frame3,compound=BOTTOM, text="crimiank2",font=("Terminal", 10),image=filename_C3)
crim2.place(x=200,y=300)
filename_C4 = PhotoImage(file="criminal4.png")
crim = Label(frame3, text="crimi", compound=BOTTOM,font=("Terminal", 10),image=filename_C4)
crim.place(x=300,y=300)
filename_C5 = PhotoImage(file="criminal5 -min.png")
crim1 = Label(frame3,compound=BOTTOM,text="crmi",font=("Terminal", 10),image=filename_C5)
crim1.place(x=400,y=300)
filename_C6 = PhotoImage(file="crminal6 -min.png")
crim2 = Label(frame3,compound=BOTTOM, text="crimiank2",font=("Terminal", 10),image=filename_C6)
crim2.place(x=500,y=300)
filename_C7 = PhotoImage(file="crminal7 -min.png")
crim = Label(frame2, text="Lind L.", compound=BOTTOM,font=("Terminal", 10),image=filename_C7)
crim.place(x=600,y=300)
filename_C8 = PhotoImage(file="crminal8 -min.png")
crim1 = Label(frame3,compound=BOTTOM, text="crmi",font=("Terminal", 10),image=filename_C8)
crim1.place(x=700,y=300)
filename_C9 = PhotoImage(file="crminal9 -min.png")
crim2 = Label(frame3,compound=BOTTOM,  text="crimiank2",font=("Terminal", 10),image=filename_C9)
crim2.place(x=800,y=300)

'''Frame Three'''

frame3_title = Label(frame2, text="SELECT YOU CHARECTER",font=("Terminal", 30), bg="red")
frame3_title.pack()
filename = PhotoImage(file="Kira.png")
but1 = Button(frame2, text="KIRA",compound=BOTTOM,font=("Terminal", 20),image=filename,
              command=lambda:[ show_frame(frame3),play2()])
but1.pack(side=LEFT)
filename_2 = PhotoImage(file="L.png")

but1 = Button(frame2, image=filename_2, text="DETECTIVE_L",compound=BOTTOM,font=("Terminal", 20),
              command=lambda:[ show_frame(frame5),play1()])
but1.pack(side=RIGHT)
'''Frame Four'''
frame4_title = Label(frame4, text="HOW TO PLAY",font=("Arail Bold",20))
frame4_title.pack()
rule1 = Label(frame4,text="If you are kira Write The Names of the Criminal Before L finds you", font =("Terminal",15) )
rule1.pack()
rule2 = Label(frame4,text="If you are L find the criminals before kira kills them",font=("Terminal",15))
rule2.pack()
frame4_btn = Button(frame4, text="HOME", command=lambda: show_frame(frame1))
frame4_btn.pack(side=TOP)

ryuk1= PhotoImage(file="Shini.png")
ryuk = Label(frame4,image=ryuk1)
ryuk.pack(side=BOTTOM)

'''Frame 7 has whole Game of L'''
photo = PhotoImage(file="Back.png")
label = Label(frame5, image=photo)
label.image = photo
label.pack(fill=BOTH)



label = Label(frame5, text="Write The Name", font=("Terminal", 10))
label.place(x=290, y=10)

wind = Entry(frame5, width=20, borderwidth=5, justify="center", cursor="pencil")
wind.place(x=280, y=50)

button1 = Button(frame5, text="Eradicate", command=game_L, relief=FLAT, font=("Terminal", 10), cursor="pencil")
button1.place(x=283, y=80)

button2 = Button(frame5, text="Quit", command=root.destroy, relief=FLAT , font=("Terminal", 10), cursor="pencil")
button2.place(x=373, y=80)

text = StringVar()
text.set("You have 3 attempts")

attempt = Label(frame5, textvariable=text)
attempt.place(x=290, y=120)

frame2_btn = Button(frame5, text="HOME", command=lambda: [show_frame(frame1),play()])
frame2_btn.place(x=0,y=0)



file_C1 = PhotoImage(file="criminal1.png")
crim = Label(frame5, text="crimi", compound=BOTTOM,font=("Terminal", 10),image=file_C1)
crim.place(x=0,y=300)
file_C2 = PhotoImage(file="criminal2.png")
crim1 = Label(frame5,compound=BOTTOM, text="crmi",font=("Terminal", 10),image=file_C2)
crim1.place(x=100,y=300)
file_C3 = PhotoImage(file="criminal3.png")
crim2 = Label(frame5,compound=BOTTOM, text="crimiank2",font=("Terminal", 10),image=file_C3)
crim2.place(x=200,y=300)
file_C4 = PhotoImage(file="criminal4.png")
crim = Label(frame5, text="Lind L. ", compound=BOTTOM,font=("Terminal", 10),image=file_C4)
crim.place(x=300,y=300)
file_C5 = PhotoImage(file="criminal5 -min.png")
crim1 = Label(frame5,compound=BOTTOM,text="crmi",font=("Terminal", 10),image=file_C5)
crim1.place(x=400,y=300)
file_C6 = PhotoImage(file="crminal6 -min.png")
crim2 = Label(frame5,compound=BOTTOM, text="crimiank2",font=("Terminal", 10),image=file_C6)
crim2.place(x=500,y=300)
file_C7 = PhotoImage(file="crminal7 -min.png")
crim = Label(frame5, text="crimi", compound=BOTTOM,font=("Terminal", 10),image=file_C7)
crim.place(x=600,y=300)
file_C8 = PhotoImage(file="crminal8 -min.png")
crim1 = Label(frame5,compound=BOTTOM, text="crmi",font=("Terminal", 10),image=file_C8)
crim1.place(x=700,y=300)
file_C9 = PhotoImage(file="crminal9 -min.png")
crim2 = Label(frame5,compound=BOTTOM,  text="crimiank2",font=("Terminal", 10),image=file_C9)
crim2.place(x=800,y=300)


show_frame(frame1)
root.mainloop()
