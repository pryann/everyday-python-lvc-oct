import csv

# a = 10
# message = "Hello, World!"
# out = "the value of 'a' is" + str(a) + " and the message is: " + message
# out_2 = "the value of 'a' is {0} and the message is: {1}".format(a, message)
# out_3 = f"the value of 'a' is {a**2} and the message is: {message.upper()}"


def validate_columns(file_columns, required_columns):
    missing_columns = [col for col in required_columns if col not in file_columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    return [file_columns.index(col) for col in required_columns]


def read_csv_file_generator(file_path, required_columns):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        columns = next(reader, None)
        col_indices = validate_columns(columns, required_columns)

        for row in reader:
            filtered_col = [row[i] for i in col_indices]
            yield (dict(zip(required_columns, filtered_col)))


if __name__ == "__main__":
    required_cols = ["yearly_salary", "years_of_experience"]
    file_path = "./files/employees-with-header.csv"

    try:
        csv_generator = read_csv_file_generator(file_path, required_cols)

        for row in csv_generator:
            print("Row: ", row)
    except ValueError as error:
        print("Error:", error)
