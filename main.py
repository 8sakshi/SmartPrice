from flask import Flask, jsonify, g, request
from dotenv import load_dotenv
import sqlite3
from time import sleep
import threading
import re
from Amazonwebhelper import get_amazon_price
from Daytabase import Product

load_dotenv()

app = Flask(__name__)
DATABASE = "product_database.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_database():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    #  CREATE TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amazon_link TEXT,
        amazon_og_price TEXT,
        amazon_current_price TEXT,
        amazon_lowest_price TEXT,
        flipkart_link TEXT,
        flipkart_og_price TEXT,
        flipkart_current_price TEXT,
        flipkart_lowest_price TEXT,
        email TEXT
    )
    """)
    db.commit()

@app.route('/api/', methods = ['GET'])
def get_all():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    # convert rows to dict
    data = []
    for row in rows:
        data.append(dict(row))

    return jsonify({'data': data})

@app.route('/api/', methods = ['DELETE'])
def delete():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()

    cursor.execute("DELETE FROM products WHERE id = " + str(data["id"]))
    db.commit()

    return jsonify({'message': "success"})

@app.route('/api/', methods = ['POST'])
def post():
    db = get_db()
    cursor = db.cursor()

    data = request.get_json()

    amazon_price = 0
    flipkart_price = 0

    if data["amazon_link"]:
        x=get_amazon_price(data["amazon_link"])
        amazon_price=re.sub("[^0-9]","",x)

    cursor.execute("INSERT INTO products (email, title, amazon_link, amazon_og_price, amazon_current_price, amazon_lowest_price, flipkart_link) VALUES ('"+ data["email"]+ "','"+data["title"]+ "','"+data["amazon_link"]+ "',"+amazon_price+","+amazon_price+","+amazon_price+",'"+data["flipkart_link"]+"')")
    db.commit()

    x = Product(data["title"])
    x.amazon_current_price = amazon_price
    x.email = data["email"]

    x.notify_addition()

    return jsonify({'message': "success"})

def start_server():
    init_database()
    app.run(debug=True)

def update():
    with app.app_context():
        while True:
            db = get_db()
            cursor = db.cursor()

            cursor.execute("SELECT * FROM products")
            rows = cursor.fetchall()
            data = []
            if rows:
                for row in rows:
                    r=dict(row)
                    p=Product(r["title"],amazon_link=r["amazon_link"],flipkart_link=r["flipkart_link"],email=r["email"])
                    p.id=r["id"]
                    p.amazon_og_price=r["amazon_og_price"]
                    p.amazon_current_price=r["amazon_current_price"]
                    p.amazon_lowest_price=r["amazon_lowest_price"]
                    p.flipkart_og_price=r["flipkart_og_price"]
                    p.flipkart_current_price=r["flipkart_current_price"]
                    p.flipkart_lowest_price=r["flipkart_lowest_price"]
                    data.append(p)

            for product in data:
                if product.amazon_link:
                    x = get_amazon_price (product.amazon_link)
                    amazon_price = re.sub("[^0-9]", "", x)

                    
                    if amazon_price == 0:
                        continue

                    if amazon_price<product.amazon_lowest_price:
                        product.amazon_current_price = amazon_price
                        product.notify_change()
                        cursor.execute("update products set amazon_current_price =" +str(amazon_price)+", amazon_lowest_price = " + str(amazon_price) + " where id=" +str(product.id))
                    else:
                        cursor.execute("update products set amazon_current_price =" +str(amazon_price)+" where id=" +str(product.id))

                    db.commit()

                    sleep(60)

            sleep(60*60*2)


if __name__ == '__main__':
    update_thread = threading.Thread(target=update)
    update_thread.start()
    start_server()
    

