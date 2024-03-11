def generate_mid_displayer_php(directory_path):
    php_code = f'''<?php
$daysM = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'];
$days_idM = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

// Read JSON file
$jsonData = file_get_contents("requires/options.json");
$options = json_decode($jsonData, true);

$options_openingM = $options['options_openingM'];
$options_closingM = $options['options_closingM'];

for ($i = 0; $i < count($daysM); $i++) {{
    $dayM = $daysM[$i];
    $day_idM = $days_idM[$i];

    echo '<div class="form-group mb-3">';
    echo '<label style="margin-right: 2px;" for="' . strtolower($day_idM) . '">' . $dayM . ':</label>';
    echo '<select class="form-label" style="margin-right: 4px;" id="' . strtolower($day_idM) . 'OpeningM" name="' . strtolower($day_idM) . 'OpeningM">';
    foreach ($options_openingM as $optionM) {{
        echo '<option value="' . $optionM . '">' . $optionM . '</option>';
    }}
    echo '</select>';
    echo '<select class="form-label" style="margin-right: 4px;" id="' . strtolower($day_idM) . 'ClosingM" name="' . strtolower($day_idM) . 'ClosingM">';
    foreach ($options_closingM as $optionM) {{
        echo '<option value="' . $optionM . '">' . $optionM . '</option>';
    }}
    echo '</select>';
    echo '<input type="checkbox" style="margin-right: 2px;margin-left: 8px;" id="closed' .strtolower($day_idM) . 'OpeningM" name="closed' .strtolower($day_idM) . 'OpeningM" unchecked> Fermé';
    echo '</div>';
}}
?>
'''

    with open(f"{directory_path}/opening-hours/requires/mid_displayer.php", "w") as php_file:
        php_file.write(php_code)
        print("mid_displayer.php generated !")
