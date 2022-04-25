
# The script for creating the database [id, source, destination]
# The order records are stored in the Product.db file

import sqlite3 as sql

def create_db():
    con = sql.connect('Product.db')

    cursor = con.cursor()

    try:
        cursor.execute(
        """CREATE TABLE products (
                    id integer PRIMARY KEY,
                    source text,
                    destination text
                    )"""
        )
    except:
        pass


    # commit the change
    con.commit()
    con.close()




create_db()
