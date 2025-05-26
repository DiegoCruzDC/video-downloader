from flask import Flask, render_template, request, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/descargar', methods=['POST'])
def descargar():
    url = request.form['url']
    nombre_archivo = f"video_{uuid.uuid4()}.mp4"
    ruta_archivo = os.path.join("downloads", nombre_archivo)

    opciones = {
        'outtmpl': ruta_archivo,
        'format': 'bv*[vcodec^=avc1]+ba/b[ext=mp4]/b',  
        'quiet': True,  
        'noplaylist': True  
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
    except Exception as e:
        return f"<h3>Error al descargar el video:</h3><p>{str(e)}</p>"

    return send_file(ruta_archivo, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    app.run(debug=True)


    if not os.path.exists("downloads"):
        os.makedirs("downloads")
