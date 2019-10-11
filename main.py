from flask import Flask
import face_recognition

app = Flask(__name__)
print(face_recognition.__version__)
@app.route('/')
def index():
    image = face_recognition.load_image_file("image.jpg")
    face_locations = face_recognition.face_locations(image)
    print(face_locations);
    return """<p style='display: flex;
                 flex-direction: column;
                 align-items: center;
                 justify-content: center;
                 height: 100vh;
                 font-size: 70px;
                 font-weight: 900;'>{¡DevOps}!</p>"""

@app.route('/javascript')
def javascript():
    return "hi everyone"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
