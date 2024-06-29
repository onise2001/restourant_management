import csv


def update_value_in_csv(path, identifier, value, identifier_column, value_column):
    rows = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[identifier_column] == identifier:
                row[value_column] = value
            rows.append(row)

    with open(path, 'w', newline='') as file:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


