# ====== Importing Modules=============================
from tkinter import *  # importing tkinter as 8 object
import pygame  # importing pygame module for music
from tkinter import messagebox as mbox  # from tkinter importing message box
import cv2  # importing cv2 module to read the video format

# ==================================================================

root = Tk()  # initialising Tk to root
root.geometry("900x500")  # setting the window size
root.rowconfigure(0, weight=1)  # giving permission to frame to expand with the window
root.columnconfigure(0, weight=1)  # giving permission to frame to expand with the window
root.title("The Death Note")  # Giving title to the window
root.iconbitmap(r'death_AD5_icon.ico')  # this line is to change the tkinter icon

# ========== Code For background music using pygame module  ============
file_T = "Deathnote theme.mp3"  # name of the file which wil be played
pygame.init()  # initialising pygame module
pygame.mixer.init()  # initialising mixer to load file
pygame.mixer.music.load(file_T)  # from mixer calling music to load the music file  (format is mp3)
pygame.mixer.music.play()  # this line will run music


# =========== Defining some play functions for button to get differ BGM for different frame =====================
def play():
    file3 = "Deathnote theme.mp3"  # same from line 16 to line 21 but different file
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file3)
    pygame.mixer.music.play()


def play1():
    file1 = "ThemeL.mp3"  # same from line 16 to line 21 but different file
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file1)
    pygame.mixer.music.play()


def play2():
    file2 = "KIRAtheme.mp3"  # same from line 16 to line 21 but different file
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file2)
    pygame.mixer.music.play()


# ====================== Defining some game function ===============================

# ============ KIRA GAMEPLAY FUNCTION ==============================================
def game_K():
    global text_1  # making a text variable as global value
    # ====LIST OF NAMES =====================
    name = ["Michel", "LindL", "Mello"]
    name1 = ["Samuel", "Ryuzaki", "Saitama"]
    name2 = ["Richard", "Light", "Genos"]
    # ===================we are using the use given input by get() method=====
    guess1 = wind1.get()
    # ============check the input=================
    if guess1 == "":
        mbox.showerror("Error", "Enter name ")  # error box if nothing is entered
    elif guess1 == name1[0] or guess1 == name[0] or guess1 == name2[0]:
        if guess1 == name[0]:
            # =========This code is used several time here ==========
            # ========This code is o play video using cv2 module=======
            cap = cv2.VideoCapture("V1Criminal 2 dies.mp4")  # initialising the video file
            while True:  # while loop when ever it is true
                ret, frame_1 = cap.read()  # this will capture frame by frame and will return to ret and plays on screen

                cv2.imshow("Kira", frame_1)  # this will show the captured frame
                if cv2.waitKey(25) & 0xFF == ord("q"):  # we are giving q to escape from the video
                    break  # this will break the loop
            cap.release()  # captured video id released
            cv2.destroyAllWindows()  # destroys all the windows of cv2
            text_1.set("Criminal 1 died")
            button1.pack_forget()
        elif guess1 == name1[0]:
            # ================SAME AS LINE 65 ===========================
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
            # ================SAME AS LINE 65 ===========================
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
            # ================SAME AS LINE 65 ===========================
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
            # ================SAME AS LINE 65 ===========================
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
            # ================SAME AS LINE 65 ===========================
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


# ==================== L GAMEPLAY FUNCTION ====================================================

