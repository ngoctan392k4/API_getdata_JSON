from db_json_config import read_db_config
from mysql.connector import MySQLConnection, Error
import sys
import json

def save_to():
    query = "SELECT id,brand,category,price,title,review,rating,image_link,product_link,from_page_link,avr_price,avr_rating FROM products_denormalize"
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query)
        outputs = cursor.fetchall()
        conn.commit()
    except Error as error:
        print(error)
        print(db_config)
        sys.exit(1)
    finally:
        cursor.close()
        conn.close()

    json_for_data = {
        'product_info': [],
        'product_link': [],
        'calculated': {
            'avr_price': [],
            'avr_rating': [],
        }
    }
    # {} type: dictionary

    for row in outputs:
        product = {
            'id': row[0],
            'brand': row[1],
            'category': row[2],
            'price': row[3],
            'title': row[4],
            'review': row[5],
            'rating': row[6],
            'image_link': row[7],
            'from_page_link': row[9]
        }
        json_for_data['product_info'].append(product)
        prod_link = {
            'id': row[0],
            'product_link': row[8]
        }
        prod_avr_price = {
            'id': row[0],
            'avr_price': row[10],
        }
        prod_avr_rating = {
            'id': row[0],
            'avr_rating': row[11]
        }
        json_for_data['product_link'].append(prod_link)
        json_for_data['calculated']['avr_price'].append(prod_avr_price)
        json_for_data['calculated']['avr_rating'].append(prod_avr_rating)

    with open('Data_smart_phone_tablet.json', 'w', encoding='utf-8') as outfile:
        json.dump(json_for_data, outfile, indent=4, ensure_ascii=False)

    """ indent=4 => file json look more clearly
    ensure_ascii=false => since json.dump() convert any character that is not in ASCII into strange string
    => hard to understand => use this func to keep non ASCII character to JSON file """

save_to() #run code