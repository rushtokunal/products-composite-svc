import pytest
from main import app
import json

#enter sample product id and form the endpoint
product_id="567"
url = "/products-svc/"+str(product_id)

def test_get_product():
    print (url)
    response = app.test_client().get(url)
    assert response.json['product_id'] == '567'
    assert response.status_code == 200

def test_upd_product_retail():
    #Content type must be included in the header
    header = {"content-type": "application/json"}
    #sample test data for updating
    data = {'product_id':'567',
            'current_price':10.99,
            'currency_code':'AED',
            'updated_by':'pytest'}
    response = app.test_client().put(url, data = json.dumps(data), headers=header)
    assert response.json['current_price'] == 10.99
    assert response.json['currency_code'] == 'AED'
    assert response.json['updated_by'] == 'pytest'
    assert response.status_code == 201 # the response code for update is 201