def game_L():
    global text_l
    names = ["Michel", "LindL", "Mello"]
    names1 = ["Samuel", "Ryuzaki", "Saitama"]
    names2 = ["Richard", "Light", "Genos"]
    guess = wind.get()
    if guess == "":
        mbox.showerror("Error", "Enter name ")
    elif guess == names[0] or guess == names2[0] or guess == names1[0]:
        if guess == names[0]:
            # ================SAME AS LINE 65 ===========================
            cap = cv2.VideoCapture("V5LtricksKira.mp4")
            while True:
                ret, frame_1 = cap.read()
                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_l.set("You Tricked Kira He is in japan")
            button1.pack_forget()
        elif guess == names1[0]:
            # ================SAME AS LINE 65 ===========================
            cap = cv2.VideoCapture("V6Lgetsthebook.mp4")
            while True:
                ret, frame_1 = cap.read()
                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_l.set("This the death note which kills the person name written in it")
            button1.pack_forget()
        elif guess == names2[0]:
            # ================SAME AS LINE 65 ===========================
            cap = cv2.VideoCapture("V7KIRAdied.mp4")
            while True:
                ret, frame_1 = cap.read()
                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_l.set("KIRA died you won")
            button1.pack_forget()
    elif guess == names[1] or guess == names[2] or guess == names1[1] or guess == names1[2] \
            or guess == names2[1] or guess == names2[2]:
        if guess == names[1] or guess == names[2]:
            # ================SAME AS LINE 65 ===========================
            cap = cv2.VideoCapture("V1Criminal 2 dies.mp4")
            while True:
                ret, frame_1 = cap.read()
                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_l.set("Kira killed first person")
            button1.pack_forget()
        elif guess == names1[1] or guess == names1[2]:
            # ================SAME AS LINE 65 ===========================
            cap = cv2.VideoCapture("V2Criminal1 dies.mp4")
            while True:
                ret, frame_1 = cap.read()
                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_l.set("Kira killed second person ")
            button1.pack_forget()
        elif guess == names2[1] or guess == names2[2]:
            # ================SAME AS LINE 65 ===========================
            cap = cv2.VideoCapture("V3Ldied.mp4")
            while True:
                ret, frame_1 = cap.read()
                cv2.imshow("Kira", frame_1)
                if cv2.waitKey(15) & 0xFF == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()
            text_l.set("You are died")
            button1.pack_forget()
    else:
        mbox.showerror("Error", "Criminal image should be present")


# ==================== function to show the frame ==================
def show_frame(frameK):  # we are passing the frame and this will be the frame we are calling
    frameK.tkraise()


# ======creating frames and initialising to the Frame widget as root ==========
# ====== we are creating 5 frame ==============================================
frame1 = Frame(root)
frame2 = Frame(root, background="Black")
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
# ============ for loop to add all 5 frame at same time =========
for frame in (frame1, frame2, frame3, frame4, frame5):
    frame.grid(row=0, column=0, sticky="nsew")  # This will put all frame onto each other

# =============================== FRAME ONE ,MAIN MENU  ===========================================
# =============================This the frame one the MENU ========================================
photo = PhotoImage(file="Back2.png")  # setting photo image to variable photo
label = Label(frame1, image=photo)  # label to show the pic this is the background picture
label.image = photo
label.pack(fill=BOTH)  # packing the label

# ==========Start button which will takes to frame 3 where we will select the character ============
frame1_btn = Button(frame1, text="Start", width=12, height=2, relief=FLAT, font=("Terminal", 10),
                    command=lambda: show_frame(frame2))
frame1_btn.place(x=0, y=200)

# ==========Instruction button which will takes to frame 4 to know to play ============
frame1_btn = Button(frame1, text="Instruction", width=12, height=2, relief=FLAT, font=("Terminal", 10),
                    command=lambda: show_frame(frame4))
frame1_btn.place(x=0, y=250)

# ==========QUIT  button  quits the game============
frame1_btn = Button(frame1, text="Quit", width=12, height=2, font=("Terminal", 10), relief=FLAT, command=quit)
frame1_btn.place(x=0, y=300)


# ========================== FRAME TWO SELECT YOUR CHARACTER ====================================================

frame3_title = Label(frame2, text="SELECT YOUR CHARACTER", font=("Terminal", 30), bg="red")  # title
frame3_title.pack()
filename = PhotoImage(file="Kira.png")  # Background image
but1 = Button(frame2, text="KIRA", compound=BOTTOM, font=("Terminal", 20), image=filename,
              command=lambda: [show_frame(frame3), play2()])
but1.pack(side=LEFT)
filename_2 = PhotoImage(file="L.png")

but1 = Button(frame2, image=filename_2, text="DETECTIVE_L", compound=BOTTOM, font=("Terminal", 20),
              command=lambda: [show_frame(frame5), play1()])
but1.pack(side=RIGHT)

