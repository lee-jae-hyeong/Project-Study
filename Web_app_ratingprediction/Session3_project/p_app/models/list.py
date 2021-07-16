from p_app import db


class List(db.Model):
    __tablenamel__ = 'list'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), nullable = False)
    director = db.Column(db.String(32), nullable = False)
    genre = db.Column(db.String(32), nullable = False)
    country = db.Column(db.String(32), nullable = False)
    actor1 = db.Column(db.String(32), nullable = False)
    actor2 = db.Column(db.String(32), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    username = db.Column(db.String(32), db.ForeignKey('user.username'))

    

    def __repr__(self):
        return f"table {self.id}"