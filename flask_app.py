from flask import Flask

app = Flask(__name__)


@app.get("/")
def accueil():
    return "Bonjour tchakounte ! Essaie /presentation"


@app.get("/presentation")
def presentation():
    return """
    <h1>Léa Martin</h1>
    <p>Je suis étudiante en <strong>première année d'informatique</strong>.</p>
    <h2>Ce que j'aime</h2>
    <ul>
        <li>Les jeux vidéo</li>
        <li>La musique</li>
        <li>Le code (bientôt !)</li>
    </ul>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
