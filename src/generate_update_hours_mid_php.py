def generate_update_hour_mid_php(directory_path, main_domain):
    php_code = f'''<?php
session_start();

require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {{
    $OpeningHoursFile = '../opening_hours.json';
    
    // Read existing JSON content from the file
    $existingContent = file_get_contents($OpeningHoursFile);
    $existingData = json_decode($existingContent, true);

    // Update only the fields you want
    $existingData['MondayOpeningM'] = isset($_POST['mondayOpeningM']) ? $_POST['mondayOpeningM'] : 'Closed';
    $existingData['TuesdayOpeningM'] = isset($_POST['tuesdayOpeningM']) ? $_POST['tuesdayOpeningM'] : 'Closed';
    $existingData['WednesdayOpeningM'] = isset($_POST['wednesdayOpeningM']) ? $_POST['wednesdayOpeningM'] : 'Closed';
    $existingData['ThursdayOpeningM'] = isset($_POST['thursdayOpeningM']) ? $_POST['thursdayOpeningM'] : 'Closed';
    $existingData['FridayOpeningM'] = isset($_POST['fridayOpeningM']) ? $_POST['fridayOpeningM'] : 'Closed';
    $existingData['SaturdayOpeningM'] = isset($_POST['saturdayOpeningM']) ? $_POST['saturdayOpeningM'] : 'Closed';
    $existingData['SundayOpeningM'] = isset($_POST['sundayOpeningM']) ? $_POST['sundayOpeningM'] : 'Closed';

    $existingData['MondayClosingM'] = isset($_POST['mondayClosingM']) ? $_POST['mondayClosingM'] : 'Closed';
    $existingData['TuesdayClosingM'] = isset($_POST['tuesdayClosingM']) ? $_POST['tuesdayClosingM'] : 'Closed';
    $existingData['WednesdayClosingM'] = isset($_POST['wednesdayClosingM']) ? $_POST['wednesdayClosingM'] : 'Closed';
    $existingData['ThursdayClosingM'] = isset($_POST['thursdayClosingM']) ? $_POST['thursdayClosingM'] : 'Closed';
    $existingData['FridayClosingM'] = isset($_POST['fridayClosingM']) ? $_POST['fridayClosingM'] : 'Closed';
    $existingData['SaturdayClosingM'] = isset($_POST['saturdayClosingM']) ? $_POST['saturdayClosingM'] : 'Closed';
    $existingData['SundayClosingM'] = isset($_POST['sundayClosingM']) ? $_POST['sundayClosingM'] : 'Closed';

    // Encode the updated data back to JSON
    $updatedOpeningHours = json_encode($existingData, JSON_PRETTY_PRINT);

    // Write the updated content back to the file
    file_put_contents($OpeningHoursFile, $updatedOpeningHours);

    $response = ['message' => 'Opening hours updated successfully'];
    echo json_encode($response);

}} else {{
    http_response_code(405); // Method Not Allowed
    echo json_encode(['error' => 'Method not allowed']);
}}

?>
<script>
    // Redirect to the desired page after a short delay (e.g., 2 seconds)
    setTimeout(function() {{
        window.location.href = 'https://{main_domain}';
    }}, 2000); // 2000 milliseconds (2 seconds)
</script>


'''

    with open(f"{directory_path}/opening-hours/requires/update_hours_mid.php", "w") as php_file:
        php_file.write(php_code)
        print("update_hour_mid.php generated !")
