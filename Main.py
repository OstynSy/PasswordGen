#Coded by: Ostyn Sy
#5/3/2018

from tkinter import *
import random


root = Tk()
root.title("Password Generator")


def numbercalc(val):
    numbers = chr(random.randint(48, 57))
    val += numbers
    return val


def specialcalc(val):
    rannum1 = random.randint(1, 4)
    if rannum1 == 1:
        special = chr(random.randint(33, 47))
    elif rannum1 == 2:
        special = chr(random.randint(58, 64))
    elif rannum1 == 3:
        special = chr(random.randint(91, 96))
    else:
        special = chr(random.randint(123, 126))
    val += special
    return val


def uppercalc(val):
    uppercase = chr(random.randint(65, 90))
    val += uppercase
    return val


def lowercalc(val):
    lowercase = chr(random.randint(97, 122))
    val += lowercase
    return val


def generate():
    genpass.configure(state="normal")
    genpass.delete("1.0", "end")
    password = ""

# lower, numbers, special, upper
    if num_var.get() and special_var.get() and upper_var.get() == 1:
        for x in range(0, length.get()):
            rannum = random.randint(1, 4)
            if rannum == 1:
                password = numbercalc(password)
            elif rannum == 2:
                password = specialcalc(password)
            elif rannum == 3:
                password = uppercalc(password)
            else:
                password = lowercalc(password)

#lower, numbers, special
    elif num_var.get() and special_var.get() == 1:
        for x in range(0, length.get()):
            rannum = random.randint(1, 3)
            if rannum == 1:
                password = numbercalc(password)
            elif rannum == 2:
                password = specialcalc(password)
            else:
                password = lowercalc(password)

# lower, numbers, uppercase
    elif num_var.get() and upper_var.get() == 1:
        for x in range(0, length.get()):
            rannum = random.randint(1, 3)
            if rannum == 1:
                password = numbercalc(password)
            elif rannum == 2:
                password = uppercalc(password)
            else:
                password = lowercalc(password)

# lower, special, uppercase
    elif special_var.get() and upper_var.get() == 1:
        for x in range(0, length.get()):
            rannum = random.randint(1, 3)
            if rannum == 1:
                password = specialcalc(password)
            elif rannum == 2:
                password = uppercalc(password)
            else:
                password = lowercalc(password)

#number
    elif num_var.get() == 1:
        for x in range(0, length.get()):
            rannum = random.randint(1, 2)
            if rannum == 1:
                password = lowercalc(password)
            else:
                password = numbercalc(password)


#special
    elif special_var.get() == 1:
        for x in range(0, length.get()):
            rannum = random.randint(1, 2)
            if rannum == 1:
                password = lowercalc(password)
            else:
                password = specialcalc(password)

#uppercase
    elif upper_var.get() == 1:
        for x in range(0, length.get()):
            rannum = random.randint(1, 2)
            if rannum == 1:
                password = lowercalc(password)
            else:
                password = uppercalc(password)

#default lowercase
    else:
        for x in range(0, length.get()):
            password = lowercalc(password)

    genpass.insert("end", ''.join(password))
    genpass.configure(state="disabled")

    root.clipboard_clear()
    root.clipboard_append(password)


#Checkbuttons
num_var = IntVar()
special_var = IntVar()
upper_var = IntVar()

enablenumbers = Checkbutton(root, text="Add Numbers", variable=num_var)
enablenumbers.grid(row=1, column=0)

enablespecial = Checkbutton(root, text="Add Special     ", variable=special_var)
enablespecial.grid(row=2, column=0)

enableuppercase = Checkbutton(root, text="Add Uppercase", variable=upper_var)
enableuppercase.grid(row=3, column=0)

#input length
lengthlabel = Label(root, text="Length of Password:")
lengthlabel.grid(row=0, column=0)

length = IntVar()
inputlength = Entry(root, textvariable=length, width="4")
inputlength.grid(row=0, column=1, sticky="W")


#generate
generatebutton = Button(root, text="generate", command=generate, width=10, height=3, textvariable=True)
generatebutton.grid(row=2, column=1)

#generated password
passlabel = Label(root, text="New Generated Password: ")
passlabel.grid(row=4, column=0)

genpass = Text(root, width="30", height="1")
genpass.grid(row=4, column=1)
genpass.configure(state="disabled")

version = Label(root, text="Version:beta 3.0")
version.grid(row=5, column=3)

default = Label(root, text="Notice: Lowercase is defaulted")
default.grid(row=5, column=1)

copied = Label(root, text="Copied to clipboard")
copied.grid(row=4, column=2)

creation = Label(root, text="Created by: Sygnia")
creation.grid(row=0, column=3)

root.mainloop()
