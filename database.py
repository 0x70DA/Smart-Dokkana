import sqlite3
from sqlite3 import Error

class Database:

    def __init__(self, db_file):
        self.db_file = db_file # Path to database file.

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
        
    def select(self, table, id):
        """ Return the row specified by the id from a certain table. """
        # Create connection to db.
        conn = self._connect_db()

        # Create a Cursor object.
        cur = conn.cursor()

        # Execute query.
        cur.execute("SELECT * FROM ? WHERE id=?", (table, id))

        row = cur.fetchall()

        return row