# 'C:\Windows\System32\drivers\etc\hosts'
import time





from tkinter import *

root = Tk()

root.geometry('500x500')
root.title('Trail')


link = StringVar()
def append():
    linkUrl =link.get()
    with open('C:\Windows\System32\drivers\etc\hosts', mode='a') as f:
        if f:
            f.write('\n\t127.0.0.1\t'+linkUrl)
    # return  linkUrl


def deleteFunc():

    with open('C:\Windows\System32\drivers\etc\hosts', 'r') as file:
        file_contents = file.read()

    # Step 3: Modify the contents (remove the added text)
    lines = file_contents.split('\n')
    print(lines)
    for i in range(1):
        lines.pop()
    file_contents = '\n'.join(lines)

    # Step 4: Write the modified contents back to the file
    with open('C:\Windows\System32\drivers\etc\hosts', 'w') as file:
        file.write(file_contents)

def call2():
    append()
    time.sleep(60)
    deleteFunc()

entry = Entry(root, textvariable= link ).pack()
submit = Button(root, text= 'Submit', command=call2).pack()










root.mainloop()
