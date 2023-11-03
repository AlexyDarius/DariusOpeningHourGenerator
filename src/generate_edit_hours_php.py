def generate_edit_hours_php(directory_path, main_domain, full_body_tag):
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
            <div class="row">
                <div class="col-6 col-md-6 d-flex justify-content-center"><button class="btn btn-primary" type="button" style="color: var(--bs-body-bg); background-color: var(--bs-primary); border: none" id="edit-midi-button">Éditer horaires du midi</button>
                </div>
                <div class="col-6 col-md-6 d-flex justify-content-center"><button class="btn btn-primary" type="button" style="color: var(--bs-body-bg); background-color: var(--bs-primary); border: none" id="edit-soir-button">Éditer horaires du soir</button>
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
                        <h2 class="text-center mb-4">Éditer vos horaires du midi ici</h2>
                            <form method="post" action="requires/update_hours_mid.php" onsubmit="updateOpeningHoursMid(); return false;">

                                <?php
                                    require $_SERVER['DOCUMENT_ROOT']. '/modules/opening-hours/requires/mid_displayer.php'
                                ?>

                                <div><button type="submit" class="btn btn-primary d-block w-100">Mettre à jour</button></div>
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
                            <h2 class="text-center mb-4">Éditez vos du soir horaires ici</h2>
                            <form method="post" action="requires/update_hours_noon.php" onsubmit="updateOpeningHoursNoon(); return false;">

                                <?php
                                    require $_SERVER['DOCUMENT_ROOT']. '/modules/opening-hours/requires/noon_displayer.php'
                                ?>

                                <div><button type="submit" class="btn btn-primary d-block w-100">Mettre à jour</button></div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section>
        </div>
            <p style="text-align: center; font-size: 24px"><a href="https://{main_domain}/">Revenir à l'accueil</a></p>
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
