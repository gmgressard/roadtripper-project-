from flask import Flask, render_template, request, session, redirect, url_for
from model import connect_to_db
import crud


app = Flask(__name__)  

app.secret_key = "^$hgj%^#^4#5&%34$#&%$w2H*5n3"


@app.route('/')
def home():
    """login page"""
    return render_template("index.html")


@app.route('/login', methods=['POST', 'GET'])
def login_user():
    """login page"""
    user = request.form["username"]
    email = request.form["email"]
    password = request.form['password']

    # if get_user(username) == True:
    #     session["email"]
    if request.method == "POST":
        session["user"] = user
        return redirect("/profile")
    else:
        return render_template("index.html")


@app.route('/profile')
def homepage():
    """homepage profile for user"""
    if "user" in session:
        return render_template("profile.html")
    else:
        alert("You are not logged in.")
        return redirect("/login")


# @app.route("/register")
# def registration():
#     return render_template("register.html")
#     return redirect("/createuser")


# @app.route("/createuser")
# def create_user():
#     """create new user and save to db"""

#     user = request.form["username"]
#     email = request.form["email"]
#     password = request.form['password']
#     fname = request.form['fname']
#     lname = request.form['lname']

#     if user in get_user(username):
#         return flash("Already in database")
#         return redirect("/")
#     else:
#         new_user = create_user(username=username, password=password, email=email)

#     return redirect("/")


# @app.route('/logout')
# def logout():
#     session.pop("user", None)
#     return redirect('/login')



if __name__=='__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')