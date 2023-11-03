def generate_opening_displayer_php(directory_path):
    php_code = f'''<div id="mondayHours" style="text-align: center;"></div>
<div id="tuesdayHours" style="text-align: center;"></div>
<div id="wednesdayHours" style="text-align: center;"></div>
<div id="thursdayHours" style="text-align: center;"></div>
<div id="fridayHours" style="text-align: center;"></div>
<div id="saturdayHours" style="text-align: center;"></div>
<div id="sundayHours" style="text-align: center;"></div>
'''

    with open(f"{directory_path}/opening-hours/requires/opening_hours.php", "w") as php_file:
        php_file.write(php_code)
        print("oepning_hours.php generated !")
