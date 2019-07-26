from flask_sqlalchemy import SQLAlchemy
from nzalawapp import app
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from nzalawapp import login_manager

#login_manager = LoginManager()

#login_manager.init_app(app)

db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))
   

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150),nullable = False )
    email = db.Column(db.String(150), unique = True,nullable = False)
    password = db.Column(db.String(256), nullable = False)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def __repr__(self):
        return 'Email: {}, Password: {}'.format(self.email,self.password)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

class ReviewForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), primary_key=True, unique=True)
    review = db.Column(db.String(300))
    

class ContactForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), primary_key=True, unique=True)
    phone_number = db.Column(db.Integer)
    address = db.Column(db.String(150))
    email_address = db.Column(db.String(100))

