from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300,300)

my_label = Label(window, text="miles", font=("Arial", 11, "normal"))

my_label.place(x=200, y=100)
input = Entry(width=10)
input.place(x=125, y=105)
equal_to = Label(window, text="is equal to", font=("Arial", 11, "normal"))
equal_to.place(x=35, y=130)
result = Label(window, text="10", font=("Arial", 11, "normal"))
result.place(x=150, y=130)
rest = Label(window, text="Kilometers", font=("Arial", 11, "normal"))
rest.place(x=200, y=130)

def calculate():
    kilometer = int(input.get()) * 1.609344
    result.config(text=f"{round(kilometer,3)}")

button = Button(text="Calculate", command=calculate)
button.place(x=150, y=200)


window.mainloop()
