from tkinter import *
from tkinter import messagebox
import pyqrcode
app = Tk()
app.title("Qr Generator")
app.config(bg='#a4c639')
app.geometry("500x500")
app.iconbitmap("jonty_dp_G1h_icon.ico")

def generate_QR():
    if len(user_input.get())!=0 :
        global qr,img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    try:
        display_code()
    except:
        pass
def display_code():
    img_lbl.config(image = img)
    output.config(text="QR code for " + user_input.get())
    
lbl = Label(app, text="Enter the link to generate QR code",bg='#a4c639',font = ("Arial", 25))
lbl.pack()

user_input = StringVar()
entry = Entry(app, textvariable = user_input,font = ("Arial", 25))
entry.pack(padx=10)

button = Button(app,text = "Convert",font = ("Arial", 15),width=15,command = generate_QR)
button.pack(pady=10)

img_lbl = Label(app,bg='#a4c639')
img_lbl.pack()

output = Label(app,text="",bg='#a4c639')
output.pack()

app.mainloop()
