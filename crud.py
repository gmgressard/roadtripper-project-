"""CRUD operations"""

from model import db, User, HikeInfo, PastHike, PlannedHike, connect_to_db


def create_user(username,password,fname,lname,email):
    """create and return new user"""

    new_user = User(username=username, password=password, fname=fname, lname=lname, email=email)

    db.session.add(new_user)
    db.session.commit()

    return new_user

def get_user(username):
    """check if user in db"""

    # user = User(username=username, password=password)
    current_user = User.query.filter_by(username=username).first()

    return current_user 


def create_hike(hike_name,coordinates,state,city,national_park,length,diificulty_rating,avg_rating):
    """create and return a hike"""

    hike_info = HikeInfo(hike_name=hike_name,state=state,city=city,nation_park=national_park,length=length,diifculty_rating=difficulty_rating,avg_rating=avg_rating)

    db.session.add(hike_info)
    db.session.commit()

    return hike_info


def past_hike(date):
    """look at past hike"""

    past_hike_info = PastHike(date=date)

    db.session.add(past_hike_info)
    db.session.commit()

    return past_hike_info


def planned_hike():

    planned_hike = PlannedHike()

    db.session.add(planned_hike)
    db.session.commit()

    return planned_hike



if __name__ == '__main__':
    from server import app
    connect_to_db(app)