from app import db
from .hotel import Hotel

class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), nullable=False)
    room_number = db.Column(db.String(10), nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    hotel = db.relationship('Hotel', backref=db.backref('rooms', lazy=True))

    def __init__(self, hotel_id, room_number, room_type, price):
        self.hotel_id = hotel_id
        self.room_number = room_number
        self.room_type = room_type
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'hotel_id': self.hotel_id,
            'room_number': self.room_number,
            'room_type': self.room_type,
            'price': self.price
        }
