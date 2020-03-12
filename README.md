# products-composite-svc
holds composite services for getting products and retail and updating retail
 
<p align="center">
  <img width="340" height="160" src="https://miro.medium.com/max/1266/1*vB-cUmm1_dBBt-4JtL0u5g.jpeg">
</p>

#### Brief
1. Created a NOSQL DB to hold products ids, description etc. and a REST service which exposes Product Catalog the details of the service is in this repository `https://github.com/rushtokunal/products-catalog`
2. Created a NOSQL DB to hold product retail, currency etc. and a REST service which exposes Product Retail the details of the service is in this repository `https://github.com/rushtokunal/products-retail`
3. Create a composite service which calls the above two services and combines the Product and retail information. BONUS, the composite service an also update the retail and currency of the product by id, the service is in this repository `https://github.com/rushtokunal/products-composite-svc`


Created a composite service which 
#### List of Product and Retail Routes, all are deployed in Google cloud platform and LIVE and PRODUCTION READY
| Request | Endpoint |  Details |
| --- | --- | --- |
| `GET` | `https://product-catalog-dot-python-game-changer.appspot.com/products/567`| Get Product by ID
| `GET` | `https://product-retail-dot-python-game-changer.appspot.com/products-retail/567/`| Get Retail by ID|
| `GET` | `https://product-composite-svc-dot-python-game-changer.appspot.com/products-svc/567`| Get Product+Retail Id|
| `PUT` | `https://product-composite-svc-dot-python-game-changer.appspot.com/products-svc/567`| Update Retail|

```
use this as the PUT request body to update the retail
{
	"product_id": "567",
	"current_price": "6.43",
	"currency_code": "CAD",
    "updated_by": "rt"
}
```

### Automated Test cases using Pytest
The automated test cases are located in the tests folder
follow the steps to run the automated test suite
1) run the composite service locally (you need python 3.7 installed)
   ```
   pip install -r requirements.txt
   python main.py
   the composite service will start in http://127.0.0.1:5000/
   ```
2) to run the test suite just run
   ```
   pytest -v
   ```

### Create python virtual env and install requirements 
```sh
pip install -r requirements.txt
```
### Configure Database
#### From [db_config_example.json](src/db_config_example.json) configure datbase url, name, user and password and create file db_config.json under src
```json
 {
   "db": {
            "url" : "mongodb://localhost:27017/",
            "name" :"db_name"
    }
 }
``` 


