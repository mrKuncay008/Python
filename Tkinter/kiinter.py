# from tkinter import *
# from tkinter import ttk 

# root = Tk()
# ttk.Button(root, text = "Hallo Aisma Meoo").grid()
# root.mainloop()

import wx

app = wx.app()

frm = wx.Frame(None, title = "Hallo World")

frm.Show()

app.MainLoop()