import csv


def write_inital_files(filepath, headers, rows ):
    with open(filepath, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)