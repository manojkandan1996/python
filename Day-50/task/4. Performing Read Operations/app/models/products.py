from .. import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Boolean, default=True)

    # Foreign key to Category
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    # Relationships
    category = db.relationship('Category', backref='products', lazy=True)
    reviews = db.relationship('Review', backref='product', lazy=True)

    def __repr__(self):
        return f"<Product {self.name} - ₹{self.price}>"
