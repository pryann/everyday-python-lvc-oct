import openpyxl


def read_xlsx(file_path, skip_headers_count=0):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    rows = list(sheet.iter_rows(values_only=True))
    # if skip_header:
    #     return rows[1:]
    # else:
    #     return rows

    return rows[skip_headers_count:] if skip_headers_count != 0 else rows


if __name__ == "__main__":
    data = read_xlsx("./files/employees-with-header.xlsx", 1)
    print(data)
