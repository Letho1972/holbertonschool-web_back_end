from flask import Flask, jsonify

""" Set up a basic Flask app """

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """ a single GET route ("/")"""

    return jsonify({
        'message': 'Hello, World!',
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True)
