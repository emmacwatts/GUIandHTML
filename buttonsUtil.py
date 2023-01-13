#Commands

def fileDialog():
    filename = filedialog.askopenfilename(initialdir = "/", 
    title = "Select a File", filetype = (("xlsx Files", "*.xlsx"),
    ("All Files", "*.*")))
    labelFile["text"]= filename
    return None

def loadExcelData():
    filePath = labelFile["text"]
    try:
        excelFilename = r"{}".format(filePath)
        df.pd.read_excel(excel_filename)
    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid.")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {filePath}")
        return None
    
    clearData()

    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text = column)

    dfRows = df.to_numpy.tolist()
    for row in dfRows:
        tv1.insert("", "end", value = row)

def clearData():
    tv1.delete(*tv1.get_children)