from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from post_list import posts
from registration_and_login import RegistrationForm, Loginform
# from pydantic import ValidationError
import logging
import pyscript


app = Flask(__name__)

app.config["SECRET_KEY"] = "ebb4d2cdeba11e178aeeb9aa8092c417"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///techfrontier.db"

db = SQLAlchemy(app)

# Just for now it ends up here
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default_profile_picture.jpg")
    password = db.Column(db.String(30), nullable=False)
    post = db.relationship('Post', backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', {self.email}, {self.image_file})"
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}, {self.date_posted}')"




@app.route("/")
@app.route("/home")
def main_page():
    return render_template("main.html")


@app.route("/blog")
def blog_page():
    return render_template("blog.html", posts=posts, title="Out Tech blog")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
                # Kurwa no poddaję się z tym pydantikiem, na razie przynajmniej
        # while True: 
        #     try:
        #         password_str = PasswordStr(password=form.password.data)
                # if password_str.password == form.confirm_password.data:
                    flash(f'Account created successfully for {form.username.data}')
                    return redirect(url_for('main_page'))
                # else:
                #     logging.error("Doesn't quite work")
            # except ValidationError as e:
            #     flash(f"You password is not correct. Here's why: {e.errors()[0]['ctx']['error'].args[0].__str__()}")
    return render_template("register.html", title="Sign up", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = Loginform()
    if form.validate_on_submit():
          if form.username.data == "MyszRemi" and form.password.data == "Grubamys6969":
                flash(f"Hello, {form.username.data}! You are currently logged in.")
                return redirect(url_for('main_page'))
          else:
                flash("Pip!", 'danger')
    return render_template("login.html", title="Sign in", form=form)


@app.route("/repl")
def repl():
    return render_template("repl.html", title="Free Python REPL")




if __name__ == "__main__":
    app.run(debug=True)
