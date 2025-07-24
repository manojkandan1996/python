from .. import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Boolean, default=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    # Relationship (one-to-many from Category)
    category = db.relationship('Category', backref='products', lazy=True)

    def __repr__(self):
        return f"<Product {self.name} - ₹{self.price}>"
