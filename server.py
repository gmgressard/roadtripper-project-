from flask import Flask, render_template, request, session, redirect, flash
from model import connect_to_db
import crud


app = Flask(__name__)  

app.secret_key = '^$hgj%^#^4#5&%34$#&%$w2H*5n3'


@app.route('/')
def home():
    """login page"""
    return render_template("index.html")


@app.route('/login', methods=['POST','GET'])
def login_user():
    """login page"""
    #get username and password input
    user = request.form['username']
    password = request.form['password']

    #validate that it is in db
    user = crud.get_user(username=user,password=password) 
    print(user)

    #validate username and password are connected 
    #create session
    #login to profile 
    if user:
        session["user_id"] = user.user_id
        session["username"] = user.username 
        return redirect("/profile")
    else: 
        flash("No user found, please create account")
        return render_template("index.html")


@app.route('/profile', methods=['GET','POST'])
def homepage():
    """homepage profile for user"""
   #check if user is logged in 
   #if yes, show profile 
   #if no, go to login page 
    
    if "user_id" in session: #key user id in session dic line 32
        return render_template("profile.html")
    else:
        flash('You are not logged in.')
        return redirect('/')


@app.route('/register')
def registration():
    return render_template('register.html')
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

    # user = crud.create_user(username=user, password=password, fname=fname, lname=lname, email=email)
    # print("*********")
    # print(user)
    # print("*********")
        # return redirect('/')

    #check if user already in db
    db_user = crud.get_user(username=user,password=password)
    print("*********")
    print(db_user)
    #if user in db, go back to log in
    #if not, add user to db and go back to log in
    if db_user is None:
        flash('Already in database')
        redirect('/')
    else: 
        user = crud.create_user(username=user, password=password, fname=fname, lname=lname, email=email)
        print("*********")
        print(user)
        print("*********")
        return redirect('/')


# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect('/login')



if __name__=='__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')