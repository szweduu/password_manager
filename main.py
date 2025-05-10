from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

Email="_"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_letters=[random.choice(letters) for letter in range(0,nr_letters-1)]
    password_symbols = [random.choice(symbols) for symbol in range(0,nr_symbols-1)]
    password_numbers = [random.choice(numbers) for number in range(0,nr_numbers-1)]

    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)

    pyperclip.copy(password)





# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    find=website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo("Info", "Please create file first.")

    else:
        try:
            email = data[find]["email"]
        except KeyError:
            messagebox.showinfo("Info", "This password doesn't exist")
        else:
            password=data[find]["password"]
            messagebox.showinfo("Info", f"Website: {find}\nEmail: {email}\nPassword: {password}")

def delete():
    password_entry.delete(0,END)
    website_entry.delete(0,END)


def combained_functions():
    add()
    delete()
    website_entry.focus()

def add():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    new_data={website:{
        "email":email,
        "password":password}}

    if len(password)==0 or len(website)==0:
        messagebox.showerror(title="Empty cells", message="Please dont leave empty cells!")
    else:
        #is_ok=messagebox.askokcancel(title="Info", message=f"Are you sure?\nEmail: {email}\nPassword: {password}")
        #if is_ok:
            try:
                with open("data.json", "r") as file:
                    data=json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)
window.config(padx=20,pady=20)
logo1=Canvas(width=200, height=200, highlightthickness=0)
logo_img=PhotoImage(file="logo.png")
logo1.create_image(110,112, image=logo_img, )
logo1.grid(column=1,row=0)

website_label=Label(text="Website")
website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username")
email_label.grid(row=2,column=0)

password_label=Label(text="Password")
password_label.grid(row=3,column=0)

website_entry=Entry(width=30)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry=Entry(width=48)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert(0,Email)

password_entry=Entry(width=30)
password_entry.grid(row=3,column=1)

generate_button=Button(text="Generate Password", command=generate,width=16)
generate_button.grid(row=3,column=2)

search_button=Button(text="Search", command=search,width=16)
search_button.grid(row=1,column=2)

add_button=Button(text="Add", command=combained_functions , width=44)
add_button.grid(row=4,column=1, columnspan=2)



window.mainloop()
