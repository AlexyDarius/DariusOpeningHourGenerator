def generate_sectionDisplayer_js(directory_path, opening_option):
    js_code = f'''// Get references to the buttons and sections
const editMidiButton = document.querySelector('#edit-midi-button');
const editSoirButton = document.querySelector('#edit-soir-button');
const editClosingButton = document.querySelector('#edit-closing-button');
const midiSection = document.querySelector('#midi-section');
const soirSection = document.querySelector('#soir-section');
const closingSection = document.querySelector('#closing-section');

// Hide both sections by default
midiSection.style.display = 'none';
soirSection.style.display = 'none';
closingSection.style.display = 'none';

// Add click event listeners to the buttons
editMidiButton.addEventListener('click', () => {{
    midiSection.style.display = 'block';
    soirSection.style.display = 'none';
    closingSection.style.display = 'none';
}});

editSoirButton.addEventListener('click', () => {{
    midiSection.style.display = 'none';
    soirSection.style.display = 'block';
    closingSection.style.display = 'none';
}});

editClosingButton.addEventListener('click', () => {{
    midiSection.style.display = 'none';
    soirSection.style.display = 'none';
    closingSection.style.display = 'block';
}});

'''
    
    if opening_option == "C" : 

        js_code = f'''// Get references to the buttons and sections
const editMidiButton = document.querySelector('#edit-midi-button');
const editSoirButton = document.querySelector('#edit-soir-button');
const editClosingButton = document.querySelector('#edit-closing-button');
const midiSection = document.querySelector('#midi-section');
const soirSection = document.querySelector('#soir-section');
const closingSection = document.querySelector('#closing-section');

// Hide both sections by default
soirSection.style.display = 'none';
closingSection.style.display = 'none';

// Add click event listeners to the buttons
editSoirButton.addEventListener('click', () => {{
    soirSection.style.display = 'block';
    closingSection.style.display = 'none';
}});

editClosingButton.addEventListener('click', () => {{
    soirSection.style.display = 'none';
    closingSection.style.display = 'block';
}});

'''

    with open(f"{directory_path}/opening-hours/js/sectionDisplayer.js", "w") as js_file:
        js_file.write(js_code)
        print("sectionDisplayer.js generated !")
