import sqlite3
from sqlite3 import Error


class Database:

    def __init__(self, db_file):
        self.db_file = db_file  # Path to database file.

    def _connect_db(self):
        """ Make a connection to the SQLite database. """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)

        return conn

    def _close_db(self, conn):
        """ Close connection to database. """
        if conn:
            conn.close()

    def select(self, id: int) -> tuple:
        """ Return the row specified by the id.. """
        # Create connection to db.
        conn = self._connect_db()

        # Create a Cursor object.
        cur = conn.cursor()

        # Execute query.
        row = cur.execute("SELECT * FROM Users WHERE id=?", (id,)).fetchall()[0]

        return row
