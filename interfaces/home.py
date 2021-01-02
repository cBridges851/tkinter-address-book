from tkinter import Tk, mainloop, Label, Button
from PIL import Image, ImageTk

class Home:
    def __init__(self):
        self.root = Tk()
    
    def render(self):
        self.root.configure(padx=20, pady=20)
        self.root.title("Chrispy Address Book")
        self.root.iconbitmap("./favicon.ico")

        title_label = Label(self.root, text="Welcome To The Chrispy Address Book", font=("Helvatica 20 bold"))
        title_label.grid(row=0, column=0, columnspan=2)

        introduction_label = Label(self.root, text="I would like to...", font=("Helvatica 18"))
        introduction_label.grid(row=1, column=0, columnspan=2)

        add_new_contact_image = ImageTk.PhotoImage(Image.open("Add A New Contact.png").resize((250,250)), Image.ANTIALIAS)
        add_new_contact_button = Button(self.root, image=add_new_contact_image)
        add_new_contact_button.grid(row=2, column=0)

        search_contact_image = ImageTk.PhotoImage(Image.open("Search For A Contact.png").resize((250,250)), Image.ANTIALIAS)
        search_contact_button = Button(self.root, image=search_contact_image)
        search_contact_button.grid(row=2, column=1)

        self.root.mainloop()

Home().render()