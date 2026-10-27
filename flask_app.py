from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def accueil():
    return render_template("accueil.html")

@app.get("/presentation")
def presentation():
    return render_template("presentation.html", prenom="Léa", nom="Martin")

@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return f"<h1>Bonjour {prenom} !</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
