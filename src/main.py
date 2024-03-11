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
from generate_displayHours_js import generate_displayHours_js
from generate_sectionDisplayer_js import generate_sectionDisplayer_js
from generate_openingHoursMid_js import generate_openingOpeningHoursMid_js
from generate_openingHoursNoon_js import generate_openingOpeningHoursNoon_js
from generate_hours_snippet import generate_hours_snippet_php
from generate_closing_json import generate_closing_json
from generate_updateClosing_js import generate_updateClosing_js
from generate_closing_displayer_php import generate_closing_displayer_php
from generate_update_closing_php import generate_update_closing_php
from generate_options_json import generate_options_json

class OpeningTime:
    MID_NOON = "M/N"
    MORNING_AFTERNOON = "AM/PM"
    CONTINUOUS = "C"

def on_checkbox_click(selected_option):
    # Uncheck all other checkboxes
    for option, var in checkbox_vars.items():
        if option != selected_option:
            var.set(False)

def get_selected_option():
    # Return the option whose checkbox is checked
    for option, var in checkbox_vars.items():
        if var.get():
            return option
    return None  # Return None or a similar value if no checkbox is checked

def toggle_am_pm_fields():
    # Show the AM/PM fields if MID_NOON or MORNING_AFTERNOON is selected
    if checkbox_vars[OpeningTime.MID_NOON].get() or checkbox_vars[OpeningTime.MORNING_AFTERNOON].get():
        am_pm_frame.pack(after=checkbox_frame)
    else:
        am_pm_frame.pack_forget()

def generate_files():
    directory_path = directory_var.get()
    main_domain = main_domain_entry.get()
    full_body_tag = full_body_tag_entry.get("1.0", "end-1c")
    bg_color = color_entry1.get()
    primary_color = color_entry2.get()
    opening_option = get_selected_option()

    if (all([directory_path, main_domain, full_body_tag, bg_color, primary_color]) and opening_option is not None) :
        # Generate tree path
        generate_arbo(directory_path)
        generate_edit_hours_php(directory_path, main_domain, full_body_tag, bg_color, primary_color, opening_option)
        generate_opening_hours_json(directory_path)
        generate_mid_displayer_php(directory_path)
        generate_noon_displayer_php(directory_path)
        generate_opening_displayer_php(directory_path)
        generate_update_hour_mid_php(directory_path, main_domain)
        generate_update_hour_noon_php(directory_path, main_domain)
        generate_disableDropdown_js(directory_path)
        generate_displayHours_js(directory_path, main_domain, opening_option)
        generate_sectionDisplayer_js(directory_path, opening_option)
        generate_openingOpeningHoursMid_js(directory_path)
        generate_openingOpeningHoursNoon_js(directory_path)
        generate_hours_snippet_php(directory_path, main_domain)
        generate_closing_json(directory_path)
        generate_updateClosing_js(directory_path)
        generate_closing_displayer_php(directory_path, main_domain)
        generate_update_closing_php(directory_path, main_domain)
        generate_options_json(directory_path)
        
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

opening_option_label = tk.Label(app, text="Opening option :")
opening_option_label.pack()

# Frame to hold the checkboxes
checkbox_frame = tk.Frame(app)
checkbox_frame.pack()

# Dictionary to hold the variables associated with each checkbox
global checkbox_vars

checkbox_vars = {
    OpeningTime.MID_NOON: tk.BooleanVar(),
    OpeningTime.MORNING_AFTERNOON: tk.BooleanVar(),
    OpeningTime.CONTINUOUS: tk.BooleanVar(),
}

# Create checkboxes for each option and pack them in the same line
for option, var in checkbox_vars.items():
    checkbox = tk.Checkbutton(checkbox_frame, text=option, variable=var, 
                              command=lambda opt=option: on_checkbox_click(opt))
    checkbox.pack(side=tk.LEFT)

# After checkboxes, pack the AM/PM frame (initially hidden)
global am_pm_frame
am_pm_frame = tk.Frame(app)

# AM/PM input fields
for _ in range(4):
    AMPM_entry = tk.Entry(am_pm_frame, width=6)
    AMPM_entry.pack(side=tk.LEFT, padx=5)

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
