import openpyxl
import json
from flask import Flask, request
jsonfile = open('POST.jspn', 'w')
templsforcar = open('templforcar.json','r')
templsforjson = open('templforjspn.json','r')
app = Flask(__name__)
x = '1235'
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        userid = request.json["user_id"]
        cart = request.json["cart"]
        jsontempl = templsforjson.read()
        for item in cart:
            itemname = item['item']
            itemprice = item['price']
            carttempl = templsforcar.read()
            carttempl.replace('"1",', itemname)
            carttempl.replace('"2",', itemprice)
            jsontempl.replace('{}', carttempl)
            jsontempl.replace(',', carttempl)
        json.dump(jsontempl, jsonfile, 'w')            
    if request.method == 'GET':
        return "GET"
if __name__ == "__main__":
    app.run()