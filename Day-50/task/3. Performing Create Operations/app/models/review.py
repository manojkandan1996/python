from .. import db
from datetime import datetime

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', backref='reviews', lazy=True)
    product = db.relationship('Product', backref='reviews', lazy=True)

    def __repr__(self):
        return f"<Review U{self.user_id} P{self.product_id} ⭐{self.rating}>"
