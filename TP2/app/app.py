from Flask import Flask, render_template

app = Flask (__name__,template_folder='../templates',static_folder='../static')

diccionario = {
    "nombre": "MTB bosques de palermo 2026",
    "organizador": "club unidos por el deporte",
    "fecha": "21-2-2026",
    "descripcion": "Una carrera de mountain bike que recorre los hermosos bosques de palermo, ideal para ciclistas de todos los niveles.",
    "horario": "9:00 AM hasta las 5:00 PM",
    "tipocarr": "MTB urbano",
    "lugar": "Bosques de palermo, Buenos Aires, Argentina",
    "auspiciantes": ["powerade", "adidas", "shimano", "gobierno de la ciudad de buenos aires"],
    "modalidad": {
        1: {"nombre": "carrera corta", "distancia": "50km", "dificultad": "media"},
        2: {"nombre": "carrera larga", "distancia": "100km", "dificultad": "avanzada"},
    },
    "imagenes": {
        1: "auspiciante1.png",
        2: "auspiciante2.png",
        3: "auspiciante3.png",
        4: "auspiciante4.png",
    }
}

@app.route('/')
def home():
    return render_template('index.html',activate_page='home',diccionario=diccionario)


@app.route("/registracion", methods=['POST', 'GET'])
def registracion():

    return render_template('form.html')

if __name__ == "__main__":
    app.run("127.0.0.1", port=8080, debug =True)