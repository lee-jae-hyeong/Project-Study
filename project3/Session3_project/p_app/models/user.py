from p_app import db


class User(db.Model):
    __tablenamel__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), nullable = False)
    # password = db.Column(db.String(32), nullable = False)
    lists = db.relationship('List', backref = 'list', lazy = 'subquery', cascade = 'all, delete')



    def __repr__(self):
        return f"table {self.id}"