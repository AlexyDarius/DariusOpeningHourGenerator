def generate_options_json(directory_path):
    json_code = f'''{{
    "options_openingM": ["11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00"],
    "options_closingM": ["12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30"],
    "options_opening": ["18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "18:45", "20:00"],
    "options_closing": ["20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00"]
}}
'''

    with open(f"{directory_path}/opening-hours/requires/options.json", "w") as json_file:
        json_file.write(json_code)
        print("options.json generated !")
