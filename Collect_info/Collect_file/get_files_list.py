input_file = "data_file.txt"
output_file = "Files_list.txt"

files = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        columns = line.strip().split()
        if len(columns) >= 6 and columns[4] == "file-directory-App":
            # Files are in column 6
            filename = columns[5]
            files.append(filename)

with open(output_file, "w", encoding="utf-8") as f_out:
    for idx, filename in enumerate(files, start=1):
        f_out.write(f"{idx} {filename}\n")

print(f"Lists of extract files in {output_file}")