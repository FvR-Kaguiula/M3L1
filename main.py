from flask import Flask, send_file, render_template
import random
import os
import requests
import time

app = Flask(__name__)

datos = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
         "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
         "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
         "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
         "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
         "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
         "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
         "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]

def get_duck_image_url():
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data["url"]

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_memes_url():
    url = 'https://api.imgflip.com/get_memes'
    res = requests.get(url)
    data = res.json()

    if data['success']:
        memes = random.choice(data['data']['memes'])
        meme_alet = memes["url"]
        return meme_alet


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/random_datos")
def randomdatos():
    return f"""<p>{random.choice(datos)}</p>
                <br><a href=/>Volver a la página principal
            """

@app.route("/gen_pass")
def gen_pass():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    length = 10
    gened_pass = ''.join(random.choice(chars) for _ in range(length))
    return f"""
            <p>Contraseña generada a continuación</p>
            <p>{gened_pass}</p>
            <br><a href=/> Volver a la página principal
            """

@app.route("/memes")
def meme():
    meme_dir = "C:/Users/Jose Antonio/OneDrive/Escritorio/Python Proyects/3713/M3L1/static/image"
    
    #Archivo elegido del directorio
    listmeme = []
   
    n = 0

    while n <= len(os.listdir(meme_dir)):
        random_meme = random.choice(os.listdir(meme_dir))
        if random_meme in listmeme:
            random_meme = random.choice(os.listdir(meme_dir))
    
        else:
            listmeme.append(random_meme)
            n += 1
            return f"""
                    <p>Meme random generado a continuación:</p>
                    <img src="/static/image/{random_meme}" width = "400" height = auto alt ="meme1">
                    <br><a href=/> Volver a la página principal
                    <br><a href="/memes" ><button type="button">Refrescar la pagina</button></a>
                    """
        time.sleep(5)
        
   

@app.route("/patos")
def duck():
    image_url = get_duck_image_url()  # Función para obtener la URL de la imagen
    return f"""<h1>Imagen de pato aleatoria</h1>
               <img src='{image_url}' alt='Duck Image'>
               <br><a href='/'>Volver a la página principal</a>"""

@app.route("/perros")
def dog():
    image_url = get_dog_image_url()  # Función para obtener la URL de la imagen
    return f"""<h1>Imagen de perros aleatoria</h1>
               <img src='{image_url}' alt='Dog Image'>
               <br><a href='/'>Volver a la página principal</a>"""

@app.route("/tiempo")
def get_weather_info_url():    
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    querystring = {"lat":"-12.051170552447141","lon":"-77.03076856051939","units":"metric","lang":"es"}
    headers = {
	"x-rapidapi-key": "dd44b94613msh2c82005f6597c3fp17fafcjsnf6fe00f40a2c",
	"x-rapidapi-host": "weatherbit-v1-mashape.p.rapidapi.com"
}
    res = requests.get(url, headers=headers, params=querystring)
    data = res.json()
    
    #Regresar la información ordenada
    weather_data = data['data'][0]
    formatted_data = (
        f"""Ciudad: {weather_data['city_name']}
        <br>Temperatura: {weather_data['temp']}°C
        <br>Descripción: {weather_data['weather']['description']}
        <br>Viento: {weather_data['wind_spd']} mph desde {weather_data['wind_cdir_full']}
        <br>Humedad: {weather_data['rh']}%
        <br>Presión: {weather_data['pres']} mb
        <br>Índice UV: {weather_data['uv']}
        <br>Visibilidad: {weather_data['vis']} millas
        <br>Hora de observación: {weather_data['ob_time']}
        <br><a href='/'>Volver a la página principal</a>"""
    )
    return(formatted_data)

@app.route("/memeapi")
def random_meme():
    image_url = get_memes_url()
    return f"""<h1>Imagenes de plantilla de memes aleatoria</h1>
               <img src='{image_url}' alt='Platmeme'>
               <br><a href='/'>Volver a la página principal</a>"""

app.run(debug=True)