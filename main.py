from flask import Flask, request, jsonify, make_response
from ml import RatingPredictor

app = Flask(__name__, instance_relative_config=True)

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    # TODO: Use db to implement users management
    if username == 'user1':
        return 'pass1'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
    
predictor = RatingPredictor()

# Define routes (TODO:Change to blueprint this routes)
@app.route("/predict", methods=['POST'])
@auth.login_required
def predict():
    product_text = request.form.get('product_text')
    try:
        predicted_rating=predictor.predict(product_text)
    except Exception as e:
        # TODO:  Handling more correctly errors
        return jsonify({'error': f'500 Unexpected error:{e}'}), 500
    return jsonify({"rating": '%s' % predicted_rating} )

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': '404 Not Found'}), 404

