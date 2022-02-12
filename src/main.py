from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta


app = Flask(__name__)
# sets a secret key, necessary for when we keep a session
# "open"
app.secret_key= "hello"

# defines the lifetime of the session (for how long you keep the 
# user logged in)
app.permanent_session_lifetime = timedelta(days=7)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    # to take information out of a form, we need to use a 
    # post method 

    if request.method == "POST":
        # needed to say that we want that timeframe for keeping you logged in
        # if not specified it only keeps you logged in for however long you 
        # keep the browser open
        session.permanent = True

        # to save the information we use request.form and create a 
        # dictionary with the necessary info
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        # if you are already logged in you don't need to see the 
        # login page again
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

#   get is more general and is not private
#   post is more secure and it won't be saved in web
# server