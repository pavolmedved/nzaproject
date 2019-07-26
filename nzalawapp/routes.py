from flask import render_template,redirect,url_for
from nzalawapp import app
from nzalawapp.forms import SignUpForm,LoginForm,ReviewForm,ContactForm
from flask_login import login_required,login_user,current_user,logout_user


from nzalawapp.models import db

# importing database model
from nzalawapp.models import User,check_password_hash

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/register",methods=["GET","POST"])
def createUser():
    form = SignUpForm()
    if form.validate_on_submit():
        print("The user is {}".format(form.username.data))
        user = User(form.username.data,form.email.data,form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("hello_world"))

    else:
        print("Form not valid")
        print(form.errors)
    
    return render_template("register.html",form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    user_email = form.email.data
    password = form.password.data
    user = User.query.filter(User.email == user_email).first()
    if user and check_password_hash(user.password,password):
        login_user(user)
        print(current_user.username)
        return redirect(url_for("hello_world"))
    print(form.email.data,form.password.data)
    return render_template("login.html",form=form)

@app.route('/logout')
def logout():
    logout_user()
    return render_template("home.html")



@app.route("/review", methods=["GET","POST"])
@login_required
def review():
    form = ReviewForm()
    return render_template("review.html",form=form)

@app.route("/contact",methods=["GET","POST"])
@login_required
def contact():
    form = ContactForm()
    return render_template("contact.html",form=form)