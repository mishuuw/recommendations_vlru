import secrets
import sqlite3
import string
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
        return user

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


class dumpDB:
    @staticmethod
    def executequery(query):
        db = sqlite3.connect('users.db')
        c = db.cursor()
        c.execute(query)
        db.commit()
        db.close()