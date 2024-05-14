from tkinter import *
from tkinter import messagebox
import base64

def perform_crypt(operation):
    password = code.get()
    if password == "1234":
        screen_child = Toplevel(screen)
        screen_child.title(f"{operation.capitalize()}")
        screen_child.geometry("400x200")
        screen_child.configure(bg="#ed3833")

        message = Text1.get(1.0, END)
        message = message.encode("ascii")
        if operation == "encrypt":
            processed_bytes = base64.b64encode(message)
        else:
            processed_bytes = base64.b64decode(message)
        processed_text = processed_bytes.decode("ascii")

        Label(screen_child, text=operation.upper(), font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen_child, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.insert(END, processed_text)
        text2.place(x=10, y=30, width=380, height=150)

    elif password == "":
        messagebox.showerror("Error", "Input password")
    else:
        messagebox.showerror("Error", "Invalid password")

def encrypt():
    perform_crypt("encrypt")

def decrypt():
    perform_crypt("decrypt")

def main_screen():
    global screen, code, Text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("PctApp")

    image_icon = PhotoImage(file="key.png")
    screen.iconphoto(False, image_icon)

    Label(text="Enter text for encryption and decryption", fg="black", font=("Calibri", 13)).place(x=10, y=10)
    Text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    Text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter Secret key for encryption and decryption", fg="black", font=("Calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=lambda: [code.set(""), Text1.delete(1.0, END)]).place(x=10, y=300)
    screen.mainloop()

main_screen()

