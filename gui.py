from tkinter import *
from tkinter import ttk

root = Tk()
root.title("underwolf")

mainframe = ttk.Frame(root, padding="20 20 20 20", borderwidth=2, relief='sunken')
mainframe.grid(column=0, row=0, sticky=N)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


ttk.Entry(mainframe, state='readonly').grid(column=2, row=1, sticky=N)
ttk.Button(mainframe,text="Generate PW").grid(column=2, row=2, sticky=N)
ttk.Button(mainframe,text="Copy to Clipboard").grid(column=2, row=3, sticky=N)
ttk.Label(mainframe, text="test").grid(column=3, row=1, padx=1000, sticky=N)


for child in mainframe.winfo_children():
     child.grid_configure(padx=5, pady=5)

root.bind("<Return>, generate")

root.mainloop()