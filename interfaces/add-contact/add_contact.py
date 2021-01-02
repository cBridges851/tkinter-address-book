from tkinter import Tk, mainloop, Button, Label
from PIL import Image, ImageTk

class AddContact:
    def __init__(self):
        self.root = Tk()

    def render(self):
        self.root.configure(padx=20, pady=20)
        self.root.title("Chrispy Address Book")
        self.root.iconbitmap("../favicon.ico")
        self.root.resizable(False, False)
        
        back_button_image = ImageTk.PhotoImage(Image.open("../Back.png").resize((70,38)), Image.ANTIALIAS)
        back_button = Button(self.root, image=back_button_image)
        back_button.grid(row=0, column=0)

        labels = [
            "Forename", 
            "Surname", 
            "Address Line 1", 
            "Address Line 2", 
            "Town/City", 
            "County", 
            "Country", 
            "Postcode", 
            "Phone Number", 
            "Email Address"
        ]

        row_count = 1
        for label in labels:
            current_label = Label(self.root, text=f"{label}:", font=("Helvatica 14"))
            current_label.grid(row=row_count, column=1)
            row_count += 1


        self.root.mainloop()

AddContact().render()