from app import conn
from flask import make_response
from config.constants import UserQueries, Response
import base64

class UserModel():
    
    def __init__(self):
        self.cur = conn.cursor(dictionary=True)

    def getAllUsers_model(self):
        self.cur.execute(UserQueries.FETCH_ALL)
        result = self.cur.fetchall()
        if result:
            return make_response({"payload": result}, 200)
        else:
            return make_response({"message": Response.NO_DATA_FOUND}, 204)

    def getUser_model(self, id):
        self.cur.execute(UserQueries.FETCH_BY_ID % (id,))
        result = self.cur.fetchall()
        if result:
            res = result[0]
            return make_response({"payload": res}, 200)
        else:
            return make_response({"message": Response.NO_DATA_FOUND}, 204)
        
    def registerUser_model(self, data):
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        password = base64.b64encode(data.get('password', '').encode('utf-8'))
        phone_no = data.get('phone_no', '')
        query = UserQueries.INSERT_USER_RECORD % (
            first_name, last_name, email, password, phone_no
            )
        self.cur.execute(query)
        return make_response({"message": "User Created Successfully"}, 201)