from tkinter import Tk, Frame
from tkinter.ttk import Notebook

guiMain = Tk()
guiMain.title('5 anh em sieu nhan')
guiMain.geometry('1300x700')
guiMain.resizable(False, False)

# Create Tab Layout
tablayout = Notebook(guiMain)
tablayout.pack(fill='both')

# Create Main Tab
mainTab = Frame(tablayout)
mainTab.pack(fill="both")
tablayout.add(mainTab, text='Main')     # add mainTab to tab layout
# Data in Main Tab


# Create Campaign Tab
campTab = Frame(tablayout)
campTab.pack(fill="both")
tablayout.add(campTab, text='Camp')     # add campTab to tab layout
# Data in Campaign Tab

# Create BM Page Tab
bmPageTab = Frame(tablayout)
bmPageTab.pack(fill="both")
tablayout.add(bmPageTab, text='BM Page')     # add bmPageTab to tab layout
# Data in BM Page Tab

# Create Card Gen Tab
cardGenTab = Frame(tablayout)
cardGenTab.pack(fill="both")
tablayout.add(cardGenTab, text='Card Gen')     # add cardGenTab to tab layout
# Data in Card Gen Tab

"""

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
    acc = api.login(fbUsername=fbUsername, fbPassword=fbPass, code_2fa=code2fa)
    acc.setUp()
    acc.testLogin()

Button(guiMain, text='Login', command=run).grid(row=3, column=0, columnspan=2)
"""

guiMain.mainloop()