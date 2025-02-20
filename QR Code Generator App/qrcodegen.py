import pyqrcode
from tkinter import *
from PIL import Image, ImageTk
import validators
from tkinter import messagebox

root = Tk()
root.title("QR Code Generator")

def paste_text():
    try:
        e1.delete(0, END)
        text = root.clipboard_get()
        e1.insert(INSERT, text)
    except TclError:
        pass

def clear():
    e1.delete(0, END)

def genqr():
    s = link.get()
    if validators.url(s):
        url = pyqrcode.create(s)
        url.png("genqr.png", scale=6) 

       
        qr_img = Image.open("genqr.png")
        qr_img = qr_img.resize((550,550))
        qr_icon = ImageTk.PhotoImage(qr_img)

        qrimg.config(image=qr_icon , width=550, height=550)
        qrimg.image = qr_icon

    else:
        messagebox.showerror("Error", "Enter a Valid Link!")

root.geometry("600x900")
root.resizable(FALSE, FALSE)
root.config(background="light grey")

link = StringVar()

paste_img = Image.open("paste.png")
paste_img = paste_img.resize((16, 16))
paste_icon = ImageTk.PhotoImage(paste_img)

h1 = Label(text="WELCOME TO QRCODE GENERATOR", font="Roboto 20 bold",highlightcolor="dark blue",highlightbackground="dark blue",highlightthickness=2,background="blue",foreground="white")
h1.pack(fill=X)
h2 = Label(text="Enter the link with https:// included", font="Roboto 12 underline", background="light grey")
h2.pack(pady=60)

f1 = Frame(root, background="white", height=100,width=100,relief=GROOVE, borderwidth=5)
f1.place(x=15, y=330)

p1 = Label(text="Paste Link:", background="pink", font="Unispace 10")
p1.place(x=10, y=200)

e1 = Entry(textvariable=link)
e1.place(x=110, y=200, width=450)

b1 = Button(text="Generate", command=genqr)
b1.place(x=280, y=240)

paste = Button(image=paste_icon, command=paste_text)
paste.place(x=562, y=199)

clearbut = Button(text="Clear", command=clear)
clearbut.place(x=35, y=240)

qrimg = Label(f1, bg="white", width=80, height=35)
qrimg.pack(expand=True)

root.mainloop()