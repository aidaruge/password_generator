import random as rnd
import tkinter as tk
import string

LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = string.punctuation


def generate_pwd():
    letter_list = []
    num_list = []
    symbol_list = []

    letter_count = letter_ent.get()
    number_count = number_ent.get()
    symbol_count = symbol_ent.get()
    
    try:
        letter_count = int(letter_count)

    except:
        letter_count = 0
    finally:
        for i in range(letter_count):
            letter_list.append(rnd.choice(LETTERS))

    
    try:
        number_count = int(number_count)

    except:
        number_count = 0
    finally:
        for i in range(number_count):
            num_list.append(rnd.choice(NUMBERS))

    
    try:
        symbol_count = int(symbol_count)

    except:
        symbol_count = 0
    finally:
        for i in range(symbol_count):
            symbol_list.append(rnd.choice(SYMBOLS))


    pwd_list = letter_list + num_list + symbol_list
    rnd.shuffle(pwd_list)
    pwd = ''.join(pwd_list)

    pwd_ent.delete(0, tk.END)
    window.clipboard_clear()
    pwd_ent.insert(0, pwd)
    window.clipboard_append(pwd)

# design

window = tk.Tk()
window.config(padx=30, pady=30)
window.title('Password Generator')

letter_lbl = tk.Label(text='How many letters?', pady=10)
letter_lbl.grid(column=0, row=0)
letter_ent = tk.Entry()
letter_ent.grid(column=1, row=0)

number_lbl = tk.Label(text='How many numbers?', pady=10)
number_lbl.grid(column=0, row=1)
number_ent = tk.Entry()
number_ent.grid(column=1, row=1)

symbol_lbl = tk.Label(text='How many symbols?', pady=10)
symbol_lbl.grid(column=0, row=2)
symbol_ent = tk.Entry()
symbol_ent.grid(column=1, row=2)

password_btn = tk.Button(text='Generate Password', command=generate_pwd, pady=5)
password_btn.grid(columnspan=2, row=3)

pwd_lbl = tk.Label(text='Your Password', pady=10)
pwd_lbl.grid(column=0, row=4)
pwd_ent = tk.Entry()
pwd_ent.grid(column=1, row=4)

window.mainloop()
