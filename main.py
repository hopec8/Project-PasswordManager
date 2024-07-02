from tkinter import *
import random
from tkinter import messagebox
import json

PASSWORD_LENGTH = 12
UPPER_CASE_LIST = ["A", "B", "C", "D", "E", "F", "G", 'H', 'I',
                      'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                      'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
LOWER_CASE_LIST = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBER_LIST = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SYMBOL_LIST = ['.', ',', '?', '!', '/', ';']

#window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#canvas setup
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

#Generate Password
def generate_password():
    password = []
    password.clear()
    symbol_to_add = random.choice(SYMBOL_LIST)
    password.append(symbol_to_add)
    for i in range(2):
        number_to_add = random.choice(NUMBER_LIST)
        password.append(number_to_add)
    for i in range(3):
        upper_to_add = random.choice(UPPER_CASE_LIST)
        password.append(upper_to_add)
    for i in range(6):
        lower_to_add = random.choice(LOWER_CASE_LIST)
        password.append(lower_to_add)
    random.shuffle(password)
    password_output = "".join(password)
    password_entry.delete(0, PASSWORD_LENGTH)
    password_entry.insert(0, password_output)

#Add password to file
def add_password():
    website_to_add = website_entry.get()
    email_to_add = email_entry.get()
    password_to_add = password_entry.get()
    new_data = {
        website_to_add: {
            "email": email_to_add,
            "password": password_to_add
        }
    }
    if len(website_to_add) == 0 or len(email_to_add) == 0 or len(password_to_add) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any field empty.")
    else:
        try:
            with open("saved_passwords.json", mode="r") as password_file:
                    data = json.load(password_file)
                    data.update(new_data)
        except FileNotFoundError:
            with open("saved_passwords.json", mode="w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            data.update(new_data)
            with open("saved_passwords.json", mode="w") as password_file:
                json.dump(data, password_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#Find Password:
def find_password():
    website = website_entry.get()
    try:
        with open("saved_passwords.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title="Error", message=f"No details for {website}")

#labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "hopecapp@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Buttons
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)
password_button = Button(text="Generate Password", width=12, command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)






window.mainloop()