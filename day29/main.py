import string
import random
import tkinter
from tkinter import messagebox

CHARACTERS = string.ascii_letters + string.digits + string.punctuation


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password = ""
    password_entry.delete(0, tkinter.END)
    for _ in range(6):
        password += random.choice(CHARACTERS)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data(webname, email_usr, password):
    with open('saved_passwords.txt', 'a') as file:
        file.write(f"{webname} | {email_usr} | {password}\n")


def to_save_dialog():
    website = website_entry.get()
    email_or_username = email_entry.get()
    password = password_entry.get()
    if website == "" or email_or_username == "" or password == "":
        messagebox.showerror(title="Error", message="Please fill in all fields!")
    else:
        is_inserted_details_correct = messagebox.askquestion("Are you sure to save?", f""
                                                                                      f"website name: {website}\n"
                                                                                      f"email address: {email_or_username}\n"
                                                                                      f"password: {password}")
        if is_inserted_details_correct == "yes":
            save_data(website, email_or_username, password)
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            email_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.minsize(400, 400)
window.config(padx=50, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website: ", font=("Arial", 10, "normal"))
website_label.grid(row=1, column=0)
website_entry = tkinter.Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_label = tkinter.Label(text="Email/Username: ", font=("Arial", 10, "normal"))
email_label.grid(row=2, column=0)
email_entry = tkinter.Entry(width=35)
email_entry.insert(0, "alibakhshi.bs@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text="Password: ", font=("Arial", 10, "normal"))
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)
generate_password_button = tkinter.Button(text="Generate Password", font=("Arial", 9, "normal"),
                                          command=password_generator)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, font=("Arial", 10, "normal"), command=to_save_dialog)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
