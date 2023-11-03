def generate_opening_hours_json(directory_path):
    json_code = f'''{{
    "MondayOpening": "Closed",
    "TuesdayOpening": "18:00",
    "WednesdayOpening": "18:00",
    "ThursdayOpening": "18:00",
    "FridayOpening": "18:00",
    "SaturdayOpening": "18:00",
    "SundayOpening": "18:00",
    "MondayClosing": "Closed",
    "TuesdayClosing": "20:30",
    "WednesdayClosing": "20:30",
    "ThursdayClosing": "20:30",
    "FridayClosing": "20:30",
    "SaturdayClosing": "20:30",
    "SundayClosing": "20:30",
    "MondayOpeningM": "11:00",
    "TuesdayOpeningM": "11:00",
    "WednesdayOpeningM": "Closed",
    "ThursdayOpeningM": "11:00",
    "FridayOpeningM": "11:00",
    "SaturdayOpeningM": "11:00",
    "SundayOpeningM": "11:00",
    "MondayClosingM": "12:30",
    "TuesdayClosingM": "12:30",
    "WednesdayClosingM": "Closed",
    "ThursdayClosingM": "12:30",
    "FridayClosingM": "12:30",
    "SaturdayClosingM": "12:30",
    "SundayClosingM": "12:30"
}}
'''

    with open(f"{directory_path}/opening-hours/opening_hours.json", "w") as php_file:
        php_file.write(json_code)
        print("opening-hours.json generated !")
