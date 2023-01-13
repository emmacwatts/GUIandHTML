#GUI practice

import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox, ttk
import buttonsUtil as c
import pandas as pd
import numpy as np

#GUI to display excel files
window = tk.Tk()
window.geometry("500x500")
window.pack_propagate(False) #this means don't resize to text

#Frame for tree view
frame = tk.LabelFrame(window, text = "Excel Data")
frame.place(height = 250, width = 500)

#Frame for open file dialog
frameOpenFile= tk.LabelFrame(window, text = "Open File")
frameOpenFile.place(height = 100, width = 400, rely = 0.65, relx = 0)

#Button1
button1 = tk.Button(frameOpenFile, text = "Browse a File", command = lambda: c.fileDialog())
button1.place(rely = 0.65, relx = 0.5)

#Button2
button2 = tk.Button(frameOpenFile, text = "Load File", command = lambda: c.loadExcelData())
button2.place(rely = 0.65, relx = 0.3)

#Label
labelFile = ttk.Label(frameOpenFile, text = "No File selected")
labelFile.place(relx = 0, rely = 0)

#Treeview widget
tv1 = ttk.Treeview(frame)
tv1.place(relheight = 1, relwidth = 1)

treescrolly = tk.Scrollbar(frame, orient = "vertical", command = tv1.yview)
treescrollx = tk.Scrollbar(frame, orient="horizontal", command = tv1.xview)
tv1.configure(xscrollcommand= treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side = "bottom", fill = "x")
treescrolly.pack(side="right", fill = "y")

window.mainloop()
