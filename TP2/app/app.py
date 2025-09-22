from flask import Flask, render_template

app = Flask (__name__,template_folder='../templates',static_folder='../static')

diccionario = {
    "nombre": "MTB bosques de palermo 2026",
    "organizador": "club unidos por el deporte",
    "fecha": "21-2-2026",
    "descripcion": "Una carrera de ciclismo en los bosques de palermo que combina deporte, naturaleza y diversion,Un recorrido unico para disfrutar pedaleando en uno de los lugares mas emblematicos de Buenos Aires.",
    "horario": "9:00 a 18:00",
    "tipocarr": "MTB urbano",
    "lugar": "Bosques de palermo",
    "modalidad": {
        1: {"nombre": "carrera corta", "distancia": "50km", "dificultad": "media"},
        2: {"nombre": "carrera larga", "distancia": "100km", "dificultad": "avanzada"},
    },
"imgausp": {
    1: {"archivo":"auspiciante1.png","texto":"ADIDAS"},
    2: {"archivo":"auspiciante3.png","texto":"GATORADE"},
    3: {"archivo":"auspiciante2.png","texto":"SHIMANO"},
    4: {"archivo":"auspiciante4.png","texto":"GOBIERNO DE LA CIUDAD"},
},
"imgdatos": {
    1: {"archivo":"logohorario.png","clave":"horario","texto":"Horario"}, 
    2: {"archivo":"logolugar.png","clave":"lugar","texto":"Ubicación"},
    3: {"archivo":"logotipocarr.png","clave":"tipocarr","texto":"Tipo de carrera"},   
    4: {"archivo":"logofecha.png","clave":"fecha","texto":"Fecha"},
    },

"pdfs": {
    1: {"palabra":"Guia","titulo": "Guia del ciclista","autor":"Gobierno de buenos aires","link":"guia.pdf"}, 
    2: {"palabra":"Reglamento","titulo":"Reglamentos de la carrera","autor":"Union internacional del ciclismo","link":"reglamento.pdf"},
    3: {"palabra":"Palermo","titulo":"Informacion sobre palermo","autor":"Ministerio de desarrollo urbano","link":"palermo.pdf"},
    },

"citas": {
    1: {"archivo":"testimonial-1.png","cita":"Desde que fui en bicicleta en los bosques de palermo, mi vida y mi forma de ver el mundo cambio por completo.","nombre":"Gustavo Cerati"}, 
    2: {"archivo":"testimonial-3.png","cita":"No me pregunten como, pero cuando termine esta carrera, la termine como una persona totalmente diferente","nombre":"Javier Milei"},
    3: {"archivo":"testimonial-2.png","cita":"Al principio dudaba de ir a la carrera, pero una vez fui, ¡Nunca estuve mas feliz de haber participado!","nombre":"niqui nicol(?)"},   
    4: {"archivo":"testimonial-4.png","cita":"Yyy la verdad que mucho no me gusto la carrera","nombre":"Un random que a nadie le importa"},
    },

}


@app.route('/')
def home():
    return render_template('index.html',activate_page='home',diccionario=diccionario)


@app.route("/registracion", methods=['POST', 'GET'])
def registracion():

    return render_template('form.html')

if __name__ == "__main__":
    app.run("127.0.0.1", port=8081, debug =True)