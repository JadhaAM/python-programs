from cProfile import label
from tkinter import *
main_window = Tk()

#labels
Label(main_window, text="Enter your name").grid(row = 0, column=0)
Label(main_window,text="Whats your age").grid(row=1, column=0)

#Text Input
my_name = Entry(main_window, width =50, borderwidth=5).grid(row=0,column=1)
my_age = Entry(main_window, width =50, borderwidth=5).grid(row=1,column=1)

def on_click():
    print(f"my name is {my_name}, and my age is {my_age}")

#Buttons
Button(main_window, text="click me", command = on_click).grid(row=2, column=1)

main_window.mainloop()




