"""Models for users and hikes app"""


from flask_sqlalchemy import SQLAlchemy 

from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """User information"""

    __tablename__="users"

    user_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    username = db.Column(db.String(30), 
                        unique=True)
    password = db.Column(db.String(30))
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    email = db.Column(db.String(40))

    def __repr__(self):
        """Show user info"""
        return f'<Username:{self.username} email: {self.email} name:{self.fname} {self.lname}>'


class HikeInfo(db.Model):
    """Getting hike information from NP Hike Data Set"""

    __tablename__="hikes_info"

    hike_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    hike_name = db.Column(db.String)
    coordinates = db.Column(db.String)
    state = db.Column(db.String)
    city = db.Column(db.String)
    national_park = db.Column(db.String)
    length = db.Column(db.Float)
    difficulty_rating = db.Column(db.Integer)
    avg_rating = db.Column(db.Float)

    def __repr__(self):
        """Show hike info"""
        return f'<hike name:{self.hike_name} national park:{self.national_park} state:{self.state} city:{self.city} length: {self.length} difficulty_rating: {self.difficulty_rating} avg_rating: {self.avg_rating}>'
        

class PastHike(db.Model):
    """Past hike information saved"""

    __tablename__="past_hikes"

    past_hike_id = db.Column(db.Integer, 
                            primary_key=True, 
                            autoincrement=True)
    hike_id = db.Column(db.Integer, 
                        db.ForeignKey("hikes_info.hike_id"))
    user_id = db.Column(db.Integer, 
                        db.ForeignKey("users.user_id"))
    date = db.Column(db.DateTime)

    hike = db.relationship('HikeInfo', backref = "past_hikes")
    user = db.relationship('User', backref = "past_hikes")

    def __repr__(self):
        """Show info about past hike"""
        return f'<hike:{self.hike_id} date:{self.date}>'



class PlannedHike(db.Model):
    """Saved hikes to do in the future"""

    __tablename__="planned_hikes"

    planned_hike_id = db.Column(db.Integer, 
                                primary_key=True, 
                                autoincrement=True)
    hike_id = db.Column(db.Integer, 
                        db.ForeignKey("hikes_info.hike_id"))
    user_id = db.Column(db.Integer, 
                        db.ForeignKey("users.user_id"))

    hike = db.relationship('HikeInfo', backref = "planned_hikes")
    user = db.relationship('User', backref = "planned_hikes")

    def __repr__(self):
        """Show info about planned hike"""
        return f'<planned_hike:{self.planned_hike_id} user is:{self.uesr_id}>'



def connect_to_db(app, db_uri="postgresql:///hikes"):
    """Connect to database"""

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)