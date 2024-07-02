import csv
from paths import USERS_PATH


def list_data(field, title, path):    
    field_to_extract = [field]
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)

        extracted_data = []
        for row in reader:
            extracted_row = {field: row[field] for field in field_to_extract}
            extracted_data.append(extracted_row)


    print(title)
    for data in extracted_data:
        for key, username in data.items():
            print(username)

    return


def delete_row(path, identifier_row, identifier):
    
    rows = []
    row_deleted = False
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not row[identifier_row] == identifier.lower().strip():
                rows.append(row)
            else:
                row_deleted = True


    with open(path, mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    if row_deleted:
        print(f'{identifier} deleted')
        return True
    
    print(f'{identifier} not found')
    return False