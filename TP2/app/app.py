from flask import Flask, render_template

app = Flask (__name__,template_folder='../templates',static_folder='../static')

@app.route('/')
def home():
    return render_template('index.html',activate_page='home')

@app.route("/registracion", methods=['POST', 'GET'])
def registracion():

    return render_template('form.html')

if __name__ == "__main__":
    app.run("127.0.0.1", port=8080, debug =True)