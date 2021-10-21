"""CRUD operations"""

from model import db, User, HikeInfo, PastHike, PlannedHike, connect_to_db


def create_user(username,password,fname,lname,email):
    """create and return new user"""

    new_user = User(username=username, password=password, fname=fname, lname=lname, email=email)
   
    db.session.add(new_user)
    db.session.commit()

    return new_user


def get_user(username,password):
    """check if user in db"""

    user = User.query.filter_by(username = username, password=password).first() #one or first
    return user


def create_hike(hike_name,coordinates,state,city,national_park,length,difficulty_rating,avg_rating):
    """create and return a hike"""

    hike_info = HikeInfo(hike_name=hike_name,coordinates=coordinates,state=state,city=city,national_park=national_park,length=length,
                        difficulty_rating=difficulty_rating,avg_rating=avg_rating)

    db.session.add(hike_info)
    db.session.commit()


def get_np_and_state():
    """return all state, np connected"""

    np_states= db.session.query(HikeInfo.state,HikeInfo.national_park).all()
    print(np_states)
    

def get_states():
    """get all states"""
    states = db.session.query(HikeInfo.state).all()
    
    states_set = set()

    for state in states:
        states_set.add(state[0])

    states_list = list(states_set)
    sorted_states_list = sorted(states_list)
    
    return sorted_states_list


def get_national_parks(state):
    """get all national parks for chosen state"""

    national_parks= HikeInfo.query.filter_by(state=state).all()
    
    nat_parks_set = set()

    for national_park in national_parks:
        nat_parks_set.add(national_park.national_park)
        
    nat_parks_list = list(nat_parks_set)
    sorted_nat_parks = sorted(nat_parks_list)

    return sorted_nat_parks
    

def get_hikes(national_park):
    """get all hikes for given state"""

    national_parks= HikeInfo.query.filter_by(national_park=national_park).all()
    
    return national_parks

# def get_coord(hike_name):
#     """Get coordinates for hike"""

#     coord_list = []

#     coordinates = HikeInfo.query.filter_by(hike_name=hike_name).all()

#     return coordinates


def save_hike(date):
    """look at past hike"""

    past_hike_info = PastHike(date=date)

    db.session.add(past_hike_info)
    db.session.commit()

    return past_hike_info


# def make_planned_hike():

#     planned_hike = PlannedHike()

#     db.session.add(planned_hike)
#     db.session.commit()

#     return planned_hike



if __name__ == '__main__':
    from server import app
    connect_to_db(app)