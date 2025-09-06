import magic

def get_file_info(file_path):
    ms = magic.Magic()
    return ms.from_file(file_path)

file_path = input("Entrez le chemin du fichier : ")
info = get_file_info(file_path)
print(f"Informations sur le fichier : {info}")
