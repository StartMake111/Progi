import openpyxl
import json
from flask import Flask, request
app = Flask(__name__)
lastadd = 0
x = '1235'
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        userid = request.json["user_id"]
        cart = request.json["cart"]
        for item in cart:
            itemname = item['item']
            itemprice = item['price']
            

        json.dump(jsontempl, jsonfile, 'w')            
    if request.method == 'GET':
        return "GET"
if __name__ == "__main__":
    app.run()