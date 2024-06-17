from app import app, db
from flask import request, jsonify
from app.models.payment import Payment

@app.route("/payments", methods=["POST", "GET"])
def payments():
    if request.method == "POST":
        booking_id = request.json["booking_id"]
        amount = request.json["amount"]
        payment_date = request.json["payment_date"]
        new_payment = Payment(booking_id=booking_id, amount=amount, payment_date=payment_date)
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({"message": "Payment berhasil ditambahkan"}), 201

    if request.method == "GET":
        payments = Payment.query.all()
        payment_list = [payment.to_dict() for payment in payments]
        return jsonify(payment_list)

@app.route("/payments/<int:payment_id>", methods=["GET", "PUT", "DELETE"])
def payment(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    
    if request.method == "GET":
        return jsonify(payment.to_dict())
    
    if request.method == "PUT":
        payment.booking_id = request.json["booking_id"]
        payment.amount = request.json["amount"]
        payment.payment_date = request.json["payment_date"]
        db.session.commit()
        return jsonify({"message": "Payment berhasil diperbarui"})
    
    if request.method == "DELETE":
        db.session.delete(payment)
        db.session.commit()
        return jsonify({"message": "Payment berhasil dihapus"})
