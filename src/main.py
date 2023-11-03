import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from generate_arbo import generate_arbo
from generate_edit_hours_php import generate_edit_hours_php
from generate_opening_hours_json import generate_opening_hours_json
from generate_mid_displayer_php import generate_mid_displayer_php
from generate_noon_displayer_php import generate_noon_displayer_php
from generate_opening_displayer_php import generate_opening_displayer_php
from generate_update_hours_mid_php import generate_update_hour_mid_php
from generate_update_hours_noon_php import generate_update_hour_noon_php
from generate_disableDropdown_js import generate_disableDropdown_js

def generate_files():
    directory_path = directory_var.get()
    main_domain = main_domain_entry.get()
    full_body_tag = full_body_tag_entry.get("1.0", "end-1c")
    bg_color = color_entry1.get()
    primary_color = color_entry2.get()

    if all([directory_path, main_domain, full_body_tag, bg_color, primary_color]):
        # Generate tree path
        generate_arbo(directory_path)
        generate_edit_hours_php(directory_path, main_domain, full_body_tag, bg_color, primary_color)
        generate_opening_hours_json(directory_path)
        generate_mid_displayer_php(directory_path)
        generate_noon_displayer_php(directory_path)
        generate_opening_displayer_php(directory_path)
        generate_update_hour_mid_php(directory_path, main_domain)
        generate_update_hour_noon_php(directory_path, main_domain)
        generate_disableDropdown_js(directory_path)
        
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

def open_color_picker1():
    color = colorchooser.askcolor()[1]
    color_entry1.delete(0, tk.END)
    color_entry1.insert(0, color)

def open_color_picker2():
    color = colorchooser.askcolor()[1]
    color_entry2.delete(0, tk.END)
    color_entry2.insert(0, color)

app = tk.Tk()
app.title("DariusDev Opening Hours Generator")

directory_var = tk.StringVar()

directory_label = tk.Label(app, text="Select Directory:")
directory_label.pack()
directory_entry = tk.Entry(app, textvariable=directory_var, width = 50)
directory_entry.pack()

select_directory_button = tk.Button(app, text="Browse", command=select_directory)
select_directory_button.pack()

main_domain_label = tk.Label(app, text="Enter the main domain (e.g. dariusdev.fr, without www. !) :")
main_domain_label.pack()
main_domain_entry = tk.Entry(app)
main_domain_entry.pack()

full_body_tag_label = tk.Label(app, text="Full Body tag (e.g. <body style=...>) :")
full_body_tag_label.pack()
full_body_tag_entry = tk.Text(app, width=50, height=5)
full_body_tag_entry.pack()

# Create an Entry widget for entering color in hex format
color_entry_label = tk.Label(app, text="Enter bg color of the buttons (#hex format) :")
color_entry_label.pack()
color_entry1 = tk.Entry(app)
color_entry1.pack()

# Create a Button to open the color picker
color_picker_button = tk.Button(app, text="Or use color picker", command=open_color_picker1)
color_picker_button.pack()

# Create an Entry widget for entering color in hex format
color_entry_label = tk.Label(app, text="Enter primary color of the buttons (#hex format) :")
color_entry_label.pack()
color_entry2 = tk.Entry(app)
color_entry2.pack()

# Create a Button to open the color picker
color_picker_button = tk.Button(app, text="Or use color picker", command=open_color_picker2)
color_picker_button.pack()

blank_label = tk.Label(app, text="")
blank_label.pack()

generate_button = tk.Button(app, text="Generate", command=generate_files)
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
