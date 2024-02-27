def generate_updateClosing_js(directory_path):
    js_code = f'''// Function to update closing dates
function updateClosing() {{
    // Get form data
    const closingDate = document.getElementById('closingDate').value;
    const reopeningDate = document.getElementById('reopeningDate').value;
    const message = document.getElementById('message').value;
    const closingMode = document.getElementById('closingMode').checked;

    // Prepare data for sending
    const formData = new FormData();
    formData.append('closingDate', closingDate);
    formData.append('reopeningDate', reopeningDate);
    formData.append('message', message);
    formData.append('closingMode', closingMode ? 'on' : '');

    // Send data to the update_closing.php file
    fetch('requires/update_closing.php', {{
        method: 'POST',
        body: formData
    }})
    .then(response => response.json())
    .then(data => {{
        console.log(data); // Log the response from the server
        // Optionally, redirect or display a success message
    }})
    .catch(error => {{
        console.error('Error updating closing dates:', error);
    }});
}}
'''

    with open(f"{directory_path}/opening-hours/js/updateClosing.js", "w") as js_file:
        js_file.write(js_code)
        print("updateClosing.js generated !")
