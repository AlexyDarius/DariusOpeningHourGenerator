def generate_noon_displayer_php(directory_path):
    php_code = f'''<?php
$days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'];
$days_id = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
$options_opening = ['18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '18:45', '20:00'];
$options_closing = ['20:30', '20:45', '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45', '23:00'];

for ($i = 0; $i < count($days); $i++) {{
    $day = $days[$i];
    $day_id = $days_id[$i];

    echo '<div class="form-group mb-3">';
    echo '<label style="margin-right: 2px;" for="' . strtolower($day_id) . '">' . $day . ':</label>';
    echo '<select class="form-label" style="margin-right: 4px;" id="' . strtolower($day_id) . 'Opening" name="' . strtolower($day_id) . 'Opening">';
    foreach ($options_opening as $option) {{
        echo '<option value="' . $option . '">' . $option . '</option>';
    }}
    echo '</select>';
    echo '<select class="form-label" style="margin-right: 4px;" id="' . strtolower($day_id) . 'Closing" name="' . strtolower($day_id) . 'Closing">';
    foreach ($options_closing as $option) {{
        echo '<option value="' . $option . '">' . $option . '</option>';
    }}
    echo '</select>';
    echo '<input type="checkbox" style="margin-right: 2px;margin-left: 8px;" id="closed' .strtolower($day_id) . 'Opening" name="closed' .strtolower($day_id) . 'Opening" unchecked> Fermé';
    echo '</div>';
}}
?>
'''

    with open(f"{directory_path}/opening-hours/requires/noon_displayer.php", "w") as php_file:
        php_file.write(php_code)
        print("noon_displayer.php generated !")
