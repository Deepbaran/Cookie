from app import conn
from flask import make_response
from config.constants import Queries, RecipeQueries, Response

class RecipeModel():
    
    def __init__(self):
        self.cur = conn.cursor(dictionary=True)