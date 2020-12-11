import openpyxl
import json
from flask import Flask, request
app = Flask(__name__)
lastadd = 1
x = '1235'
columnN,columnID,columnTime,columnItem,columnPrice = 0,1,2,3,4
book = openpyxl.Workbook()
sheet = book.active
sheet[1][0].value,sheet[1][1].value,sheet[1][2].value,sheet[1][3].value,sheet[1][4].value = 'N','User ID', 'Datetime','Item','Price'
book.save('data.xlsx')
book.close
nest = lastadd+1
@app.route('/', methods = ['POST', 'GET'])
def index(nest,lastadd):
    if request.method == 'POST':
        userid = request.json["user_id"]
        cart = request.json["cart"]
        book = openpyxl.Workbook()
        sheet = book.active
        sheet[nest][columnN].value = lastadd
        sheet[nest][columnID].value = userid
        for item in cart:
            lastadd+=1
            itemname = item['item']
            itemprice = item['price']
            sheet[lastadd][columnItem].value = itemname
            sheet[lastadd][columnPrice].value = itemprice
        book.save('data.xlsx')
        book.close
    if request.method == 'GET':
        return "GET"
if __name__ == "__main__":
    app.run()