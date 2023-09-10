from app import conn
from flask import make_response
from config.constants import RecipeQueries, Response

class RecipeModel():
    
    def __init__(self):
        self.cur = conn.cursor(dictionary=True)

    def getAllRecipes_model(self):
        self.cur.execute(RecipeQueries.FETCH_ALL)
        result = self.cur.fetchall()
        if result:
            res = make_response({"payload": result}, 200)
        else:
            res = make_response({"message": Response.NO_DATA_FOUND}, 204)