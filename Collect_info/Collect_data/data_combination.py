from pathlib import Path

# Fichiers source
file1 = Path("../Collect_file/data_file.txt")
file2 = Path("../Collect_command/data_command.txt")
output_file = Path("./data_collect.txt")

# Stockage des lignes formatées
lines = []

# Traitement du fichier 1 (file-directory-App)
with file1.open(encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 6:
            date = parts[0]
            time_open = parts[1]
            time_close = parts[2]
            duration = parts[3]
            type_ = parts[4]
            name = " ".join(parts[5:])
            lines.append(f"{date}\t{time_open}\t{time_close}\t{duration}\t{type_}\t{name}")

# Traitement du fichier 2 (Commande)
with file2.open(encoding="utf-8") as f:
    for line in f:
        parts = [x.strip() for x in line.strip().split(",")]
        if len(parts) >= 6:
            date = parts[0]
            time_open = parts[1]
            time_close = parts[2]
            duration = parts[3]
            type_ = parts[4]
            name = parts[5]
            lines.append(f"{date}\t{time_open}\t{time_close}\t{duration}\t{type_}\t{name}")

# Écriture du fichier final en TSV
with output_file.open("w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

print(f"✅ Fichier TSV généré : {output_file.resolve()}")
