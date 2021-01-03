from tkinter import Tk, mainloop, Button, Label, Entry
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

        title_label = Label(self.root, text="Add A New Contact", font=("Helvatica 18 bold"))
        title_label.grid(row=0, column=1, columnspan=2)

        fields = {
            "Forename": None, 
            "Surname": None, 
            "Address Line 1": None, 
            "Address Line 2": None, 
            "Town/City": None, 
            "County": None, 
            "Country": None, 
            "Postcode": None, 
            "Phone Number": None, 
            "Email Address": None
        }

        row_count = 1

        for label in fields.keys():
            current_label = Label(self.root, text=f"{label}:", font=("Helvatica 14"), pady=5)
            current_label.grid(row=row_count, column=1)

            current_entry = Entry(self.root, font=("Helvatica 14"), width=50)
            fields[label] = current_entry
            current_entry.grid(row=row_count, column=2)

            row_count += 1
        
        submit_button = Button(self.root, text="ADD", font=("Helvatica 14 bold"), bg="green", fg="#FFFFFF")
        submit_button.grid(row=row_count + 1, column=1, columnspan=2)
        self.root.mainloop()