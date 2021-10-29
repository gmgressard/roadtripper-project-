from flask import Flask, render_template, request, session, redirect, flash
from model import connect_to_db
import crud, model
import datetime
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required




from jinja2 import StrictUndefined #gives errors for undefined variables 
app = Flask(__name__)  
app.secret_key = '^$hgj%^#^4#5&%34$#&%$w2H*5n3'

login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """load user needed for flask login ext"""
    return crud.get_user_by_id(int(user_id))


@app.route('/')
def home():
    """login page"""

    return render_template("index.html")


@app.route('/login', methods=['POST','GET'])
def login():
    """login page"""

    username = request.form['username']
    password = request.form['password']

    user = crud.get_user(username=username, password=password)

    if current_user.is_authenticated:
        return redirect('/profile')

    if user:
        login_user(user)
        flash('you aer logged in')
        return redirect('/profile')

    flash('invalid login')
    return redirect('/')


@app.route('/profile', methods=['GET','POST'])
def homepage():
    """homepage profile for user"""
   #check if user is logged in 
   #if yes, show profile 
   #if no, go to login page 
    
    if current_user.is_authenticated:
        return render_template('profile.html')
    else:
        return redirect('/', current_user=current_user)
   

@app.route('/register')
def registration():
    return render_template('register-user.html')
    return redirect('/createuser')


@app.route('/createuser', methods = ['POST','GET'])
def create_new_user():
    """create new user and save to db"""

    #get user input for creating new account
    user = request.form['username']
    email = request.form['email']
    password = request.form['password']
    fname = request.form['fname']
    lname = request.form['lname']

    #check if user already in db
    db_user = crud.get_user(username=user,password=password) 

    # #if user in db, go back to log in
    # #if not, add user to db and go back to log in

    if db_user is not None:
        flash('Already in database')
        return redirect('/')
    else: 
        user = crud.create_user(username=user, password=password, fname=fname, lname=lname, email=email)
        return redirect('/')


@app.route('/newhike')
@login_required
def create_new_hike():
    """list states > NP"""
    
    states = crud.get_states()

    return render_template('states-newhike.html', states=states)


@app.route('/nationalparks')
@login_required
def national_parks():
    """get national parks from state"""
    
    chosen_state = request.args.get('state')

    national_parks = crud.get_national_parks(chosen_state)
    

    return render_template('nat-parks-newhike.html', state=chosen_state, national_parks=national_parks)
    

@app.route('/hikes')
@login_required
def hikes():
    """get hikes from national park"""

    chosen_national_park = request.args.get('national_park')

    hikes = crud.get_hikes(chosen_national_park)
    
    return render_template('hikes-newhike.html', hikes=hikes)


@app.route('/hike/<hike_name>')
@login_required
def hike(hike_name):
    """display details and map of hike"""

    hike_details = crud.get_hike_details(hike_name)

    coordinates = crud.get_coord(hike_name)
    print(coordinates)
    print("*******************")
  
    return render_template('hike-newhike.html', hike_details=hike_details, coordinates=coordinates)


@app.route('/savehike', methods=['GET', 'POST'])
@login_required
def save_hike():
    """save trip to user id and view on past hikes"""

    logged_in_user = current_user.user_id
    print(logged_in_user)
    print("************************")

    save_hike_id = request.form.get("hike_id")
    print(save_hike_id)
    print("***************************")

    datetime_object = datetime.datetime.now()

    save_hike = crud.save_hike(save_hike_id, logged_in_user, datetime_object)

    if logged_in_user is None:
        flash('Please log in to save hike')
    else:
        view_saved_hikes = crud.show_saved_hikes(logged_in_user)

    return render_template('saved-hikes.html', save_hike_id=save_hike_id, logged_in_user=logged_in_user, view_saved_hikes=view_saved_hikes)    


@app.route('/savedhikes')
@login_required
def view_past_hikes():
    return redirect('/savehike')


@app.route('/logout')
@login_required
def logout():
    """log user out"""

    logout_user()
    flash('You are logged out')

    return redirect('/')


@app.route('/updateprofile', methods=['POST', 'GET'])
@login_required
def update_user():
    """update user info"""

    # logged_in_user = current_user.user_id

    # new_username = request.form['new_username']
    # new_password = request.form['new_password']

    
    # new_username = user.username 
    # new_password = user.password 

    # flash('username and password updated')

    return render_template('user-info.html', current_user=current_user)




if __name__=='__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')