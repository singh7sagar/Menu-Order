# Menu Order

from tkinter import *


def display():
    if (x.get() == 0):
        print("You Ordered a Pizza! ")
    elif (x.get() == 1):
        print("You Ordered a Burger!")
    else:
        print("You Ordered a Sandwich!")


food = ["Pizza  $1.50", "Burger  $0.50", "Sandwich  $0.40"]


window = Tk()
window.config(bg="black")

burger = PhotoImage(file="burger.gif")
pizza = PhotoImage(file="pizza.gif")
sandwich = PhotoImage(file="sandwich.gif")
food_images = [pizza, burger, sandwich]

x = IntVar()


for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value=index,
                               padx=25,
                               font=("Impact", 30),
                               bg="black",
                               fg="#00ff00",
                               activeforeground="#00ff00",
                               activebackground="Black",
                               image=food_images[index],
                               compound="left",
                               width=375,
                               indicatoron=0,
                               command=display
                               )

    radio_button.pack(anchor=W)

window.mainloop()
#Menu Order

from tkinter import *


def display():
    if (x.get() == 0):
        print("You Ordered a Pizza! ")
    elif (x.get() == 1):
        print("You Ordered a Burger!")
    else:
        print("You Ordered a Sandwich!")


food = ["Pizza  $1.50", "Burger  $0.50", "Sandwich  $0.40"]


window = Tk()
window.config(bg="black")

burger = PhotoImage(file="burger.gif")
pizza = PhotoImage(file="pizza.gif")
sandwich = PhotoImage(file="sandwich.gif")
food_images = [pizza, burger, sandwich]

x = IntVar()


for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value=index,
                               padx=25,
                               font=("Impact", 30),
                               bg="black",
                               fg="#00ff00",
                               activeforeground="#00ff00",
                               activebackground="Black",
                               image=food_images[index],
                               compound="left",
                               width=375,
                               indicatoron=0,
                               command=display
                               )

    radio_button.pack(anchor=W)

window.mainloop()
