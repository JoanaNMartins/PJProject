from flask import Flask, redirect, url_for


# Initiates the site
app = Flask(__name__)

@app.route("/")
def home():
    # in line html can be returned in a function
    return "Hello! Welcome to the main page!"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

# Initiates the site
if __name__ == "__main__":
    app.run()