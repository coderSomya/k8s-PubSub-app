import psychopg2

def store_transaction(order):

    conn = psychopg2.connect(
            dbname='orders_db',
            user='postgres',
            password='postgres',
            host='postgres'
        )
    cur = conn.cursor()

    cur.execute(
            'CREATE TABLE if not exists transactions (
            email VARCHAR(255),
            item VARCHAR(255),
            qty INT,
            price INT
            );'
            )
    cur.execute(
            'INSERT INTO transactions (email, item, qty,price) 
            VALUES (%s, %s, %s, %s)',
            (order['email'], order['item'], order['qty'], order['price'])
            )

    conn.commit()
    cur.close()
    conn.close()



