


from datetime import datetime

class Invoice:
    invoice_id =  0
    incoive_num = 1000
    def __init__(self, amount, trip=None, username=None, traveller_name=None, date=datetime.today().strftime('%Y-%m-%d') ):
        Invoice.invoice_id += 1
        Invoice.incoive_num +=1
        self.id = Invoice.invoice_id
        self.number = Invoice.incoive_num

        self.trip = trip
        self.amount = amount
        self.username = username
        self.traveller_name = traveller_name
        self.data = date

  
