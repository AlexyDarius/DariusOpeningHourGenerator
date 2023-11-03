def generate_displayHours_js(directory_path, main_domain):
    js_code = f'''$(document).ready(function(){{$.ajax({{url:"https://www.{main_domain}/modules/opening-hours/opening_hours.json",dataType:"json",success:function(r){{var n={{Monday:"Lundi",Tuesday:"Mardi",Wednesday:"Mercredi",Thursday:"Jeudi",Friday:"Vendredi",Saturday:"Samedi",Sunday:"Dimanche"}};for(var e in n){{var o=r[e+"OpeningM"],s=r[e+"ClosingM"],i=r[e+"Opening"],a=r[e+"Closing"],d="";d="Closed"===o?"<strong>"+n[e]+":</strong> Ferm\xe9 le midi / ":"<strong>"+n[e]+":</strong> "+o+" - "+s+" / ","Closed"===i?d+="Ferm\xe9 le soir":d=d+i+" - "+a,$("#"+e.toLowerCase()+"Hours").html(d)}}}},error:function(){{$(".hours").text("Error fetching opening hours")}}}})}});
'''

    with open(f"{directory_path}/opening-hours/js/displayHours.js", "w") as js_file:
        js_file.write(js_code)
        print("displayHours.js generated !")
