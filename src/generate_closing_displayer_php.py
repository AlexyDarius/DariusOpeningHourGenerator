def generate_closing_displayer_php(directory_path):
    php_code = f'''<?php
// Path to the closing.json file
$ClosingFile = "https://www.dariuspizza.fr/modules/opening-hours/closing.json";

// Read the JSON content from the file
$jsonContent = file_get_contents($ClosingFile);
$closingData = json_decode($jsonContent, true);

// Check if display is true
if ($closingData && $closingData['display']) {{
    // Format the dates from JSON (assuming they are in DD/MM/YYYY format)
    $closingDate = DateTime::createFromFormat('d/m/Y', $closingData['ClosingDate'])->format('d/m/Y');
    $reopeningDate = DateTime::createFromFormat('d/m/Y', $closingData['ReopeningDate'])->format('d/m/Y');

    // Start of the styled box
    echo '<div class="closing-announcement-box">';
    echo "Nous serons fermés du " . $closingDate . " au " . $reopeningDate . ".<br>";
    echo $closingData['message'];
    echo '</div>'; // End of the styled box
}}
?>

<style>
.closing-announcement-box {{
    background-color: var(--bs-secondary);
    border: 2px var(--bs-primary);
    border-radius: 10px;
    margin-top: 12px;
    margin-bottom: 12px;
    padding: 15px;
    color: #000; /* Optional: change text color */
    font-weight: bold;
}}
</style>
'''

    with open(f"{directory_path}/opening-hours/requires/closing_displayer.php", "w") as php_file:
        php_file.write(php_code)
        print("closing_displayer.php generated !")
