from flask import Flask, render_template, request, redirect, abort
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
    
@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.get("/salut")
def salut():
    prenom = request.args.get("prenom", "inconnu")
    ville = request.args.get("ville", "nulle part")
    return f"Bonjour {prenom}, qui vient de {ville} !" 
 # 3xx : une redirection
@app.get("/home")
def home():
    return redirect("/")
    @app.get("/moi")
def moi():
    return render_template(
        "moi.html",
        ip=request.headers.get("X-Real-IP", request.remote_addr),
        navigateur=request.headers.get("User-Agent"),
        langues=request.headers.get("Accept-Language"),
        entetes=request.headers,
    )


# 4xx : un accès interdit
@app.get("/secret")
def secret():
    abort(403)


# Une page d'erreur 404 personnalisée
@app.errorhandler(404)
def page_introuvable(erreur):
    return render_template("404.html"), 404   
    
@app.get("/calcul")
def calcul():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return f"{a} + {b} = {a + b}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
