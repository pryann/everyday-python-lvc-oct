import openpyxl


def write_list_to_xlsx(file_path, rows_list):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Employees"

    for row in rows_list:
        sheet.append(row)

    workbook.save(file_path)


def write_list_dict_to_xlsx(file_path, rows_list, allow_headers=True):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Employees"
    # if you have headers
    if allow_headers and len(rows_list):
        headers = list(rows_list[0].keys())
        sheet.append(headers)

    for row in rows_list:
        sheet.append(list(row.values()))

    workbook.save(file_path)


if __name__ == "__main__":
    rows = [
        [1, "John", "Doe", 30],
        [2, "Jane", "Doe", 22],
    ]
    write_list_to_xlsx("./files/employees-write-out.xlsx", rows)

    rows_dict = [
        {"id": 1, "first_name": "John", "last_name": "Doe", "age": 30},
        {"id": 2, "first_name": "Jane", "last_name": "Doe", "age": 22},
    ]

    write_list_dict_to_xlsx("./files/employees-write-out-2.xlsx", rows_dict)
