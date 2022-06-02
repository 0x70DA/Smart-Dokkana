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

    def select(self, id: int) -> dict:
        """ Return the row specified by the id. """
        # Create connection to db.
        conn = self._connect_db()
        conn.row_factory = sqlite3.Row  # To return a dictionary instead of a tuple.

        # Create a Cursor object.
        cur = conn.cursor()

        # Execute query.
        row = dict(cur.execute("SELECT * FROM Users WHERE id=?", (id,)).fetchone())

        # Close connection to db.
        self._close_db(conn)

        return row

    def select_all(self) -> list:
        """ Return all the rows from the database. """
        # Create connection to db.
        conn = self._connect_db()
        conn.row_factory = sqlite3.Row

        # Create a cursor object.
        cur = conn.cursor()

        # Execute query.
        rows = list(map(dict, cur.execute("SELECT * FROM Users").fetchall()))

        # Close connection to db.
        self._close_db(conn)

        return rows

    def insert(self, row: tuple) -> int:
        """ Insert a new row to the database. """
        # Create connection to db.
        conn = self._connect_db()

        # Create a cursor object.
        cur = conn.cursor()

        # Execute query.
        query = "INSERT INTO Users(username, name, email, password) VALUES(?, ?, ?, ?)"
        cur.execute(query, row)
        conn.commit()
        last_row_id = cur.lastrowid

        # Close connection to db.
        self._close_db(conn)

        # Return the id of the new row.
        return last_row_id

    def update(self, id: int, new_balance: int):
        """ Update data in database. """
        # Create connection to db.
        conn = self._connect_db()

        # Create a cursor object.
        cur = conn.cursor()

        # Execute query.
        query = "UPDATE Users SET balance = ? WHERE id = ?"
        cur.execute(query, (new_balance, id))
        conn.commit()

        # Close connection to db.
        self._close_db(conn)

    def delete(self, id: int):
        """ Delete data in database. """
        # Create connection to db.
        conn = self._connect_db()

        # Create a cursor object.
        cur = conn.cursor()

        # Execute query.
        query = "DELETE FROM Users WHERE id = ?"
        cur.execute(query, (id,))
        conn.commit()

        # Close connection to db.
        self._close_db(conn)

# db = Database('database.db')
# print(db.select(1))
# print(db.select_all())
# print(db.insert(('example', 'example', 'example@example.com', 'example')))
# db.update(1, 150)
