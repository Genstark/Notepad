import tkinter as tk
from tkinter import filedialog

def save():
    data = [("All tyes", "*.*"),("html file",".html"),
            ("css file",".css"),("javascript file",".js"),
            ("java file",".java"),("python file",".py"),
            ("c++ file",".cpp"),("text file",".txt")]
    
    filedialog.asksaveasfile(filetypes = data, defaultextension = data)

root = tk.Tk()
root.title("App")
root.minsize(400,400)

frame = tk.Frame(root)

btn_1 = tk.Button(text="SAVE AS",
                width=20,
                borderwidth=3,
                command=save)
btn_1.pack(in_=frame,side="left")

btn_2 = tk.Button(text="EXIT",
                width=20,
                borderwidth=3,
                command=quit)
btn_2.pack(in_=frame,side="left")   

frame.pack(side="top",fill="x")

txt = tk.Text(root,
            borderwidth=2)
txt.pack(expand=True,fill="both")

root.mainloop()#end of program
