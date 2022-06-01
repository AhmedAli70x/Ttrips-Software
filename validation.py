from tkinter import messagebox

class Validation:
    def __init__(self) -> None:
        pass

    @staticmethod
    def check_trip(name, date ):
        msg = ''
        if len(name)< 5:
            msg += ' Trip name min legth is 5 \n'
        if not date:
            msg += 'Date is required \n'

        
        if msg:
            messagebox.showerror(title="Error", message=msg)
            return False
        else:
            return True




