from tkinter import *
from tkinter import messagebox as mbox
import random
window = Tk()
window.title("Password Manager")

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    if len(password_entry.get()) != 0:
        password_entry.delete(0, END)
    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list.extend([random.choice(symbols) for symbol in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for number in range(random.randint(2, 4))])
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(END, f"{password}")


# Writing Informations
def write_into_text():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()



    if len(website) and len(email) and len(password) > 0:
        is_okay = mbox.askokcancel(title=website, message=f"These are the details entered: "
                                                          f"\nEmail:{email}\nPassword: {password}\nIs it okay to save?")
        if is_okay:
            with open("data.txt", 'a') as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        mbox.showerror(title = "Empty input", message = "Please enter all the details")




# UI Setting ----------
window.config(padx=50,pady=50)
image = PhotoImage(file = "logo.png")
canvas = Canvas(width=200, height=224)
canvas.create_image(102,112, image=image)
canvas.grid(row=0,column=1)


## Information about website here
website_text = Label(text = "Website: ", font=("Arial", 16))
email_label = Label(text = "Email: ", font=("Arial", 16))
password_label = Label(text = "Password: ", font=("Arial", 16))

website_text.grid(row=1,column=0)
email_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)


website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)

website_entry.grid(row=1,column=1,columnspan=2)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(END, "seojin@gmail.com")
password_entry.grid(row=3,column=1)
website_entry.focus()

## Buttons

generate_password_button = Button(text = "Generate Password", command = generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text = "Add", width = 36, command = write_into_text)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()
