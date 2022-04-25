
# The file for the API service to query the database records

import sqlite3 as sql


def listAllProducts():
    try:
        # The API for list out all the products in the database
        db = sql.connect('Product.db')
        cursor = db.cursor()

        select_query = 'SELECT * FROM products'
        cursor.execute(select_query)
        products = cursor.fetchall()

        for product in products:
            for i, attribute in enumerate(product):
                if (i == len(product)-1):
                    # last attribute have line break
                    print(attribute)
                else:
                    print(attribute, end=',')

        cursor.close()

    except sql.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if db:
            db.close()




def createNewOrder(source, detination):
    try:
        # parse the string to location
        source, detination = parse_string_to_location(source, detination)

        # The API for insert new order by source and destination
        db = sql.connect('Product.db')
        cursor = db.cursor()

        # Insert new product order
        cursor.executemany('INSERT INTO products (source, destination) VALUES(?,?)', [(source, detination,)])
        
        # Get the order ID
        select_query = 'SELECT id FROM products WHERE source = ? AND destination = ?'
        cursor.execute(select_query, (source, detination,))

        id = cursor.fetchone()
        print(id[0])
        
        cursor.close()

        # commit the db change
        db.commit()

    except sql.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if db:
            db.close()



def takeOrder(product_id):
    if product_id.isdigit():
        try:
                # The API for insert new order by source and destination
                db = sql.connect('Product.db')
                cursor = db.cursor()

                select_query = "SELECT MAX(id) FROM products"
                cursor.execute(select_query)
                max_id = cursor.fetchone()

                if int(product_id) > int(max_id[0]):
                    # Not Existed Product because exceed the max id
                    print('order does not exist')

                else:
                    # check the product is taken away or not
                    select_query = "SELECT source, destination FROM products WHERE id = ?"
                    cursor.execute(select_query, (product_id))
                    product = cursor.fetchone()

                    if product:
                        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
                    else:
                        print('order already taken')
                
                cursor.close()

                # commit the db change
                db.commit()

        except sql.Error as error:
            print("Failed to read data from sqlite table", error)

        finally:
            if db:
                db.close()
    else:
        print("Please enter a numerical ID")



def parse_string_to_location(source, detination):
    source = source.replace('"', '')
    detination = detination.replace('"', '')
    return source, detination