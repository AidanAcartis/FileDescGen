#!/bin/bash

# Obtenir la date actuelle
today=$(date '+%Y-%m-%d')

# Charger le fichier log dans un tableau (inversé pour chercher depuis la fin)
mapfile -t log_lines < <(tac ~/window_changes.log)

# Fonction pour récupérer l'heure de fermeture d'un fichier
get_close_time() {
    local file_name="$1"
    for ((i=0; i<${#log_lines[@]}; i++)); do
        if [[ "${log_lines[i]}" =~ "Fenêtres fermées" ]]; then
            local close_time=$(echo "${log_lines[i]}" | awk '{print $2}')
            local closed_file=$(echo "${log_lines[i+1]}" | awk -F ' aidan ' 'NF>1 {split($2, arr, " - "); title=""; for (j=1; j<=length(arr)-2; j++) title = title (j>1 ? " - " : "") arr[j]; print title ? title : arr[1]}')
            if [[ "$closed_file" == *"$file_name"* ]]; then
                echo "$close_time"
                return
            fi
        fi
    done
    echo "N/A"
}

# Trouver les fichiers ouverts aujourd'hui uniquement
find /home/aidan/ -type f ! -path '*/.*' -atime 0 2>/dev/null | while read file; do
    # Récupérer la date et l'heure d'accès (ouverture)
    open_time=$(stat --format='%x' "$file" | awk '{print $1, $2}')

    # Vérifier si la date d'ouverture correspond à aujourd'hui
    if [[ $(echo "$open_time" | awk '{print $1}') == "$today" ]]; then
        # Vérifier si le fichier est encore ouvert avec `lsof`
        if lsof -t -- "$file" > /dev/null 2>&1; then
            close_time="N/A"
        else
            # Récupérer l'heure de fermeture depuis le log
            close_time=$(get_close_time "$file")
        fi

        # Afficher le résultat formaté
        echo "$open_time $close_time $file"
    fi
done | sort -k1,1 -k2,2
