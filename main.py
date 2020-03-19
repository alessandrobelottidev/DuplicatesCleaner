from tkinter import filedialog
import tkinter.font as font
from tkinter import *
from packages.deletecopies import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askdirectory()
    if filename != "":
        folder_path.set(filename)
    finished_statement.set("Click the button to start cleaning")


root = Tk()
root.geometry("500x250")
root.resizable(False, False)
root.title("Duplicates Deleter")
root.configure(bg="#303444")
root.iconphoto(False, PhotoImage(file='assets/icon/logo.png'))

folder_path = StringVar(value="Please select a folder")
finished_statement = StringVar(value="Click the button to start cleaning")


# Styling
titleFont = font.Font(size=18, weight=font.BOLD)
showLabelFont = font.Font(family="Helvetica")
finishedFont = font.Font(family="Helvetica", size=8)
browseButtonFont = font.Font(family="Arial", size=10, weight=font.BOLD)
deleteButtonFont = font.Font(family="Arial", size=12, weight=font.BOLD)

primary = "#303444"
secondary = "#3E4458"
white = "#fff"

middle = 0.5


titleLabel = Label(master=root, text="Duplicates Deleter", bg=primary, fg=white,anchor='w', height=2)
titleLabel.place(relx=middle, rely=0.18, anchor=CENTER)
titleLabel['font'] = titleFont

showLabel = Label(master=root,textvariable=folder_path, bg=secondary, fg=white,anchor='w', height=2)
showLabel.pack(fill='x', padx=30, pady=92)
showLabel['font'] = showLabelFont

selectButton = Button(text="SELECT", command=browse_button, bg=primary, fg=white, height=1)
selectButton.place(relx=0.86, rely=0.45, anchor=CENTER)
selectButton['font'] = browseButtonFont

deleteButton = Button(text="DELETE", command=lambda:check_for_duplicates([folder_path.get()], finished_statement), bg=white, fg=primary, height=2, width=12)
deleteButton.place(relx=middle, rely=0.76, anchor=CENTER)
deleteButton['font'] = deleteButtonFont

finishedLabel = Label(master=root,textvariable=finished_statement, bg=primary, fg=white,anchor='w')
finishedLabel.place(relx=middle, rely=0.93, anchor=CENTER)
finishedLabel['font'] = finishedFont

mainloop()
