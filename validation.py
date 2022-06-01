from tkinter import messagebox

class Validation:
    def __init__(self) -> None:
        pass

    @staticmethod
    def check_trip(name, date ):
        msg = ''
        if len(name)< 5:
            msg += 'Trip name min legth is 5 \n'
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
            msg += 'Traveller name min legth is 5 \n'
        if not address:
            msg += 'Address min legth is 5  \n'
        if not birth_date:
            msg += 'Birth Date is required \n'
        if not birth_date:
            msg += 'Birth Date is required \n'

        if not emr_contact.strip().isdigit():
            msg += 'Enter valid Emr Contact number \n'

        if not ID_num.strip().isdigit():
            msg += 'Enter valid ID number \n'

        if len(full_name)< 5:
            msg += 'Full name min length is 5 \n'

        if not expiry_date:
            msg += 'Expiry Date is required \n'

        if not country:
            msg += 'Country is required \n'
        
        if msg:
            messagebox.showerror(title="Error", message=msg)
            return False
        else:
            return True

    @staticmethod
    def check_trip_leg(start_location, destination, interest_point, transport_provider):
        msg = ''
        if len(start_location)< 5:
            msg += 'Start Location min legth is 5 \n'
        if len(destination)< 5:
            msg += 'Destination min legth is 5 \n'
        if len(interest_point)< 6:
            msg += 'Interest Point min legth is 6  \n'
        if len(transport_provider)< 4:
            msg += 'Transport Provider min legth is 4  \n'

        if msg:
            messagebox.showerror(title="Error", message=msg)
            return False
        else:
            return True

    
    @staticmethod
    def check_user(username,user_name,  phone):
        msg = ''

        if len(username)< 5:
            msg += 'Username min legth is 5 \n'
        if len(user_name)< 3:
            msg += 'Name  minlegth is 3 \n'
        if not phone.strip().isdigit():
            msg += 'Enter valid phone number \n'

        if msg:
            messagebox.showerror(title="Error", message=msg)
            return False
        else:
            return True


    
    @staticmethod
    def check_invoice(amount, traveller):
        msg = ''
 
        if not amount.strip().isdigit():
            msg += 'Enter valid amount \n'
        if len(traveller)< 3:
            msg += 'Traveller min legth is 3 \n'

        if msg:
            messagebox.showerror(title="Error", message=msg)
            return False
        else:
            return True







