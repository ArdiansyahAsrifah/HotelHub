from app import app, db
from flask import request, jsonify
from app.models.room import Room

@app.route("/rooms", methods=["POST", "GET"])
def rooms():
    if request.method == "POST":
        hotel_id = request.json["hotel_id"]
        room_number = request.json["room_number"]
        room_type = request.json["room_type"]
        price = request.json["price"]
        new_room = Room(hotel_id=hotel_id, room_number=room_number, room_type=room_type, price=price)
        db.session.add(new_room)
        db.session.commit()
        return jsonify({"message": "Room berhasil ditambahkan"}), 201

    if request.method == "GET":
        rooms = Room.query.all()
        room_list = [room.to_dict() for room in rooms]
        return jsonify(room_list)

@app.route("/rooms/<int:room_id>", methods=["GET", "PUT", "DELETE"])
def room(room_id):
    room = Room.query.get_or_404(room_id)
    
    if request.method == "GET":
        return jsonify(room.to_dict())
    
    if request.method == "PUT":
        room.hotel_id = request.json["hotel_id"]
        room.room_number = request.json["room_number"]
        room.room_type = request.json["room_type"]
        room.price = request.json["price"]
        db.session.commit()
        return jsonify({"message": "Room berhasil diperbarui"})
    
    if request.method == "DELETE":
        db.session.delete(room)
        db.session.commit()
        return jsonify({"message": "Room berhasil dihapus"})
