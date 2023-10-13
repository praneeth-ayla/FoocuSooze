# 'C:\Windows\System32\drivers\etc\hosts'
from tkinter import *
import time
import threading


root = Tk()
root.geometry('400x500')
timeVar = IntVar()
timeVar.set(5)

timer = Entry(root, textvariable=timeVar)
timer.pack()
entryBoxes = Frame(root, width=300, height=400)
entryBoxes.pack_propagate(False)
entryBoxes.pack()
entryList = []
linksUrl = []


def printData():
    for i in entryList:
        link = i.get()
        linksUrl.append(link)
    call2()


def create_new_window():

    global new_window
    root.withdraw()  # Hide the main window
    new_window = Toplevel()  # Create a new top-level window
    new_window.title("Time Left")
    new_window.geometry('400x500')

    # Add widgets to the new window
    label = Label(new_window, text="Wait for 25 mins")
    label.pack()

    button = Button(new_window, text='STOP')
    button.pack()


print(create_new_window.__doc__)


def add_entry():
    entry_frame = Frame(entryBoxes)  # Create a frame for the entry components
    entry_frame.pack()

    # Create an Entry widget
    entry = Entry(entry_frame)
    entry.pack(side=LEFT)
    entryList.append(entry)

    # Create a Delete button
    def delete_entry():
        if entry.get():  # Check if the Entry widget has text
            entryList.remove(entry)  # Remove the Entry from the list
        entry_frame.destroy()  # Remove the entire frame

    delete_button = Button(entry_frame, text="Delete", command=delete_entry)
    delete_button.pack(side=LEFT)


def append():
    with open('trial.txt', mode='a') as f:
        for i in linksUrl:
            f.write('\n\t127.0.0.1\t'+i)
    # return  linkUrl


def deleteFunc():

    with open('trial.txt', 'r') as file:
        file_contents = file.read()

    # Step 3: Modify the contents (remove the added text)
    lines = file_contents.split('\n')
    print(lines)
    for i in range(len(linksUrl)):
        lines.pop()
    file_contents = '\n'.join(lines)

    # Step 4: Write the modified contents back to the file
    with open('trial.txt', 'w') as file:
        file.write(file_contents)


def call2():
    append()
    create_new_window()
    print(timeVar.get())

    def timer_thread():
        time.sleep(timeVar.get())
        # Perform actions after the timer expires here
        deleteFunc()
        root.deiconify()
        new_window.destroy()

    def start_timer():
        timer = threading.Thread(target=timer_thread)
        timer.start()

    # Call this function when you want to start the timer
    start_timer()


addBtn = Button(root, text='add', command=add_entry)
addBtn.pack()

startBtn = Button(root, text='start', command=printData)
startBtn.pack()

root.mainloop()
