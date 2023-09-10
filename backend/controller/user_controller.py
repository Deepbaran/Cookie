from app import app
from model.user_model import UserModel
from flask import request

user_model = UserModel()

@app.get("/user")
def getAllUsers_controller():
    return user_model.getAllUsers_model()

@app.get("/user/<id>")
def gegUser_controller(id):
    return user_model.getUser_model(id)

@app.post("/user")
def registerUser_controller():
    return user_model.registerUser_model(request.form)