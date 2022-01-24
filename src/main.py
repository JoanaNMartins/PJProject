from flask import Flask, redirect, url_for, render_template


# Initiates the site
app = Flask(__name__)


# derterminar o que aparece na "home" => "/" 
# Se content não estiver definido não aparece de todo

@app.route("/")
def home():
    # in line html can be returned in a function 
    return render_template("index.html", content="test", list=["Ju", "André", "Tsuki"])


# podem ser inseridas "variáveis" no argumento do "decorador", namely 
# entre <> temos uma variável, enquanto sem <> tem de se escrever mesmo esse valor
# Isto pode ser feito através do template, com {{}} no doc de html 

@app.route("/<name>")
def content(name):
    return render_template("index.html", content=name, r=2, list=[name])

# ou caso seja algo mais simples pode ser feito como está aqui, 
# com uma f-string

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

# Initiates the site and debug True faz com que o 
# programa detete as alterações no código e vá actualizando o site
if __name__ == "__main__":
    app.run(debug=True)