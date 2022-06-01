try:
    import Tkinter as tk
except:
    import tkinter as tk
    

app = tk.Tk()
app.geometry("300x100")
button1 = tk.Button(app, text="Button 1",
                    state=tk.DISABLED)


# button2 = tk.Button(app, text="EN/DISABLE Button 1")
# # button2.configure['state'] = tk.DISABLED
# button1.pack(side=tk.LEFT)
# button2.pack(side=tk.RIGHT)
# app.mainloop()

# invoice = [5,6,7]
# payment = [1,2,3]

# invoice += payment

# print(invoice)