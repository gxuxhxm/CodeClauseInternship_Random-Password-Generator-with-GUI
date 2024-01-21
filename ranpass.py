import random
import pyperclip
import string as s
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle

def on_hover(event):
    style = ThemedStyle(window)
    style.configure('my.TButton', background='#007acc', foreground='#282828', padding=5, font=('Ubuntu', 10))
    event.widget.configure(style='my.TButton')

def on_leave(event):
    style = ThemedStyle(window)
    style.configure('my.TButton', background='#00a1ff', foreground='#282828', padding=5, font=('Ubuntu', 10))
    event.widget.configure(style='my.TButton')

def randpassgen():
    try:
        password = ""
        for _ in range(int(inputlen.get())):
            char_Set = random.choice(all_str_combi)
            password += random.choice(char_Set)
        outpass.set(password)
    except ValueError:
        outpass.set("Invalid Input")

def copytoclip():
    pyperclip.copy(outpass.get())

window = Tk()
window.title("RANDOM PASSWORD GENERATOR")
window.geometry('400x400')
window.configure(bg='#282828')

outpass = StringVar()
all_str_combi = [s.digits, s.ascii_uppercase, s.ascii_lowercase, s.punctuation]

# frontend
head = Label(window, text="Password Length", font="Ubuntu  12 bold", bg='#282828', fg='#00a1ff')
head.pack(pady=10)

#spinbox to choose number of digits between 8 to 36
inputlen = Spinbox(window, from_=8, to_=36, textvariable=IntVar(), width=24, font='arial 16')
inputlen.pack()

# Generate password button
style = ThemedStyle(window)
style.set_theme("xpnative")  # You can choose a different theme if you like
style.configure('my.TButton', background='#00a1ff', foreground='#282828', padding=5, font=('Ubuntu', 10))
style.map('my.TButton', background=[('active', '#007acc')])

generate_button = ttk.Button(window, text="Generate password", command=randpassgen, style='my.TButton')
generate_button.pack(pady=20)
generate_button.bind("<Enter>", on_hover)
generate_button.bind("<Leave>", on_leave)

passlabel = Label(window, text='Random Generated Password', font='Ubuntu  12 bold', bg='#282828', fg='#00a1ff')
passlabel.pack(pady="30 10")

pass_entry = Entry(window, textvariable=outpass, width=24, font='Ubuntu  16')
pass_entry.pack()

copy_button = ttk.Button(window, text="Copy To Clipboard", command=copytoclip, style='my.TButton')
copy_button.pack(pady=20)
copy_button.bind("<Enter>", on_hover)
copy_button.bind("<Leave>", on_leave)

window.mainloop()
