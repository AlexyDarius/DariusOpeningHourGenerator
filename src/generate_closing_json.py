def generate_closing_json(directory_path):
    json_code = f'''{{
    "ClosingDate": "01\/01\/2024",
    "ReopeningDate": "01\/02\/2024",
    "display": false,
    "message": "test"
}}
'''

    with open(f"{directory_path}/opening-hours/closing.json", "w") as json_file:
        json_file.write(json_code)
        print("closing.json generated !")
