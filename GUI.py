from tkinter import *
from FB_test import *

guiMain = Tk()
guiMain.title('5 anh em sieu nhan')
guiMain.geometry('500x400')


Label(guiMain, text='Account:').grid(row=0, column=0)
Label(guiMain, text='Password:').grid(row=1, column=0)
Label(guiMain, text='Code2FA:').grid(row=2, column=0)

e_acc = Entry(guiMain, width=60, borderwidth=5)
e_acc.grid(row=0, column=1)
e_pass = Entry(guiMain, width=60, borderwidth=5)
e_pass.grid(row=1, column=1)
e_code2fa = Entry(guiMain, width=60, borderwidth=5)
e_code2fa.grid(row=2, column=1)

def run():
    fbUsername = e_acc.get()
    fbPass = e_pass.get()
    code2fa = e_code2fa.get()
    # print(fbUsername)
    # print(fbPass)
    acc = LoginTest(fbUsername=fbUsername, fbPassword=fbPass, code2fa=e_code2fa)
    acc.setUp()
    acc.testLogin()

Button(guiMain, text='Login', command=run).grid(row=3, column=0, columnspan=2)

guiMain.mainloop()