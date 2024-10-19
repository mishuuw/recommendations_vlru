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
    data = request.json
    if 'login' not in data or 'password' not in data:
        return jsonify({"error": "Login and password are required"}), 400

    response = usersDB.authorize(data['login'], data['password'])
    print(response)

    if response:
        return jsonify({"user_id": response[0]}), 200
    else:
        return jsonify({"error": "Invalid login or password"}), 401

@app.route('/addFavorite', methods=['POST'])
def addfavorite():
    data = request.json
    if 'userID' not in data or 'eventID' not in data:
        return jsonify({"error": "User ID and Event ID are required"}), 400

    user_id = data['userID']
    event_id = data['eventID']

    try:
        success = usersDB.add_to_favorites(user_id, event_id)
        if success:
            return jsonify({"message": "Event added to favorites"}), 200
        else:
            return jsonify({"error": "Failed to add event to favorites"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/buy', methods=['POST'])
def buy():
    data = request.json
    if 'userID' not in data or 'eventID' not in data:
        return jsonify({"error": "User ID and Event ID are required"}), 400

    user_id = data['userID']
    event_id = data['eventID']

    try:
        success = usersDB.add_to_purchases(user_id, event_id)
        if success:
            return jsonify({"message": "Event purchased"}), 200
        else:
            return jsonify({"error": "Failed to purchase event"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getPopularEvents', methods=['GET'])
def getpopularevents():
    try:
        events = usersDB.get_popular_events()
        return jsonify(events), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getFavoriteList', methods=['GET'])
def getfavoritelist():
    user_id = request.args.get('userID')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    try:
        favorites = usersDB.get_favorites(user_id)
        return jsonify(favorites), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getPurchaseList', methods=['GET'])
def getpurchaselist():
    user_id = request.args.get('userID')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    try:
        purchases = usersDB.get_purchases(user_id)
        return jsonify(purchases), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getEventData', methods=['GET'])
def geteventdata():
    event_id = request.args.get('eventID')
    if not event_id:
        return jsonify({"error": "Event ID is required"}), 400

    try:
        event_data = usersDB.get_event_data(event_id)
        return jsonify(event_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getRecommendedEvents', methods=['GET'])
def getrecommendedevents():
    user_id = request.args.get('userID')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    try:
        recommended_events = usersDB.get_recommended_events(user_id)
        return jsonify(recommended_events), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
