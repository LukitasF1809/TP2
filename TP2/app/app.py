from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_mail import Mail, Message


import os

app = Flask (__name__,template_folder='../templates',static_folder='../static')

load_dotenv()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = ("MTB Tandil", "ciclismouped@gmail.com")
mail = Mail(app)


unete= True
diccionario = {
    "nombre": "Tandil en bici 2025",
    "organizador": "club unidos por el deporte",
    "fecha": "24-10-2025",
    "descripcion": "Un evento único de ciclismo en la ciudad de Tandil, Buenos Aires. Una jornada para disfrutar del deporte, la naturaleza y los paisajes serranos en un recorrido pensado para todos los amantes de la bicicleta",
    "tipocarr": "Ciclismo urbano y rural",
    "horario": "9:00 a 18:00",
    "lugar": "Ciudad de Tandil, Buenos Aires",
    "modalidad": {
        1: {"nombre": "carrera corta", "distancia": "30km", "dificultad": "media"},
        2: {"nombre": "carrera larga", "distancia": "80km", "dificultad": "avanzada"},
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
    3: {"palabra":"Tandil","titulo":"Informacion sobre Tandil","autor":"Municipio de Tandil","link":"palermo.pdf"},
    4: {"palabra":"deslinde","titulo":"Deslinde","autor":"Club unidos por el deporte","link":"deslinde.pdf"},
    },

"citas": {
    1: {"archivo":"testimonial-3.png","cita":"cuando participe en Tandil en bici 2024, mi vida y mi forma de ver el mundo cambio por completo.","nombre":"Gustavo Cerati"}, 
    2: {"archivo":"testimonial-1.png","cita":"No me pregunten como, pero cuando termine esta carrera, la termine como una persona totalmente diferente","nombre":"Javier Milei"},
    3: {"archivo":"testimonial-2.png","cita":"Al principio dudaba de ir a la carrera, pero una vez fui, ¡Nunca estuve mas feliz de haber participado!","nombre":"niqui nicol(?)"},   
    4: {"archivo":"testimonial-4.png","cita":"Yyy la verdad que mucho no me gusto la carrera","nombre":"Un random que a nadie le importa"},
    },

}


@app.route('/')
def home():
    global unete
    return render_template('index.html',activate_page='home',diccionario=diccionario, unete=unete)


@app.route("/registracion", methods=['POST', 'GET'])
def registracion():
    global unete
    mensaje= None

    if request.method == "POST":
        nombre = request.form.get("name")
        email = request.form.get("email")
        num = request.form.get("num")
        modalidad= request.form.get("modalidad")
        info = request.form.get("info")
        if not info or info.strip() == "":
            info = "No se envió información adicional"

        if not nombre or not email or not num or not modalidad:
            mensaje = f"Por favor rellene todos los campos obligatorios"
        else:
            mensaje = f"Sus datos han sido enviados ¡Gracias por participar!"

            correo = Message(
                subject="Nueva registración",
                recipients=["ciclismouped@gmail.com"],  # tu correo donde recibís los formularios
            )
            correo.html = f"""
                            <h2>Nueva registración recibida</h2>
                            <p><strong>Nombre:</strong> {nombre}</p>
                            <p><strong>Email:</strong> {email}</p>
                            <p><strong>Celular:</strong> {num}</p>
                            <p><strong>Modalidad:</stong> {modalidad} </p>
                            <p><br><strong>Info adicional:</strong> {info}</p>
                        """
            mail.send(correo)    
            unete= False

    return render_template('form.html', mensaje=mensaje, diccionario=diccionario, unete=unete)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run("127.0.0.1", port=8081, debug =True)