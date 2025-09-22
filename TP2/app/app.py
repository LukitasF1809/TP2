from flask import Flask, render_template

app = Flask (__name__,template_folder='../templates',static_folder='../static')

diccionario = {
    "nombre": "MTB bosques de palermo 2026",
    "organizador": "club unidos por el deporte",
    "fecha": "21-2-2026",
    "descripcion": "Una carrera de ciclismo en los bosques de palermo que combina deporte, naturaleza y diversion,Un recorrido unico para disfrutar pedaleando en uno de los lugares mas emblematicos de Buenos Aires.",
    "horario": "9:00 AM hasta las 5:00 PM",
    "tipocarr": "MTB urbano",
    "lugar": "Bosques de palermo, Buenos Aires, Argentina",
    "modalidad": {
        1: {"nombre": "carrera corta", "distancia": "50km", "dificultad": "media"},
        2: {"nombre": "carrera larga", "distancia": "100km", "dificultad": "avanzada"},
    },
"imgausp": {
    1: {"archivo":"auspiciante1.png","texto":"Adidas"},
    2: {"archivo":"auspiciante2.png","texto":"Gatorade"},
    3: {"archivo":"auspiciante3.png","texto":"Shimano"},
    4: {"archivo":"auspiciante4.png","texto":"Gobierno de la ciudad"},
},
"imgdatos": {
    1: {"archivo":"logohorario.png","clave":"horario"}, 
    2: {"archivo":"logolugar.png","clave":"lugar"},
    3: {"archivo":"logotipocarr.png","clave":"tipocarr"},   
    4: {"archivo":"logofecha.png","clave":"fecha"}}
}


@app.route('/')
def home():
    return render_template('index.html',activate_page='home',diccionario=diccionario)


@app.route("/registracion", methods=['POST', 'GET'])
def registracion():

    return render_template('form.html')

if __name__ == "__main__":
    app.run("127.0.0.1", port=8080, debug =True)