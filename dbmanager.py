import secrets
import sqlite3
import string
from webbrowser import Error


class usersDB:
    def __init__(self):
        self.db = sqlite3.connect('users')
        self.summon()

    def summon(self):
        c = self.db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS userinfo(
                userid text,
                username text,
                email text,
                password text)""")
        c.execute("""CREATE TABLE IF NOT EXISTS favorites(
                userid text,
                eventid text)""")
        c.execute("""CREATE TABLE IF NOT EXISTS purchases(
                userid text,
                eventid text)""")

    def register_user(self, username, email, password):
        try:
            alphabet = string.ascii_letters + string.digits
            userid = ''.join([secrets.choice(alphabet) for i in range(32)])
            c = self.db.cursor()
            c.execute(f"""INSERT INTO userinfo VALUES ("{userid}", "{username}", "{email}", "{password}")""")
            return True
        except Exception as e:
            raise Error(e)

    def add_to_favorites(self, userid, eventid):
        try:
            c = self.db.cursor()
            c.execute(f"""INSERT INTO favorites VALUES ("{userid}", "{eventid}")""")
            return True
        except Exception as e:
            raise Error(e)

    def add_to_purchases(self, userid, eventid):
        try:
            c = self.db.cursor()
            c.execute(f"""INSERT INTO purchases VALUES ("{userid}", "{eventid}")""")
            return True
        except Exception as e:
            raise Error(e)