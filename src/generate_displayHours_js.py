def generate_displayHours_js(directory_path, main_domain, opening_option):

    text1 = ""
    text2 = ""

    if opening_option == "M/N" :
        text1 = "Fermé le midi"
        text2 = "Fermé le soir"
    elif opening_option == "AM/PM" :
        text1 = "Fermé le matin"
        text2 = "Fermé l'après-midi"

    js_code = f'''$(document).ready(function(){{$.ajax({{url:"https://www.{main_domain}/modules/opening-hours/opening_hours.json",dataType:"json",success:function(r){{var n={{Monday:"Lundi",Tuesday:"Mardi",Wednesday:"Mercredi",Thursday:"Jeudi",Friday:"Vendredi",Saturday:"Samedi",Sunday:"Dimanche"}};for(var e in n){{var o=r[e+"OpeningM"],s=r[e+"ClosingM"],i=r[e+"Opening"],a=r[e+"Closing"],d="";d="Closed"===o?"<strong>"+n[e]+":</strong> {text1} / ":"<strong>"+n[e]+":</strong> "+o+" - "+s+" / ","Closed"===i?d+="{text2}":d=d+i+" - "+a,$("#"+e.toLowerCase()+"Hours").html(d)}}}},error:function(){{$(".hours").text("Error fetching opening hours")}}}})}});
'''
    
    if opening_option == "C" : 

        js_code = f'''$(document).ready(function(){{$.ajax({{url:"https://www.{main_domain}/modules/opening-hours/opening_hours.json",dataType:"json",success:function(r){{var n={{Monday:"Lundi",Tuesday:"Mardi",Wednesday:"Mercredi",Thursday:"Jeudi",Friday:"Vendredi",Saturday:"Samedi",Sunday:"Dimanche"}};for(var e in n){{var o=r[e+"Opening"],s=r[e+"Closing"],a="";a="Closed"===o?"<strong>"+n[e]+":</strong> Ferm\xe9":"<strong>"+n[e]+":</strong> "+o+" - "+s,$("#"+e.toLowerCase()+"Hours").html(a)}}}},error:function(){{$(".hours").text("Error fetching opening hours")}}}})}});
'''

    with open(f"{directory_path}/opening-hours/js/displayHours.js", "w") as js_file:
        js_file.write(js_code)
        print("displayHours.js generated !")
