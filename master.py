from flask import Flask, request, jsonify
from flask_cors import CORS
from dbmanager import *
app = Flask(__name__)
CORS(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    response = usersDB.register_user(data['username'], data['email'], data['password'])
    print(response)
    return response

# to do:
@app.route('/authorize', methods=['POST'])
def authorize():
    pass

@app.route('/addFavorite', methods=['POST'])
def addfavorite():
    pass

@app.route('/buy', methods=['POST'])
def buy():
    pass

@app.route('/getPopularEvents', methods=['GET'])
def getpopularevents():
    pass

@app.route('/getFavoriteList', methods=['GET'])
def getfavoritelist():
    pass

@app.route('/getPurchaseList', methods=['GET'])
def getpurchaselist():
    pass

@app.route('/getEventData', methods=['GET'])
def geteventdata():
    pass

@app.route('/getRecommendedEvents', methods=['GET'])
def getrecommendedevents():
    pass

if __name__ == '__main__':
    app.run(debug=True)
