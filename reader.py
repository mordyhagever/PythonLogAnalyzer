import csv
def get_file(file_path):
    all_rows = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            all_rows.append(row)
    return all_rows