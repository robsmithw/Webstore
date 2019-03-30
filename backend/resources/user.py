from flask_restful import Resource
import os
import json

class User(Resource):
    def get(self): #In the future I will be setting this up to connect to a db
        return {
    "Users":[
        {
            "id":1,
            "user_name": "a_user_name",
            "password": "a_hashed_value",
            "selling":[{
                "item_id":1
            },
            {"item_id" : 2
            }]
        },
        {
            "id":3,
            "user_name": "a_user_name",
            "password": "a_hashed_value",
            "selling":[{
                "item_id":3
            },
            {"item_id" : 4
            }]
        },
        {
            "id":3,
            "user_name": "a_user_name",
            "password": "a_hashed_value",
            "selling":[{
                "item_id":5
            },
            {"item_id" : 6
            },{
                "item_id":7
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