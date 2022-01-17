from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.title("Title")
root.geometry("600x600")
root.configure(background="black")
pic = Image.open("Kira.png")

resized = pic.resize((150,150),Image.ANTIALIAS)

new = ImageTk.PhotoImage(resized)
pic = ImageTk.PhotoImage(file="Kira.png")
label = Label(root,image=new)
label.pack()
'''
def(frame)
   

        image = Image.open("Back.png")
        img_copy = self.image.copy()

        sbackground_image = ImageTk.PhotoImage(self.image)

        background = Label(self, image=self.background_image)
        background.pack(fill=BOTH, expand=YES)
        background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


e = Example(root)
e.pack(fill=BOTH, expand=YES)
'''
root.mainloop()
# This code  to make bakcgrounfd image expand with the background
