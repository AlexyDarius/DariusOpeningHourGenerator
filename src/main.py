import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from generate_arbo import generate_arbo

def generate_files():
    directory_path = directory_var.get()

    if all([directory_path]):
        # Generate tree path
        generate_arbo(directory_path)
        
        result_label.config(text="Opening Hours files have been generated.")

        print("Opening Hours files well generated, don't forget to minify !")
        print("Read readme.txt for implementation.\n")

        app.quit()
    else:
        result_label.config(text="Please provide all required fields.")

def select_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_var.set(directory_path)

app = tk.Tk()
app.title("DariusDev Opening Hours Generator")

directory_var = tk.StringVar()

directory_label = tk.Label(app, text="Select Directory:")
directory_label.pack()
directory_entry = tk.Entry(app, textvariable=directory_var, width = 50)
directory_entry.pack()

select_directory_button = tk.Button(app, text="Browse", command=select_directory)
select_directory_button.pack()

blank_label = tk.Label(app, text="")
blank_label.pack()

generate_button = tk.Button(app, text="Generate", command=generate_files)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
