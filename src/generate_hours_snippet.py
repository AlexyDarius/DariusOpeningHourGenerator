def generate_hours_snippet_php(directory_path, main_domain):
    php_code = f'''<section style="margin-top: 24px;margin-bottom: 48px;">
        <div class="container">
            <div class="row">
                <div class="col-md-12" style="text-align: center;">
                    <h3 style="font-family: 'Advent Pro', sans-serif;font-weight: bold; font-size:32px; text-decoration: underline;">Nos horaires</h3>
                    
<?php
include $_SERVER['DOCUMENT_ROOT']. '/modules/requires/opening-hours/opening_hours.php'
?>

<script src="https://code.jquery.com/jquery-3.6.0.min.js" defer></script>
<script src="https://www.{main_domain}/modules/opening-hours/js/displayHours.js" defer></script>

                </div>
            </div>
        </div>
    </section>
'''

    with open(f"{directory_path}/opening-hours/requires/opening_hours_snippet.php", "w") as php_file:
        php_file.write(php_code)
        print("opening_hours_snippet.php generated !")
