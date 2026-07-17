import csv

#reading the file and returning rows function
def get_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        all_rows = [row for row in reader]
    return all_rows
