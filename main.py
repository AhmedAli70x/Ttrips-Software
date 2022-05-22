from tkinter import *
from tkinter import messagebox
from turtle import left

class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Gui")
        self.add_heading_label()
        self.add_sumbit_button()
        self.cancle_button()
        self.add_email_frame()
        self.add_email_label()
        self.add_email_entry()
        
    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack()
    
    def add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side=LEFT)
        self.email_label.configure(font="Arial 12",
                                    text="Email")
    
    def add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=RIGHT)

    def add_heading_label(self): 
        self.heading_label = Label()
        self.heading_label.pack()

        self.heading_label.configure(font="Arial 24",
                                    text="This is a heading.")

    def add_sumbit_button(self):
        self.submit_button = Button()
        self.submit_button.pack()

        self.submit_button.configure(
            text = "submit",
            bd = 2,
            bg = '#eff000'
        )
        self.submit_button.bind("<ButtonRelease-1>", self.submit_button_clicked)

    def cancle_button(self):

        self.submit_button = Button()
        self.submit_button.pack()

        self.submit_button.configure(
            text = "Cancle",
            bd = 2,
            bg = '#eff111')


    def submit_button_clicked(self, event):
        print("Hello Event")
        
        messagebox.showinfo("Welcome to the first GUI!", "The data has been submitted!")
        messagebox.showinfo("Your email isL:", self.email_entry )


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()