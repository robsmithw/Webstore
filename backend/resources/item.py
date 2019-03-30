from flask_restful import Resource

class Item(Resource):
    def get(self): #will query from db in future
        return {
    "for_sell":[
    {
    "id" : 1,       
    "item_name": "Basketball",
    "price": 30,
    "quantity":1,
    "status":"new",
    "instock": True,
    "Type" : [{
        "Sell": True,
        "rent": False
    }]
    }, 
    {
    "id" : 2,       
    "item_name": "HDMI Cable",
    "price": 5,
    "quantity":0,
    "status":"used",
    "instock": False,
    "Type" : [{
        "Sell": True,
        "rent": False
    }]
    }, 
    {
    "id" : 3,       
    "item_name": "VGA Cable",
    "price": 3,
    "quantity":0,
    "status":"new",
    "instock": False,
    "Type" : [{
        "Sell": True,
        "rent": False
    }]
    }, 
    {
    "id" : 4,       
    "item_name": "24 inch monitor",
    "price": 200,
    "quantity":1,
    "status":"new",
    "instock": True,
    "Type" : [{
        "Sell": True,
        "rent": False
    }]
    }, 
    {
    "id" : 5,       
    "item_name": "Speaker",
    "price": 50,
    "quantity":1,
    "status":"used",
    "instock": True,
    "Type" : [{
        "Sell": True,
        "rent": False
    }]
    }, 
    {
    "id" : 6,       
    "item_name": "Lightning Cable",
    "price": 10,
    "quantity":1,
    "status":"new",
    "instock": True,
    "Type" : [{
        "Sell": True,
        "rent": False
    }]
    }, 
    {
    "id" : 7,       
    "item_name": "A game",
    "price": 60,
    "quantity":1,
    "status":"new",
    "instock": True,
    "Type" : [{
        "Sell": True,
        "rent": True
    }]
    }
    ]
}
    def post(self):
        return
    def put(self):
        return
    def delete(self):
        return