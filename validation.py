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

    @staticmethod
    def check_traveller(name, address, birth_date, emr_contact, ID_num, full_name, expiry_date, country ):
        msg = ''
        if len(name)< 5:
            msg += ' Traveller name min legth is 5 \n'
        if not address:
            msg += 'Address min legth is 5  \n'
        if not birth_date:
            msg += 'Birth Date is required \n'
        if not birth_date:
            msg += 'Birth Date is required \n'

        if not emr_contact.strip().isdigit():
            msg += ' Enter valid Emr Contact number \n'

        if not ID_num.strip().isdigit():
            msg += 'Enter valid ID number \n'

        if len(full_name)< 5:
            msg += ' Full name min length is 5 \n'

        if not expiry_date:
            msg += ' Expiry Date is required \n'

        if not country:
            msg += ' Country is required \n'


        
        if msg:
            messagebox.showerror(title="Error", message=msg)
            return False
        else:
            return True




