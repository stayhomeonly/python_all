import csv


def get_csv_data(csv_file, line):
    with open(csv_file, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader, 1):
            if index == line:
                return row


csv_file = '../data/account.csv'
data = get_csv_data(csv_file, 1)
print(data)
