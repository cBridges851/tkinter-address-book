from tkinter import Tk, mainloop, Button, Label, Entry, OptionMenu, StringVar
from PIL import Image, ImageTk

class SearchContact:
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

        title_label = Label(self.root, text="Search For A Contact", font=("Helvatica 18 bold"))
        title_label.grid(row=0, column=1, columnspan=4)

        search_by_label = Label(self.root, text="I wish to search by:", font=("Helvatica 16"))
        search_by_label.grid(row=1, column=1)

        fields = [
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

        options_var = StringVar()
        options_var.set(fields[0])

        search_by_dropdown = OptionMenu(self.root, options_var, *fields)
        search_by_dropdown.configure(font=("Helvatica 14"), width=10)
        search_by_dropdown.grid(row=1, column=2)

        search_field = Entry(self.root, font=("Helvatica 14"), width=30)
        search_field.grid(row=1, column=3, padx=10, pady=5)

        search_button = Button(self.root, text="SEARCH", font=("Helvatica 14"), width=10)
        search_button.grid(row=1, column=4)

        self.root.mainloop()