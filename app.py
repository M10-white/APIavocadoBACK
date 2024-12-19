import pickle
import pandas as pd
from flask_cors import CORS
from flask import Flask, request, jsonify, render_template_string
import pandas as pd

app = Flask(__name__)

# Configurer CORS pour permettre les requêtes cross-origin
CORS(app)

# Charger le modèle préalablement sauvegardé
with open('src/avocado_price_model.pkl', 'rb') as model_file:
    model_pipeline = pickle.load(model_file)

@app.route('/')
def home():
    # HTML pour la page d'accueil avec le bouton
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>API BACK</title>
            <style>
                body {
                    background-color: #000;
                    color: #fff;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                }

                .button {
                    padding: 15px 30px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    font-size: 1.2rem;
                    cursor: pointer;
                    text-decoration: none;
                }

                .button:hover {
                    background-color: #45a049;
                }
                
                .button-top-right {
                    position: absolute;
                    top: 20px;
                    right: 20px;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    font-size: 1rem;
                    font-weight: bold;
                    cursor: pointer;
                    text-decoration: none;
                }
            </style>
        </head>
        <body>
            <a href="http://localhost:8080" class="button-top-right">ACCEDER AU FRONT</a>
            <h1>Bienvenue sur le back de l'API de prédiction du prix des avocats !</h1><br><br>
            <p><a href="/csv_data" class="button">Voir les données CSV</a></p>
        </body>
        </html>
    """)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données envoyées
        data = request.get_json()

        # Définitions des catégories valides
        valid_types = ["conventional", "organic"]
        valid_regions = ["Albany", "Atlanta", "Baltimore", ...]  # Liste des régions utilisées lors de l'entraînement

        # Validation des colonnes catégoriques
        if data["type"] not in valid_types:
            return jsonify({"error": f"Invalid type: {data['type']}. Expected one of {valid_types}."}), 400
        if data["region"] not in valid_regions:
            return jsonify({"error": f"Invalid region: {data['region']}. Expected one of {valid_regions}."}), 400

        # Conversion des données en DataFrame
        feature_data = {
            "Quality1": data["Quality1"],
            "Quality2": data["Quality2"],
            "Quality3": data["Quality3"],
            "Small Bags": data["Small Bags"],
            "Large Bags": data["Large Bags"],
            "XLarge Bags": data["XLarge Bags"],
            "year": data["year"],
            "type": data["type"],
            "region": data["region"],
        }
        features_df = pd.DataFrame([feature_data])

        # Prédire avec le modèle
        prediction = model_pipeline.predict(features_df)
        predicted_price = float(prediction[0])

        # Retourner la réponse
        return jsonify({"predicted_price": predicted_price})

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
# Route pour afficher les données du CSV en JSON
@app.route('/csv_data')
def display_csv_json():
    # Charger le fichier CSV
    df = pd.read_csv('src/back/avocado.csv') 
    
    # Convertir le DataFrame en dictionnaire et renvoyer en JSON
    data = df.to_dict(orient='records')
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)