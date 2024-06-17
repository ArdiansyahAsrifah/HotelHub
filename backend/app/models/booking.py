from app import db

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    hotel_id = db.Column(db.Integer, nullable=False)
    room_id = db.Column(db.Integer, nullable=False)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)

    def __init__(self, user_id, hotel_id, room_id, check_in, check_out):
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.room_id = room_id
        self.check_in = check_in
        self.check_out = check_out

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'hotel_id': self.hotel_id,
            'room_id': self.room_id,
            'check_in': self.check_in,
            'check_out': self.check_out
        }
