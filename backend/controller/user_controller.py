from app import app
from model.user_model import UserModel
from flask import request

user_model = UserModel()

@app.post("/user")
def register_user_controller():
    return user_model.register_user_model(request.form)

@app.get("/user")
def get_all_users_controller():
    return user_model.get_all_users_model(request.args)

@app.get("/user/<id>")
def get_user_controller(id):
    return user_model.get_user_model(id)

@app.patch("/user/<id>")
def update_user_controller(id):
    return user_model.update_user_model(id, request.form)

@app.delete("/user/<id>")
def delete_user_controller(id):
    return user_model.delete_user_model(id)