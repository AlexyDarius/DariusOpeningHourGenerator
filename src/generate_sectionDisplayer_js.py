def generate_sectionDisplayer_js(directory_path, main_domain):
    js_code = f'''// Get references to the buttons and sections
const editMidiButton = document.querySelector('#edit-midi-button');
const editSoirButton = document.querySelector('#edit-soir-button');
const midiSection = document.querySelector('#midi-section');
const soirSection = document.querySelector('#soir-section');

// Hide both sections by default
midiSection.style.display = 'none';
soirSection.style.display = 'none';

// Add click event listeners to the buttons
editMidiButton.addEventListener('click', () => {{
    midiSection.style.display = 'block';
    soirSection.style.display = 'none';
}});

editSoirButton.addEventListener('click', () => {{
    midiSection.style.display = 'none';
    soirSection.style.display = 'block';
}});
'''

    with open(f"{directory_path}/opening-hours/js/sectionDisplayer.js", "w") as js_file:
        js_file.write(js_code)
        print("sectionDisplayer.js generated !")
