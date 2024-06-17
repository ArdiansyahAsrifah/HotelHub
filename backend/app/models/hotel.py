from app import db

class Hotel(db.Model):
    __tablename__ = 'hotels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    details = db.Column(db.Text, nullable=True)

    def __init__(self, name, address, details=None):
        self.name = name
        self.address = address
        self.details = details

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'details': self.details
        }
