from tkinter import*
from tkinter import messagebox
from random import choice, shuffle, randint
#import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    passwd_entry.insert(0, password)
    #pyperclip.copy(password)

# password = ""
# for char in password_list:
#   password += char



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = passwd_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="WHatttt?", message="Can't save an Empty file")
    else:
        messagebox.showinfo(title="You Sure?", message="Okay")

        with open("Info.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            web_entry.delete(0, END)
            passwd_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=5)

canvas = Canvas(width=200, height=200)
passwd = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=passwd)
canvas.grid(row=0, column=1)

#Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0) #, fg='black', bg='white', highlightthickness=

#Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=1)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=1)
email_entry.insert(0,"siddharth.desai1996@gmail.com")
passwd_entry = Entry(width=35)
passwd_entry.grid(row=3, column=1)

#Buttons
gen_passwd_button = Button(text="Generate Password", command=gen_password)
gen_passwd_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=29, command=save)
add_button.grid(row=4, column=1)





window.mainloop()