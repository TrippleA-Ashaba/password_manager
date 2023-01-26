import json
from tkinter import *
from tkinter import messagebox
import pyperclip

BTN_COLOR = "#cce0ff"
BTN_ACTIVE = "#99c2ff"
ENTRY_BG = "#e6f0ff"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
from random import choice, shuffle, randint


def generate_password():
    password_entry.delete(0, END)
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "{", "}"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)
    # print(f"Your password is: {password}")
    # print(len(password))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = (web_entry.get()).title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details: \nEmail: {email} \nPassword: {password} \nIs it Ok to SAVE?",
        )
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving Updated data
                    json.dump(data, data_file, indent=4)
            finally:
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ----------------------------FIND PASSWORD --------------------------#


def find_password():
    website = (web_entry.get()).title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="No Data File Found.")
    else:

        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email : {email}\nPassword: {password}"
            )
        else:
            messagebox.showinfo(title="ERROR", message=f"{website} doesn't exist")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1, sticky="w", pady=2, padx=5)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2, sticky="w", pady=2, padx=5)

password_label = Label(text="Password")
password_label.grid(column=0, row=3, sticky="w", pady=2, padx=5)

# Entries
web_entry = Entry(width=32, background=ENTRY_BG)
web_entry.grid(column=1, row=1, sticky="w", pady=2)
web_entry.focus()

email_entry = Entry(width=52, background=ENTRY_BG)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w", pady=2)
email_entry.insert(0, "zbeeblebrox@email.com")

password_entry = Entry(width=32, background=ENTRY_BG)
password_entry.grid(column=1, row=3, sticky="w", pady=2)

# Buttons
generate_pwrd_btn = Button(
    text="Generate Password",
    bd=0,
    background=BTN_COLOR,
    width=15,
    command=generate_password,
    cursor="hand2",
    activebackground=BTN_ACTIVE,
)
generate_pwrd_btn.grid(column=2, row=3, sticky="w", pady=2)

add_btn = Button(
    text="Add",
    width=44,
    bd=0,
    background=BTN_COLOR,
    command=save,
    cursor="hand2",
    activebackground=BTN_ACTIVE,
)
add_btn.grid(column=1, row=4, columnspan=2, sticky="w", pady=2)

search_btn = Button(
    text="Search",
    background=BTN_COLOR,
    bd=0,
    width=15,
    command=find_password,
    cursor="hand2",
    activebackground=BTN_ACTIVE,
)
search_btn.grid(column=2, row=1, sticky="w", pady=2)


window.mainloop()
