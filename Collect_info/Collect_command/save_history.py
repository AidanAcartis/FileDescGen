import mysql.connector
import os
from datetime import datetime, timedelta

# Configuration de la connexion à la base de données
db_config = {
    "host": "localhost",
    "user": "jennie",  # Remplace par ton utilisateur MySQL
    "password": "nerd",  # Remplace par ton mot de passe MySQL
    "database": "commandes_db"
}

# Connexion à MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Lire le fichier d'historique
history_file = os.path.expanduser("~/.bash_history")

with open(history_file, "r") as file:
    lines = file.readlines()

# Variables pour stocker les données extraites
commandes = []
current_timestamp = None

# Obtenir la date actuelle au format "YYYY-MM-DD"
date_aujourdhui = datetime.now().strftime("%Y-%m-%d")

for line in lines:
    line = line.strip()
    if line.startswith("#"):
        try:
            current_timestamp = int(line[1:])  # Convertir le timestamp Unix
        except ValueError:
            current_timestamp = None
    elif current_timestamp is not None:
        # Convertir le timestamp en heure et date
        date_du_jour = datetime.fromtimestamp(current_timestamp).strftime("%Y-%m-%d")

        # Vérifier si la commande est d'aujourd'hui
        if date_du_jour == date_aujourdhui:
            heure_ouverture = datetime.fromtimestamp(current_timestamp).strftime("%H:%M:%S")
            heure_fermeture = (datetime.fromtimestamp(current_timestamp) + timedelta(seconds=2)).strftime("%H:%M:%S")

            # Ajouter uniquement les commandes d'aujourd'hui
            commandes.append((current_timestamp, "Commande", line, heure_ouverture, heure_fermeture, date_du_jour))

# Trier la liste des commandes par timestamp (du plus ancien au plus récent)
commandes.sort(key=lambda x: x[0])

# Insérer les données dans la base de données (sans le timestamp)
sql = """
INSERT INTO historique_commandes (type, Nom, heure_ouverture, heure_fermeture, jour)
VALUES (%s, %s, %s, %s, %s)
"""

# Exécuter la requête en excluant le timestamp (index 0)
if commandes:
    cursor.executemany(sql, [cmd[1:] for cmd in commandes])
    conn.commit()
    print(f"{len(commandes)} commandes d'aujourd'hui insérées dans la base de données.")
else:
    print("Aucune commande enregistrée aujourd'hui.")

# Fermer la connexion
cursor.close()
conn.close()
