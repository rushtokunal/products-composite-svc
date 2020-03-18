import requests
import json
from flask import Flask, request, jsonify
#from flask_cors import CORS  # avoid cors errors if called from frontend
import os
os.environ['no_proxy']='*'

app = Flask(__name__)
#CORS(app)

@app.route('/', methods=['GET'])
def hello():
    return "Welcome to the Product Catalog composite Service Suite", 200

@app.route('/products-svc/<string:product_id>', methods=['GET','PUT'])
def get_products(product_id):
    product_url = "https://redsky.target.com/v2/pdp/tcin/"+str(product_id) # 13860428
    #product_url = "https://product-catalog-dot-python-game-changer.appspot.com/products/"+str(product_id)
    product_retl_url = "https://product-retail-dot-python-game-changer.appspot.com/products-retail/"+str(product_id)

    def get_combine():
        header = {"content-type": "application/json"}
        r_prod = requests.get(url = product_url)
        data = r_prod.json()
        #print(data['product']['item']['product_description']['title'])
        r_prod_retl = requests.get(url = product_retl_url)
        product_data = {'product_id':product_id,
                       'name':data['product']['item']['product_description']['title']}
        combine = product_data
        combine.update(r_prod_retl.json())
        return combine

    if request.method == "GET":
        print("1st in GET")
        return get_combine(), 200 #code 200 for successful GET
    
    if request.method == "PUT":
        #Content type must be included in the header
        header = {"content-type": "application/json"}
        data = {'product_id':product_id,
                'current_price':request.json['current_price'],
                'currency_code':request.json['currency_code'],
                'updated_by':request.json['updated_by']}
        resp_retl_upd = requests.put(url = product_retl_url, data = json.dumps(data), headers=header)
        return get_combine(), 201 #code 201 for successful PUT and GET
if __name__ == '__main__':
    app.run(port=5003,debug=True)
