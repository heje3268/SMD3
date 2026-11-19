import json

from pathlib import Path

from flask import Flask, jsonify, render_template

app = Flask(__name__)

DOSSIER = Path(__file__).parent

with open(DOSSIER / "donnees.json", "r", encoding="utf-8") as fichier:

    DONNEES = json.load(fichier)

print("Données chargées :", len(DONNEES), "territoires")

@app.route("/")

def home():

    return render_template("index.html")

@app.route("/api/donnees")

def get_donnees():

    return jsonify(DONNEES)

if __name__ == "__main__":

    app.run(debug=True)
