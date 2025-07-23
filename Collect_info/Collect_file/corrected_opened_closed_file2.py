#!/usr/bin/env python3

def treat_lines(infile, outfile):
    """Lit un fichier ligne par ligne, supprime les lignes impaires, traite chaque ligne et écrit le résultat."""

    try:
        # Lire toutes les lignes du fichier source
        with open(infile, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Ne garder que les lignes paires (index 1, 3, 5... en base 0)
        even_lines = [line.strip() for i, line in enumerate(lines) if i % 2 == 1]

        # Liste temporaire pour stocker les lignes modifiées
        modified_lines = []

        for line in even_lines:
            dot_index = line.rfind('.')  # Trouver le dernier point

            if dot_index != -1:
                part1 = line[:dot_index]
                part2 = line[dot_index + 1:]

                # Garder uniquement le premier mot après le point
                part2 = part2.split()[0]
                result = f'{part1}.{part2}'
            else:
                result = line

            modified_lines.append(result)

        # Écriture dans le fichier de sortie
        with open(outfile, 'w', encoding='utf-8') as file:
            file.writelines(line + '\n' for line in modified_lines)

        print(f"[✓] Le fichier '{outfile}' a été généré avec succès.")

    except FileNotFoundError:
        print(f"[!] Fichier introuvable : {infile}")
    except Exception as e:
        print(f"[!] Erreur lors du traitement de {infile} : {e}")

# 🔁 Traitement des deux fichiers
treat_lines('Opened_file.txt', 'Opened_file_true.txt')
treat_lines('Closed_file.txt', 'Closed_file_true.txt')
