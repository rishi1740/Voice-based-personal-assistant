# button_callback.py
from tkinter import *
import jarvis
root = Tk()

# Create a button with a custom callback
def start():
    jarvis.mainprogram()# Prints to console not the GUI

def stop():
    jarvis.jarvi("exit")
root = Tk()
# Create a button that will destroy the main window when clicked
exit_button = Button(root, text='Exit Program', command=root.destroy())
exit_button.pack()

prin = Button(root, text='Stop', command=stop)
prin.pack()

b1=Button(root,image='jarvis.jpg',text="stop")
b1.grid(row=25,column=15)


print_button = Button(root, text='Start', command=start)
print_button.pack()

root.mainloop()
