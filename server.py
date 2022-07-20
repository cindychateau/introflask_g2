from flask import Flask, render_template #Importando Flask para que nos permita crear una aplicación
app = Flask(__name__)   #Creando una nueva instancia de la clase Flask

@app.route('/') #Asociando una ruta a una función
def index():    #Función que se ejecuta al ingresar a la ruta
    return "Hola mundo!" #Regresa el texto Hola mundo!

@app.route('/hola/<nombre_url>')
def hola(nombre_url):
    return "Hola, cómo estás "+nombre_url

@app.route('/hello/<nombre_url>/<int:cantidad>')
def hello(nombre_url, cantidad):
    return render_template('index.html', nombre=nombre_url, num=cantidad)


if __name__=="__main__": #Asegura que el archivo que estoy ejecutando es directo y no es un módulo externo
    app.run(debug=True)  #Ejecuta mi aplicación