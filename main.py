from tkinter import filedialog
import tkinter.font as font
from tkinter import *
from packages.deletecopies import *
from style import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


root = Tk()
root.geometry("500x250")
root.resizable(False, False)
root.title("Duplicates Deleter")
root.configure(bg="#303444")
root.iconphoto(False, PhotoImage(file='assets/icon/logo.png'))

folder_path = StringVar(value="Please select a folder")


titleLabel = Label(master=root, text="Duplicates Deleter", bg=primary, fg=white,anchor='w', height=2)
titleLabel.place(relx=middle, rely=0.18, anchor=CENTER)
titleLabel['font'] = titleFont

showLabel = Label(master=root,textvariable=folder_path, bg=secondary, fg=white,anchor='w', height=2)
showLabel.pack(fill='x', padx=30, pady=92)
showLabel['font'] = showLabelFont

selectButton = Button(text="SELECT", command=browse_button, bg=primary, fg=white, height=1)
selectButton.place(relx=0.86, rely=0.45, anchor=CENTER)
selectButton['font'] = browseButtonFont

deleteButton = Button(text="DELETE", command=lambda:check_for_duplicates([folder_path.get()]), bg=white, fg=primary, height=2, width=12)
deleteButton.place(relx=middle, rely=0.76, anchor=CENTER)
deleteButton['font'] = deleteButtonFont

mainloop()