frame4_btn = Button(frame2, text="HOME", command=lambda: show_frame(frame1))
frame4_btn.place(x=0, y=0)
# ======================================= FRAME THREE GAME FRAME OF KIRA ===========================================
photo = PhotoImage(file="Back.png")  # background image
label = Label(frame3, image=photo)
label.image = photo
label.pack(fill=BOTH)

label = Label(frame3, text="Guess the name", font=("Terminal", 10))  # label which says write name
label.place(x=290, y=10)

wind1 = Entry(frame3, width=20, borderwidth=5, justify="center",
              cursor="pencil")  # entry widget to take input from user
wind1.place(x=280, y=50)

button1 = Button(frame3, text="Eradicate", command=game_K, relief=FLAT, font=("Terminal", 10), cursor="pencil")
button1.place(x=283, y=80)  # button which checks the input taken from user

button2 = Button(frame3, text="Quit", command=root.destroy, relief=FLAT, font=("Terminal", 10), cursor="pencil")
button2.place(x=373, y=80)  # quit button

text_1 = StringVar()
text_1.set("Eradicate the criminals")  # giving text which will be changed according to the output

attempt = Label(frame3, textvariable=text_1)  # label which will store the string variable
attempt.place(x=290, y=120)

frame2_btn = Button(frame3, text="HOME", command=lambda: [show_frame(frame1), play()])
frame2_btn.place(x=0, y=0)  # button to go back to main menu
frame2_btn1 = Button(frame3, text="BACK", command=lambda: [show_frame(frame2), play()])
frame2_btn1.place(x=850, y=0)
# ==========================All CRIMINALS IMAGES AND NAMES WILL BE SHOWN ON FRAME 3 ===================================
# ===========================USED SAME LABEL METHOD ===================================================================

filename_K1 = PhotoImage(file="criminal1.png")
crim = Label(frame3, text="Mello", compound=BOTTOM, font=("Terminal", 10), image=filename_K1)
crim.place(x=0, y=300)
filename_K2 = PhotoImage(file="criminal2.png")
crim1 = Label(frame3, compound=BOTTOM, text="Michel", font=("Terminal", 10), image=filename_K2)
crim1.place(x=100, y=300)
filename_K3 = PhotoImage(file="criminal3.png")
crim2 = Label(frame3, compound=BOTTOM, text="Samuel", font=("Terminal", 10), image=filename_K3)
crim2.place(x=200, y=300)
filename_K4 = PhotoImage(file="criminal4.png")
crim = Label(frame3, text="Light", compound=BOTTOM, font=("Terminal", 10), image=filename_K4)
crim.place(x=300, y=300)
filename_K5 = PhotoImage(file="criminal5 -min.png")
crim1 = Label(frame3, compound=BOTTOM, text="Ryuzaki", font=("Terminal", 10), image=filename_K5)
crim1.place(x=400, y=300)
filename_K6 = PhotoImage(file="crminal6 -min.png")
crim2 = Label(frame3, compound=BOTTOM, text="Genos", font=("Terminal", 10), image=filename_K6)
crim2.place(x=500, y=300)
filename_K7 = PhotoImage(file="crminal7 -min.png")
crim = Label(frame3, text="LindL", compound=BOTTOM, font=("Terminal", 10), image=filename_K7)
crim.place(x=600, y=300)
filename_K8 = PhotoImage(file="crminal8 -min.png")
crim1 = Label(frame3, compound=BOTTOM, text="Richard", font=("Terminal", 10), image=filename_K8)
crim1.place(x=700, y=300)
filename_K9 = PhotoImage(file="crminal9 -min.png")
crim2 = Label(frame3, compound=BOTTOM, text="Saitama", font=("Terminal", 10), image=filename_K9)
crim2.place(x=800, y=300)

