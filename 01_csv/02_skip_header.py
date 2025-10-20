import csv


def read_csv(file_path, skip_first=True):
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)

        if skip_first:
            next(reader, None)

        print([row for row in reader])


if __name__ == "__main__":
    read_csv("./files/employees-with-header.csv", False)
