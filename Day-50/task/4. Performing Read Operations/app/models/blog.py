from datetime import datetime
from .. import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)  # ✅ long text field
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key to User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Blog '{self.title}' by User ID {self.user_id}>"
