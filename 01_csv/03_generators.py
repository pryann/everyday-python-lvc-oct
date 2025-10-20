import csv


def read_csv_file_generator(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        columns = next(reader, None)
        yield columns

        for row in reader:
            yield (dict(zip(columns, row)))


if __name__ == "__main__":
    csv_generator = read_csv_file_generator("./files/employees-with-header.csv")
    columns = next(csv_generator)
    print("Columns:", columns)
    for row in csv_generator:
        print("Row:", row)
