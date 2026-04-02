from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import smtplib

app = Flask(__name__)
app.secret_key = "123abc"

# define the login form
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

# function to send email
def send_email(to_email):
    sender = "queenestheradekanmi@gmail.com"
    password = "iccs grlp ajct srrf"

    message = "Subject: Login Alert\n\nYou just logged in!"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, password)
    server.sendmail(sender, to_email, message)
    server.quit()

# route MUST be outside functions
@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email == "queenestheradekanmi@gmail.com" and password == "1234":
            send_email(email)
            return "Login successful! Email sent ✅"
        else:
            return "Wrong details ❌"

    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)