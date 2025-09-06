import filetype

# Entrée du chemin depuis le terminal
file_path = input("Entrez le chemin du fichier : ")

try:
    kind = filetype.guess(file_path)
    if kind:
        print(f"Le fichier {file_path} est de type : {kind.mime}, extension suggérée : {kind.extension}")
    else:
        print(f"Type inconnu pour {file_path}")
except FileNotFoundError:
    print(f"Erreur : le fichier {file_path} n'existe pas.")
except Exception as e:
    print(f"Erreur lors de l'analyse : {e}")
