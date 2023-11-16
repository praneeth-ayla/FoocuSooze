# 'C:\Windows\System32\drivers\etc\hosts'
from tkinter import *
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
    


def stop_timer():
    global entryList
    global linksUrl
    deleteFunc()
    root.deiconify()
    new_window.destroy()


def stop_timer():
    global entryList
    global linksUrl
    deleteFunc()
    root.deiconify()
    new_window.destroy()


def create_new_window():
    global new_window
    global remaining_time 

    remaining_time = timeVar.get()*60
    root.withdraw()  # Hide the main window
    new_window = Toplevel()  # Create a new top-level window
    new_window.title("Foocusooze")
    new_window.geometry('400x500')
    stopBtn = Button(new_window,text='STOP',command=stop_timer)
    stopBtn.pack()
    def update_timer():
        # remaining_time = timeVar.get()*60
        global remaining_time
        if remaining_time > 0:
            remaining_time -= 1
            mins = remaining_time//60
            secs = remaining_time%60
            timer_label.config(text=f"Time Left: {mins}: {secs} sec")
            timer_label.after(1000, update_timer)
        else:
            timer_label.config(text="Time's up!")
            if len(linksUrl)!=0:
                stop_timer()
    
    timer_label = Label(new_window, text=f"Time Left: {remaining_time} sec", font=("Helvetica", 16))
    timer_label.pack(padx=20, pady=20)
    
    update_timer()



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




def deleteFunc():
    global entryList
    global linksUrl
    with open('C:\Windows\System32\drivers\etc\hosts', 'r') as file:
        file_contents = file.read()

    # Step 3: Modify the contents (remove the added text)
    lines = file_contents.split('\n')
    print(lines)
    for i in range(totalLinks):
        lines.pop()
    file_contents = '\n'.join(lines)

    # Step 4: Write the modified contents back to the file
    with open('C:\Windows\System32\drivers\etc\hosts', 'w') as file:
        file.write(file_contents)

def append():
    global totalLinks
    global linksUrl
    totalLinks= len(linksUrl)
    print(linksUrl)
    with open("C:\Windows\System32\drivers\etc\hosts", mode='a') as f:
        for i in linksUrl:
            f.write('\n\t127.0.0.1\t'+i)
    linksUrl = []
    
def call2():
    append()
    
    
    create_new_window()
    print(timeVar.get())

    

addBtn = Button(root, text='add', command=add_entry)
addBtn.pack()

startBtn = Button(root, text='start', command=printData)
startBtn.pack()

root.mainloop()


