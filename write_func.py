import csv


def write_inital_files(filepath, headers, rows):
    with open(file=filepath, mode='w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)