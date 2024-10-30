from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    password = pass_entry.get()
    email = us_em_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) < 3 or len(email) < 14 or len(password) < 1:
        messagebox.showinfo(title="", message="Please don't leave any fields empty")
    else:
        try:
            with open("Pass_Generator.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("Pass_Generator.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("Pass_Generator.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    search_item = web_entry.get()
    try:
        with open("Pass_Generator.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="", message="File not found")
    else:
        if search_item in data:
            x = data[search_item]
            messagebox.showinfo(title="", message=f"{search_item} Email:{x["email"]} Password:{x["password"]}")
        else:
            messagebox.showinfo(title="Not found",
                                message=f"You dont have a password stored for Website: {search_item}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
canvas_image = PhotoImage(file="password_generator/logo.png")
canvas.create_image(100, 100, image=canvas_image)
canvas.grid(column=1, row=0)

website_lb = Label(text="Website:", font=("arial", 24, "bold"))
website_lb.grid(column=0, row=1)
us_em_lb = Label(text="Email/Username:", font=("arial", 24, "bold"))
us_em_lb.grid(column=0, row=2)
pass_lb = Label(text="Password:", font=("arial", 24, "bold"))
pass_lb.grid(column=0, row=3)

web_entry = Entry(width=21)
web_entry.grid(column=1, row=1, columnspan=1)
web_entry.focus()

us_em_entry = Entry(width=38)
us_em_entry.grid(column=1, row=2, columnspan=2)
us_em_entry.insert(0, "your email address")
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="search", width=13, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
