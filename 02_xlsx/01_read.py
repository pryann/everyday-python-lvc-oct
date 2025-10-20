import openpyxl


def read_xlsx(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(values_only=True):
        print(row)


if __name__ == "__main__":
    read_xlsx("./files/employees.xlsx")
