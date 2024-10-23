import random
import secrets
import sqlite3
import string
from datetime import datetime
from webbrowser import Error


class usersDB:
    def __init__(self):
        self.summon()

    @staticmethod
    def executequery(query):
        db = sqlite3.connect('users.db')
        c = db.cursor()
        result = c.execute(query).fetchall()
        db.commit()
        db.close()
        return result

    @classmethod
    def summon(cls):
        cls.executequery("""CREATE TABLE IF NOT EXISTS userinfo(
                userid text,
                username text,
                email text,
                password text)""")
        cls.executequery("""CREATE TABLE IF NOT EXISTS favorites(
                userid text,
                eventid text)""")
        cls.executequery("""CREATE TABLE IF NOT EXISTS purchases(
                userid text,
                eventid text)""")

    @classmethod
    def register_user(cls, username, email, password):
        try:
            # ---- inner vl.ru hash generation logic ----
            alphabet = string.ascii_letters + string.digits
            userid = ''.join([secrets.choice(alphabet) for i in range(32)])
            # ---- inner vl.ru hash generation logic ----
            cls.executequery(
                f"""INSERT INTO userinfo VALUES ("{userid}", "{username}", "{email}", "{password}")""")
            return dict(userid=userid, username=username, email=email, password=password)
        except Exception as e:
            raise Error(e)

    @staticmethod
    def fetchone(query, params=None):
        db = sqlite3.connect('users.db')
        c = db.cursor()
        if params:
            c.execute(query, params)
        else:
            c.execute(query)
        result = c.fetchone()
        db.close()
        return result

    @classmethod
    def authorize(cls, login, password):
        query = """SELECT userid FROM userinfo WHERE (username = ? OR email = ?) AND password = ?"""
        user = cls.fetchone(query, (login, login, password))
        return user is not None

    @classmethod
    def add_to_favorites(cls, userid, eventid):
        try:
            cls.executequery(
                f"""INSERT INTO favorites VALUES ("{userid}", "{eventid}")""")
            return True
        except Exception as e:
            raise Error(e)

    @classmethod
    def get_favorites(cls, userid):
        try:
            result = cls.executequery(f"""SELECT eventid FROM favorites WHERE userid == "{userid}" """)
            result = [row[0] for row in result]
            return result
        except Exception as e:
            raise Error(e)

    @classmethod
    def add_to_purchases(cls, userid, eventid):
        try:
            cls.executequery(f"""INSERT INTO purchases VALUES ("{userid}", "{eventid}")""")
            return True
        except Exception as e:
            raise Error(e)

    @classmethod
    def get_purchases(cls, userid):
        try:
            result = cls.executequery(f"""SELECT eventid FROM purchases WHERE userid == "{userid}" """)
            result = [row[0] for row in result]
            return result
        except Exception as e:
            raise Error(e)

    @classmethod
    def get_popular_events(cls):
        try:
            query = """
            SELECT eventid, COUNT(*) as popularity
            FROM (
                SELECT eventid FROM favorites
                UNION ALL
                SELECT eventid FROM purchases
            )
            GROUP BY eventid
            ORDER BY popularity DESC
            """
            result = cls.executequery(query)
            return [row[0] for row in result]
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_recommended_events(cls, user_id):
        try:

            popular_events = cls.get_popular_events()

            user_favorites = set(cls.get_favorites(user_id))
            user_purchases = set(cls.get_purchases(user_id))
            user_events = user_favorites.union(user_purchases)

            recommended_events = [event for event in popular_events if event not in user_events]
            return recommended_events
        except Exception as e:
            raise Exception(e)


class eventsDB:
    @staticmethod
    def executequery(query):
        db = sqlite3.connect('dump.db') #dump.db - затычка для моих затычковских нужд
        c = db.cursor()
        result = c.execute(query).fetchall()
        db.commit()
        db.close()
        return result

    @staticmethod # Абсолютно затычковый метод, просто выбирает рандомные события (типо актуальная афиша)
    def get_random_events():
        query = f"""SELECT EventID FROM Event_to_Category"""
        result = eventsDB.executequery(query)
        events = [event[0] for event in result]
        events = random.choices(events, k=700)
        return [eventsDB.get_event_data(event) for event in events]

    @staticmethod # Полностью затычковый метод, должен обращаться к 'events.db' и брать инфу оттуда
    def get_event_data(event_id):
        query = f"""SELECT Categories FROM Event_to_Category WHERE EventID == "{event_id}" """
        result = eventsDB.executequery(query)[0][0]
        event_data=dict(
            event_id=event_id,
            categories=result.split(';'),
            name=result.split(';')[::-1][0],
            desc='Описание события',
            cost=0, #Цена события
            date=dict(
                day=datetime.now().day,
                month=datetime.now().month,
                year=datetime.now().year
                ),
            location='Ул. Пушкина, Д. Колотушкина',
            program='Программа мероприятия. Вероятно, должна быть в JSON, но мне лень. затычка.',
            author='Автор события. в VL.RU есть странички у организаторов. затычка. мб ссылку сюда.',
            likes=random.randint(0,100),
            dislikes=random.randint(0,50),
            views=random.randint(0,5000)
        )
        return event_data