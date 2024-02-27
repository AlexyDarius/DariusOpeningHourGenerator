def generate_update_closing_php(directory_path, main_domain):
    php_code = f'''<?php
session_start();

require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php';

function convertDateToDDMMYYYY($date) {{
    if ($date) {{
        $dateObject = DateTime::createFromFormat('Y-m-d', $date);
        return $dateObject ? $dateObject->format('d/m/Y') : null;
    }}
    return null;
}}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {{
    $ClosingFile = '../closing.json';
    
    // Read existing JSON content from the file
    $existingContent = file_get_contents($ClosingFile);
    $existingData = json_decode($existingContent, true);

    // Convert and update fields from the form
    $existingData['ClosingDate'] = isset($_POST['closingDate']) ? convertDateToDDMMYYYY($_POST['closingDate']) : $existingData['ClosingDate'];
    $existingData['ReopeningDate'] = isset($_POST['reopeningDate']) ? convertDateToDDMMYYYY($_POST['reopeningDate']) : $existingData['ReopeningDate'];
    $existingData['message'] = isset($_POST['message']) ? $_POST['message'] : $existingData['message'];
    $existingData['display'] = isset($_POST['closingMode']) ? true : false;

    // Encode the updated data back to JSON
    $updatedClosing = json_encode($existingData, JSON_PRETTY_PRINT);

    // Write the updated content back to the file
    file_put_contents($ClosingFile, $updatedClosing);

    $response = ['message' => 'Closing updated successfully'];
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

    with open(f"{directory_path}/opening-hours/update-closing.php", "w") as php_file:
        php_file.write(php_code)
        print("update-closing.php generated !")
