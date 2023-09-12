from app import conn
from flask import make_response
from config.constants import Queries, UserQueries, Response
import base64

class UserModel():
    
    def __init__(self):
        self.cur = conn.cursor(dictionary=True)

    def register_user_model(self, data):
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        password = base64.b64encode(data.get('password', '').encode('utf-8'))
        phone_no = data.get('phone_no', '')
        qry = UserQueries.INSERT_USER_RECORD % (
            first_name, last_name, email, password, phone_no
            )
        self.cur.execute(qry)
        return make_response({"message": Response.RECORD_CREATED_SUCCESSFULLY}, 201)
    
    def get_all_users_model(self, args):
        # get all users with pagination
        limit = int(args.get("limit"))
        page = int(args.get("page"))
        start = (page * limit) - limit
        self.cur.execute(Queries.FETCH_ALL % ('users', start, limit))
        result = self.cur.fetchall()
        if result:
            return make_response({"payload": result}, 200)
        else:
            return make_response({"message": Response.NO_DATA_FOUND}, 204)

    def get_user_model(self, id):
        self.cur.execute(Queries.FETCH_BY_ID % ('users', id))
        result = self.cur.fetchall()
        if result:
            res = result[0]
            return make_response({"payload": res}, 200)
        else:
            return make_response({"message": Response.NO_DATA_FOUND}, 204)
    
    def update_user_model(self, id, data):
        qry = UserQueries.UPDATE_USER
        for k, v in data.items():
            qry += f"{k}='{v}',"
        qry = qry[:-1] + f"WHERE id='{id}'"
        self.cur.execute(qry)
        if self.cur.rowcount > 0:
            return make_response({"message": Response.RECORD_UPDATED_SUCCESSFULLY}, 201)
        else:
            return make_response({"message": Response.NOTHING_TO_UPDATE}, 201)
        
    def delete_user_model(self, id):
        self.cur.execute(UserQueries.DELETE_USER % (id,))
        if self.cur.rowcount > 0:
            return make_response({'message': Response.RECORD_DELETED_SUCCESSFULLY}, 200)
        else:
            return make_response({'message': Response.NOTHING_TO_DELETE}, 202)