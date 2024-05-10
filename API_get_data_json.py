from flask import Flask, jsonify
import json

app = Flask(__name__)

def get_product_by_id(find_ID_data: str):
    with open('Data_smart_phone_tablet.json', 'r', encoding='utf-8') as in_file:
        list_products = json.load(in_file)

    #Since info is in many places => create a dictionary to combine all info
    full_data = {
        'id': None,
        'brand': None,
        'category': None,
        'price': None,
        'title': None,
        'review': None,
        'rating': None,
        'image_link': None,
        'product_link': None,
        'avr_price': None,
        'avr_rating': None
    }

    for product in list_products['product_info']:
        if product['id'] == find_ID_data:
            for info in product:
                full_data[info] = product[info]

    for link_prod in list_products['product_link']:
        if link_prod['id'] == find_ID_data:
            full_data['product_link'] = link_prod['product_link']

    for price_prod in list_products['calculated']['avr_price']:
        if price_prod['id'] == find_ID_data:
            full_data['avr_price'] = price_prod['avr_price']

    for rating_prod in list_products['calculated']['avr_rating']:
        if rating_prod['id'] == find_ID_data:
            full_data['avr_rating'] = rating_prod['avr_rating']

    return full_data
    """
    Lack of information => only return product_info
    for product in list_products['product_info']:
        if product["id"] == find_ID_data:
            return product

    for link in list_products['product_link']:
        if link["id"] == find_ID_data:
            return link['product_link']

    for rating in list_products['calculated']['avr_rating']:
        if rating["id"] == find_ID_data:
            return rating['avr_rating']

    for price in list_products['calculated']['avr_price']:
        if price["id"] == find_ID_data:
            return price['avr_rating']

    """

@app.route('/product', methods=['GET'])
def get_product():
    id_prod = '34928767' # => edit ID that you want to find
    product = get_product_by_id(id_prod)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product with {id_prod} does not exist"}), 404

if __name__ == '__main__':
    app.run(port=5000)
