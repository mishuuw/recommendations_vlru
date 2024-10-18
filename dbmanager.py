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
        c.execute(query)
        db.commit()
        db.close()

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
            return True
        except Exception as e:
            raise Error(e)

    @classmethod
    def add_to_favorites(cls, userid, eventid):
        try:
            cls.executequery(
                f"""INSERT INTO favorites VALUES ("{userid}", "{eventid}")""")
            return True
        except Exception as e:
            raise Error(e)

    @classmethod
    def add_to_purchases(cls, userid, eventid):
        try:
            cls.executequery(f"""INSERT INTO purchases VALUES ("{userid}", "{eventid}")""")
            return True
        except Exception as e:
            raise Error(e)

class dumpDB:
    @staticmethod
    def executequery(query):
        db = sqlite3.connect('users.db')
        c = db.cursor()
        c.execute(query)
        db.commit()
        db.close()