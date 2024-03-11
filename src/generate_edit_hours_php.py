def generate_edit_hours_php(directory_path, main_domain, full_body_tag, bg_color, primary_color, opening_option):

    if opening_option == "M/N" :
        text1 = "du matin"
        text2 = "de l'après-midi"
    elif opening_option == "AM/PM" :
        text1 = "du midi"
        text2 = "du soir"

    php_code = f'''<?php
require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php';
include $_SERVER['DOCUMENT_ROOT']. '/includes/head.php'
?>

    <title>Votre gestonnaire d'horaires d'ouverture</title>
    <script src= "js/disableDropdown.js"></script>
</head>

{full_body_tag}

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/navbar.php'
?>

    <h1 class="text-center" style="margin-top: 12px;font-weight: bold;text-decoration:  underline;">Éditer vos horaires d'ouverture</h1>
    <section style="margin-top: 32px;margin-bottom: 32px;">
        <div class="container">
            <div class="row" style="margin-bottom: 24px">
                <div style="text-align: center"><button class="btn btn-primary" type="button" style="color: {primary_color}; background-color: {bg_color}; border: none" id="edit-closing-button">Mode fermeture</button>
                </div>
            </div>
            <div class="row">
                <div class="col-6 col-md-6 d-flex justify-content-center"><button class="btn btn-primary" type="button" style="color: {primary_color}; background-color: {bg_color}; border: none" id="edit-midi-button">Éditer horaires {text1}</button>
                </div>
                <div class="col-6 col-md-6 d-flex justify-content-center"><button class="btn btn-primary" type="button" style="color: {primary_color}; background-color: {bg_color}; border: none" id="edit-soir-button">Éditer horaires {text2}</button>
                </div>
            </div>
        </div>
    </section>
    <section class="position-relative py-4 py-xl-5" id="midi-section">
        <div class="container position-relative">
            <div class="row d-flex justify-content-center">
                <div class="col-md-8 col-lg-6 col-xl-5 col-xxl-4">
                    <div class="card mb-5">
                        <div class="card-body p-sm-5">
                        <h2 class="text-center mb-4">Éditer vos horaires {text1} ici</h2>
                            <form method="post" action="requires/update_hours_mid.php" onsubmit="updateOpeningHoursMid(); return false;">

                                <?php
                                    require $_SERVER['DOCUMENT_ROOT']. '/modules/opening-hours/requires/mid_displayer.php'
                                ?>

                                <div><button style="color: {primary_color}; background-color: {bg_color}; border: none" type="submit" class="btn btn-primary d-block w-100">Mettre à jour</button></div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="position-relative py-4 py-xl-5" id="soir-section">
        <div class="container position-relative">
            <div class="row d-flex justify-content-center">
                <div class="col-md-8 col-lg-6 col-xl-5 col-xxl-4">
                    <div class="card mb-5">
                        <div class="card-body p-sm-5">
                            <h2 class="text-center mb-4">Éditez vos {text2} horaires ici</h2>
                            <form method="post" action="requires/update_hours_noon.php" onsubmit="updateOpeningHoursNoon(); return false;">

                                <?php
                                    require $_SERVER['DOCUMENT_ROOT']. '/modules/opening-hours/requires/noon_displayer.php'
                                ?>

                                <div><button style="color: {primary_color}; background-color: {bg_color}; border: none" type="submit" class="btn btn-primary d-block w-100">Mettre à jour</button></div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="position-relative py-4 py-xl-5" id="closing-section">
        <div class="container position-relative">
            <div class="row d-flex justify-content-center">
                <div class="col-md-8 col-lg-6 col-xl-5 col-xxl-4">
                    <div class="card mb-5">
                        <div class="card-body p-sm-5">
                        <h2 class="text-center mb-4">Passez en mode fermeture</h2>
                            <form method="post" action="requires/update_closing.php" onsubmit="updateClosing(); return false;">
                                <label for="closingDate">Date de fermeture:</label><br>
                                <input type="date" id="closingDate" name="closingDate"><br>

                                <label for="reopeningDate">Date de réouverture:</label><br>
                                <input type="date" id="reopeningDate" name="reopeningDate"><br>

                                <label for="message">Message de fermeture:</label><br>
                                <textarea id="message" name="message" rows="4" cols="30"></textarea><br>

                                <input type="checkbox" id="closingMode" name="closingMode">
                                <label for="closingMode">Activer le mode fermeture</label><br>

                                <div style="margin-rop: 12px"><button style="color: {primary_color}; background-color: {bg_color}; border: none" type="submit" class="btn btn-primary d-block w-100">Mettre à jour</button></div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section>
        </div>
            <p style="text-align: center; font-size: 24px"><a href="https://www.{main_domain}/">Revenir à l'accueil</a></p>
        </div>
    </section>


    <script src="js/sectionDisplayer.js"></script>
    <script src="js/udpateOpeningHoursNoon.js"></script>
    <script src="js/udpateOpeningHoursMid.js"></script>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/footer.php'
?>
'''

    with open(f"{directory_path}/opening-hours/edit-hours.php", "w") as php_file:
        php_file.write(php_code)
        print("edit-hours.php generated !")
