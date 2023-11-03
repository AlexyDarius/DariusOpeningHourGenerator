def generate_update_hour_noon_php(directory_path, main_domain):
    php_code = f'''<?php
session_start();

require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {{
    $openingHoursFile = '../opening_hours.json';
    
    // Read existing JSON content from the file
    $existingContent = file_get_contents($openingHoursFile);
    $existingData = json_decode($existingContent, true);

    // Update only the fields you want
    $existingData['MondayOpening'] = isset($_POST['mondayOpening']) ? $_POST['mondayOpening'] : 'Closed';
    $existingData['TuesdayOpening'] = isset($_POST['tuesdayOpening']) ? $_POST['tuesdayOpening'] : 'Closed';
    $existingData['WednesdayOpening'] = isset($_POST['wednesdayOpening']) ? $_POST['wednesdayOpening'] : 'Closed';
    $existingData['ThursdayOpening'] = isset($_POST['thursdayOpening']) ? $_POST['thursdayOpening'] : 'Closed';
    $existingData['FridayOpening'] = isset($_POST['fridayOpening']) ? $_POST['fridayOpening'] : 'Closed';
    $existingData['SaturdayOpening'] = isset($_POST['saturdayOpening']) ? $_POST['saturdayOpening'] : 'Closed';
    $existingData['SundayOpening'] = isset($_POST['sundayOpening']) ? $_POST['sundayOpening'] : 'Closed';

    $existingData['MondayClosing'] = isset($_POST['mondayClosing']) ? $_POST['mondayClosing'] : 'Closed';
    $existingData['TuesdayClosing'] = isset($_POST['tuesdayClosing']) ? $_POST['tuesdayClosing'] : 'Closed';
    $existingData['WednesdayClosing'] = isset($_POST['wednesdayClosing']) ? $_POST['wednesdayClosing'] : 'Closed';
    $existingData['ThursdayClosing'] = isset($_POST['thursdayClosing']) ? $_POST['thursdayClosing'] : 'Closed';
    $existingData['FridayClosing'] = isset($_POST['fridayClosing']) ? $_POST['fridayClosing'] : 'Closed';
    $existingData['SaturdayClosing'] = isset($_POST['saturdayClosing']) ? $_POST['saturdayClosing'] : 'Closed';
    $existingData['SundayClosing'] = isset($_POST['sundayClosing']) ? $_POST['sundayClosing'] : 'Closed';

    // Encode the updated data back to JSON
    $updatedOpeningHours = json_encode($existingData, JSON_PRETTY_PRINT);

    // Write the updated content back to the file
    file_put_contents($openingHoursFile, $updatedOpeningHours);

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
        window.location.href = 'https://www.{main_domain}';
    }}, 2000); // 2000 milliseconds (2 seconds)
</script>
'''

    with open(f"{directory_path}/opening-hours/requires/update_hour_noon.php", "w") as php_file:
        php_file.write(php_code)
        print("update_hour_noon.php generated !")
