import magic

# créer l'instance
ms = magic.Magic()

# demander le chemin du fichier à l'utilisateur
file_path = input("Entrez le chemin du fichier : ")

try:
    file_type = ms.from_file(file_path)
    print(f"Le fichier {file_path} est de type : {file_type}")
except FileNotFoundError:
    print(f"Erreur : le fichier {file_path} n'existe pas.")
except Exception as e:
    print(f"Erreur lors de la lecture du fichier : {e}")
