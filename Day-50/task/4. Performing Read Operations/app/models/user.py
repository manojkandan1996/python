from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    # Relationship to Blog and Review (optional if you have reviews)
    blogs = db.relationship('Blog', backref='author', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.name} ({self.email})>"
