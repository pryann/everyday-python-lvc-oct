import csv


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


def calcuate_statistics(data, column_name):
    stat = {"min": None, "max": None, "average": None, "count": 0, "sum": 0}
    values = []
    for item in data:
        try:
            value = float(item[column_name])
            values.append(value)
        except (ValueError, TypeError):
            continue

    if len(values) > 0:
        stat["count"] = len(values)
        stat["sum"] = sum(values)
        stat["min"] = min(values)
        stat["max"] = max(values)
        stat["average"] = stat["sum"] / stat["count"]

    return stat


def write_to_csv(file_path, data):
    if len(data) > 0:
        header = data[0].keys()
        with open(file_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)


if __name__ == "__main__":
    required_cols = ["yearly_salary", "years_of_experience"]
    file_path = "./files/employees-with-header.csv"
    output_file_path = "./files/employees-stat-oct.csv"

    try:
        csv_generator = read_csv_file_generator(file_path, required_cols)
        data = list(csv_generator)
        write_to_csv(output_file_path, data)
        stat = calcuate_statistics(data, "yearly_salary")
        print("Stat", stat)

    except ValueError as error:
        print("Error:", error)

    # try:
    #     print(
    #         calcuate_statistics(
    #             list(
    #                 read_csv_file_generator(
    #                     "./files/employees-with-header.csv",
    #                     ["yearly_salary", "years_of_experience"],
    #                 )
    #             ),
    #             "yearly_salary",
    #         )
    #     )

    # except ValueError as error:
    #     print("Error:", error)
