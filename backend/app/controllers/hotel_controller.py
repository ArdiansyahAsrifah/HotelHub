from app import app, db
from flask import request, jsonify
from app.models.hotel import Hotel


@app.route("/hotels", methods=["POST", "GET"])
def hotels():
    if request.method == "POST":
        name = request.json["name"]
        address = request.json["address"]
        details = request.json.get("details")
        new_hotel = Hotel(name=name, address=address, details=details)
        db.session.add(new_hotel)
        db.session.commit()
        return jsonify({"message": "Hotel berhasil ditambahkan"}), 201

    if request.method == "GET":
        hotels = Hotel.query.all()
        hotel_list = [hotel.to_dict() for hotel in hotels]
        return jsonify(hotel_list)

@app.route("/hotels/<int:hotel_id>", methods=["GET", "PUT", "DELETE"])
def hotel(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    
    if request.method == "GET":
        return jsonify(hotel.to_dict())
    
    if request.method == "PUT":
        hotel.name = request.json["name"]
        hotel.address = request.json["address"]
        hotel.details = request.json.get("details", hotel.details)
        db.session.commit()
        return jsonify({"message": "Hotel berhasil diperbarui"})
    
    if request.method == "DELETE":
        db.session.delete(hotel)
        db.session.commit()
        return jsonify({"message": "Hotel berhasil dihapus"})
