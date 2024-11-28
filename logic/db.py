import sqlite3

class Log():
    def con(self, filename, text) -> list[tuple]:
        con = sqlite3.connect(filename)
        cursor = con.cursor()

        passwords = cursor.execute("""SELECT * from passwords WHERE web_name LIKE ? """, ('%' + text + '%',)).fetchall()
        con.close()
        return passwords

    def add(self, filename, web, user, password):
        con = sqlite3.connect(filename)
        cursor = con.cursor()

        cursor.execute("""INSERT INTO passwords("web_name", "username", "password") VALUES(?, ?, ?)""", (web, user, password,))
        con.commit()
        con.close()

    def create_db(self, filename):
        con = sqlite3.connect(filename)
        cursor = con.cursor()

        cursor.execute("""CREATE TABLE passwords(
                       id INTEGER PRIMARY KEY,
                       web_name TEXT,
                       username TEXT,
                       password TEXT
                       );""")
        con.commit()
        con.close()