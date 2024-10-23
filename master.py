from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_caching import Cache
from dbmanager import usersDB, eventsDB
from neural_network import NeuralNetwork

def create_app():
    app = Flask(__name__)
    """НАСТРОЙКА КЭША, ЙОУ"""
    cache = Cache(app, config={'CACHE_TYPE': 'simple'})
    """КОНЕЦ НАСТРОЙКИ КЭША, ЙОУ"""

    @app.route('/register', methods=['POST'])
    def register():
        data = request.json
        response = usersDB.register_user(data['username'], data['email'], data['password'])
        print(response)
        return response

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
                cache.delete('getPopularEvents')
                cache.delete(f'getRecommendedEvents_{user_id}')
                cache.delete(f'getFavoriteList_{user_id}')
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
                cache.delete('getPopularEvents')
                cache.delete(f'getRecommendedEvents_{user_id}')
                cache.delete(f'getPurchaseList_{user_id}')
                return jsonify({"message": "Event purchased"}), 200
            else:
                return jsonify({"error": "Failed to purchase event"}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/getPopularEvents', methods=['GET'])
    @cache.cached(timeout=228)  # Кэширование на 5 минут
    def getpopularevents():
        try:
            events = usersDB.get_popular_events()
            return jsonify(events), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/getFavoriteList', methods=['GET'])
    @cache.cached(timeout=228, key_prefix="getFavoriteList_{user_id}")
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
    @cache.cached(timeout=228, key_prefix="getPurchaseList_{user_id}")
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
    @cache.cached(timeout=228, key_prefix="getEventData_{event_id}")
    def geteventdata():
        event_id = request.args.get('eventID')
        if not event_id:
            return jsonify({"error": "Event ID is required"}), 400

        try:
            event_data = eventsDB.get_event_data(event_id)
            return jsonify(event_data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/getRecommendedEvents', methods=['GET'])
    @cache.cached(timeout=228, key_prefix="getRecommendedEvents_{user_id}")
    def getrecommendedevents():
        user_id = request.args.get('userID')
        if not user_id:
            return jsonify({"error": "User ID is required"}), 400

        try:
            recommended_events = AI.get_recommendations(user_id)
            print(recommended_events, type(recommended_events))
            return jsonify(recommended_events), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return app

app = create_app()
CORS(app)

if __name__ == '__main__':
    if 'AI' not in globals():  # Убедитесь, что объект создается один раз
        AI = NeuralNetwork()
    # Запуск приложения с отключенным reloader'ом для избежания двойной инициализации
    app.run(debug=True, use_reloader=False)
