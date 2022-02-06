from crypt import methods
from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    pass

if __name__ == "__main__":
    app.run(debug=True)

#   get is more general and is not private
#   post is more secure and it won't be saved in web
# server