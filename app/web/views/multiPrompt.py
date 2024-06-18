# from flask import Blueprint, request, jsonify
# from flask_cors import cross_origin
# from app.chat.multi import handle_prompts  # Importar la función handle_prompts desde multi.py

# bp = Blueprint('multiPrompt', __name__, url_prefix='/api')

# @bp.route('/multiPrompt', methods=['POST'])
# @cross_origin()
# def handle_multi_prompt():
#     data = request.get_json()
#     response = handle_prompts(data)  # Llamar a la función en multi.py
#     return jsonify(response), 200


# multiprompt.py

from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.chat.multi import handle_prompts  # Importar la función handle_prompts desde multi.py

bp = Blueprint('multiPrompt', __name__, url_prefix='/api')

@bp.route('/multiPrompt', methods=['POST'])
@cross_origin()
def handle_multi_prompt():
    data = request.get_json()
    responses = handle_prompts(data)  # Llamar a la función en multi.py
    return jsonify(responses), 200
