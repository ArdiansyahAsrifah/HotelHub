from app import app, db
from flask import request, jsonify
from app.models.booking import Booking

@app.route("/bookings", methods=["POST", "GET"])
def bookings():
    if request.method == "POST":
        user_id = request.json["user_id"]
        hotel_id = request.json["hotel_id"]
        room_id = request.json["room_id"]
        check_in = request.json["check_in"]
        check_out = request.json["check_out"]
        new_booking = Booking(user_id=user_id, hotel_id=hotel_id, room_id=room_id, check_in=check_in, check_out=check_out)
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking berhasil ditambahkan"}), 201

    if request.method == "GET":
        bookings = Booking.query.all()
        booking_list = [booking.to_dict() for booking in bookings]
        return jsonify(booking_list)

@app.route("/bookings/<int:booking_id>", methods=["GET", "PUT", "DELETE"])
def booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    
    if request.method == "GET":
        return jsonify(booking.to_dict())
    
    if request.method == "PUT":
        booking.user_id = request.json["user_id"]
        booking.hotel_id = request.json["hotel_id"]
        booking.room_id = request.json["room_id"]
        booking.check_in = request.json["check_in"]
        booking.check_out = request.json["check_out"]
        db.session.commit()
        return jsonify({"message": "Booking berhasil diperbarui"})
    
    if request.method == "DELETE":
        db.session.delete(booking)
        db.session.commit()
        return jsonify({"message": "Booking berhasil dihapus"})
