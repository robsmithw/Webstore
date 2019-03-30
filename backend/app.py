from flask import Flask
from flask_restful import Api
from resources.item import Item
from resources.user import User

app = Flask(__name__)
api = Api(app)

api.add_resource(Item, "/items","/item/<item_id>")
api.add_resource(User, "/users","/user/<user_id>")

if __name__ == '__main__':
    app.run(port = 5000, debug=True)