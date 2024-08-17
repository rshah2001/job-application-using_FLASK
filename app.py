from datetime import datetime
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Load environment variables from .env.local file
load_dotenv(".env.local")

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///data.db")
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER", "smtp.gmail.com")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT", 465))
app.config["MAIL_USE_SSL"] = os.getenv("MAIL_USE_SSL", "True") == "True"
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

db = SQLAlchemy(app)
mail = Mail(app)

# Creating a database and connecting it to the SQLAlchemy
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()  # Convert to date object
        occupation = request.form["occupation"]

        # Sending data to the database
        form = Form(first_name=first_name, last_name=last_name,
                    email=email, date=date_obj, occupation=occupation)
        db.session.add(form)
        db.session.commit()

        message_body = f"Thank you for your submission, {first_name}.\n\n" \
                       f"Here are your details:\n" \
                       f"First Name: {first_name}\n" \
                       f"Last Name: {last_name}\n" \
                       f"Date: {date}\n" \
                       f"Occupation: {occupation}\n\n" \
                       f"Thank you for your submission. We will get in touch with you shortly about your application!"

        message = Message(subject="New form submission",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[email],
                          body=message_body)

        mail.send(message)

        flash(f"{first_name}, your form was submitted successfully!", "success")

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
