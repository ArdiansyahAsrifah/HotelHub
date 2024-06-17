from app import app, db
from flask import request, jsonify
from app.models.user import User

@app.route("/users", methods=["POST", "GET"])
def users():
    if request.method == "POST":
        username = request.json["username"]
        password = request.json["password"]
        role = request.json["role"]
        new_user = User(username=username, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User berhasil ditambahkan"}), 201

    if request.method == "GET":
        users = User.query.all()
        user_list = [user.to_dict() for user in users]
        return jsonify(user_list)

@app.route("/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def user(user_id):
    user = User.query.get_or_404(user_id)
    
    if request.method == "GET":
        return jsonify(user.to_dict())
    
    if request.method == "PUT":
        user.username = request.json["username"]
        user.password = request.json["password"]
        user.role = request.json["role"]
        db.session.commit()
        return jsonify({"message": "User berhasil diperbarui"})
    
    if request.method == "DELETE":
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User berhasil dihapus"})
