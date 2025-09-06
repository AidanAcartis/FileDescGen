from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

# Entrée du chemin depuis le terminal
file_path = input("Entrez le chemin du fichier : ")

try:
    parser = createParser(file_path)
    if not parser:
        print(f"Impossible d'analyser {file_path}")
    else:
        metadata = extractMetadata(parser)
        if metadata:
            print("\n".join(metadata.exportPlaintext()))
        else:
            print(f"Aucune métadonnée trouvée pour {file_path}")
except FileNotFoundError:
    print(f"Erreur : le fichier {file_path} n'existe pas.")
except Exception as e:
    print(f"Erreur lors de l'analyse : {e}")
