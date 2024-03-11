def generate_noon_displayer_php(directory_path):
    php_code = f'''<?php
$days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'];
$days_id = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

// Read JSON file
$jsonData = file_get_contents("requires/options.json");
$options = json_decode($jsonData, true);

$options_opening = $options['options_opening'];
$options_closing = $options['options_closing'];

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
