from tkinter import Tk, mainloop, Button
from PIL import Image, ImageTk

class AddContact:
    def __init__(self):
        self.root = Tk()

    def render(self):
        self.root.configure(padx=20, pady=20)
        self.root.title("Chrispy Address Book")
        self.root.iconbitmap("../favicon.ico")
        self.root.resizable(False, False)
        
        back_button_image = ImageTk.PhotoImage(Image.open("../Back.png").resize((250,125)), Image.ANTIALIAS)
        back_button = Button(self.root, image=back_button_image)
        back_button.grid(row=0, column=0)
        self.root.mainloop()

AddContact().render()