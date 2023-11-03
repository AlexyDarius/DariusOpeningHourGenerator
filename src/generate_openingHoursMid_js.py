def generate_openingOpeningHoursMid_js(directory_path):
    js_code = f'''// Function to update opening hours
function updateOpeningHoursMid() {{
    // Loop through each day to gather the data
    const days_openingM = ['mondayOpeningM', 'tuesdayOpeningM', 'wednesdayOpeningM', 'thursdayOpeningM', 'fridayOpeningM', 'saturdayOpeningM', 'sundayOpeningM'];
    const closingM = ['mondayClosingM', 'tuesdayClosingM', 'wednesdayClosingM', 'thursdayClosingM', 'fridayClosingM', 'saturdayClosingM', 'sundayClosingM'];
    const requestData = {{}};

    days_openingM.forEach(function (dayM) {{
        const selectElement = document.getElementById(dayM);
        const checkboxElement = document.getElementById('closed' + dayM.charAt(0).toUpperCase() + dayM.slice(1)); // Construct checkbox ID based on the day

        const isClosed = checkboxElement.checked;
        const openingHoursM = isClosed ? 'Closed' : selectElement.value;

        requestData[dayM] = openingHoursM;
    }});

    closingM.forEach(function (dayM) {{
        const selectElement = document.getElementById(dayM);
        const checkboxElement = document.getElementById('closed' + dayM.charAt(0).toUpperCase() + dayM.slice(1)); // Construct checkbox ID based on the day

        const isClosed = checkboxElement.checked;
        const closingHoursM = isClosed ? 'Closed' : selectElement.value;

        requestData[dayM] = closingHoursM;
    }});

    // Update opening hours in the JSON file
    fetch('../requires/update_hours_mid.php', {{
        method: 'POST',
        body: JSON.stringify(requestData),
        headers: {{
            'Content-Type': 'application/json'
        }}
    }})
    .then(response => response.json())
    .then(data => {{
        console.log(data); // Log the response from the server

        // Fetch and display updated opening hours
        fetchAndDisplayOpeningHours();
    }})
    .catch(error => {{
        console.error('Error updating opening hours:', error);
    }});
}}
'''

    with open(f"{directory_path}/opening-hours/js/updateOpeningHoursMid.js", "w") as js_file:
        js_file.write(js_code)
        print("updateOpeningHoursMid.js generated !")