# ==============================INSTRUCTION PAGE FRAME FOUR ==================================================
frame4_title = Label(frame4, text="HOW TO PLAY", font=("Arial Bold", 20))
frame4_title.pack()  # label to show text
rule1 = Label(frame4, text="If you are kira Write The Names of the Criminal Before L finds you", font=("Terminal", 15))
rule1.pack()  # label to show text
rule2 = Label(frame4, text="If you are L find the criminals before kira kills them", font=("Terminal", 15))
rule2.pack()  # label to show text
frame4_btn = Button(frame4, text="HOME", command=lambda: show_frame(frame1))
frame4_btn.pack(side=TOP)  # button will take back to home

ryuk1 = PhotoImage(file="Shini.png")  # label method to show image
ryuk = Label(frame4, image=ryuk1)
ryuk.pack(side=BOTTOM)

# ==========================FRAME FIVE CHARACTER L GAME FRAME=============================
photo = PhotoImage(file="Back.png")  # label method to set background image
label = Label(frame5, image=photo)
label.image = photo
label.pack(fill=BOTH)

label = Label(frame5, text="Guess The Name", font=("Terminal", 10))
label.place(x=290, y=10)

wind = Entry(frame5, width=20, borderwidth=5, justify="center", cursor="pencil")
wind.place(x=280, y=50)

button1 = Button(frame5, text="Eradicate", command=game_L, relief=FLAT, font=("Terminal", 10), cursor="pencil")
button1.place(x=283, y=80)

button2 = Button(frame5, text="Quit", command=root.destroy, relief=FLAT, font=("Terminal", 10), cursor="pencil")
button2.place(x=373, y=80)

text_l = StringVar()
text_l.set("Guess the criminal KIRA might kill")

attempt = Label(frame5, textvariable=text_l)
attempt.place(x=290, y=120)

frame2_btn = Button(frame5, text="HOME", command=lambda: [show_frame(frame1), play()])
frame2_btn.place(x=0, y=0)
frame2_btn1 = Button(frame5, text="BACK", command=lambda: [show_frame(frame2), play()])
frame2_btn1.place(x=850, y=0)
# ==========================All CRIMINALS IMAGES AND NAMES WILL BE SHOWN ON FRAME 5 ===================================
# ===========================USED SAME LABEL METHOD ===================================================================
filename_C1 = PhotoImage(file="criminal1.png")
crim = Label(frame5, text="Mello", compound=BOTTOM, font=("Terminal", 10), image=filename_C1)
crim.place(x=0, y=300)
filename_C2 = PhotoImage(file="criminal2.png")
crim1 = Label(frame5, compound=BOTTOM, text="Michel", font=("Terminal", 10), image=filename_C2)
crim1.place(x=100, y=300)
filename_C3 = PhotoImage(file="criminal3.png")
crim2 = Label(frame5, compound=BOTTOM, text="Samuel", font=("Terminal", 10), image=filename_C3)
crim2.place(x=200, y=300)
filename_C4 = PhotoImage(file="criminal4.png")
crim = Label(frame5, text="Light", compound=BOTTOM, font=("Terminal", 10), image=filename_C4)
crim.place(x=300, y=300)
filename_C5 = PhotoImage(file="criminal5 -min.png")
crim1 = Label(frame5, compound=BOTTOM, text="Ryuzaki", font=("Terminal", 10), image=filename_C5)
crim1.place(x=400, y=300)
filename_C6 = PhotoImage(file="crminal6 -min.png")
crim2 = Label(frame5, compound=BOTTOM, text="Genos", font=("Terminal", 10), image=filename_C6)
crim2.place(x=500, y=300)
filename_C7 = PhotoImage(file="crminal7 -min.png")
crim = Label(frame5, text="LindL", compound=BOTTOM, font=("Terminal", 10), image=filename_C7)
crim.place(x=600, y=300)
filename_C8 = PhotoImage(file="crminal8 -min.png")
crim1 = Label(frame5, compound=BOTTOM, text="Richard", font=("Terminal", 10), image=filename_C8)
crim1.place(x=700, y=300)
filename_C9 = PhotoImage(file="crminal9 -min.png")
crim2 = Label(frame5, compound=BOTTOM, text="Saitama", font=("Terminal", 10), image=filename_C9)
crim2.place(x=800, y=300)

# ==================this function is called which will show the frame 1==============
show_frame(frame1)
# ================this line will run the event loop=======================
root.mainloop()
