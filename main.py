import requests
import json
from flask import Flask, request, jsonify
#from flask_cors import CORS  # avoid cors errors if called from frontend
import os
os.environ['no_proxy']='*'

app = Flask(__name__)
#CORS(app)

@app.route('/products-svc/<string:product_id>', methods=['GET','PUT'])
def get_products(product_id):
    product_url = "http://127.0.0.1:5000/products/"+str(product_id)
    product_retl_url = "http://127.0.0.1:5002/products-retail/"+str(product_id)

    def get_combine():
        r_prod = requests.get(url = product_url)
        r_prod_retl = requests.get(url = product_retl_url)
        combine = r_prod.json()
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
    app.run(debug=True)
