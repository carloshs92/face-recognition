from flask import Blueprint, request
from flask_cors import cross_origin
import face_recognition
from flask import Response
import json

# Define the blueprint: 'auth', set its url prefix: app.url/auth
detector_service = Blueprint('categorías', __name__, url_prefix='/api/v1/face-detector')

@detector_service.route('/', methods=['GET'])
@cross_origin()
def list_categories():
    image = face_recognition.load_image_file("./picture.jpg")
    face_locations = face_recognition.face_locations(image)
    json_response = json.dumps({
            'status': 1,
            'message': 'Se encontró las caras',
            'data': face_locations
        })
    return Response(json_response,
                    status=200,
                    mimetype='application/json')
