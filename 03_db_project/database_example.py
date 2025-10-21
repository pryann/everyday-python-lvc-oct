import mysql.connector
from xlsx_handler import read_xlsx
from computations import generate_stat


def connect_to_mariadb(host, database, user, password, port=3306):
    try:
        connection = mysql.connector.connect(
            host=host, database=database, user=user, password=password, port=port
        )
        return connection
    except mysql.connector.Error as error:
        print("MardiaDB conection error:", error)
        return None


def create_table(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        print("Failed to create table:", error)


def insert_employees(connection, data):
    try:
        cursor = connection.cursor()
        # pass header info as parameters, or set up directly in the function
        # TODO: use batch insert for better performance!!!!
        query = "INSERT INTO employees(id, first_name,last_name, email_address, gender, yearly_salary, years_of_experience) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        for employee in data:
            cursor.execute(query, employee)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        print("Failed to insert data:", error)


def run_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    except mysql.connector.Error as error:
        print("Failed to run select query:", error)
        return None


def main(conn):
    table = """CREATE TABLE IF NOT EXISTS employees(
      id INT AUTO_INCREMENT PRIMARY KEY,
      first_name VARCHAR(50) NOT NULL,
      last_name VARCHAR(50) NOT NULL,
      email_address VARCHAR(100) NOT NULL UNIQUE,
      gender VARCHAR(50) NOT NULL,
      yearly_salary INT NOT NULL,
      years_of_experience TINYINT NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """

    create_table(conn, table)
    print(run_query(conn, "SHOW TABLES"))
    data = read_xlsx("./files/employees-with-header.xlsx", 1)
    insert_employees(conn, data)


if __name__ == "__main__":
    mariadb_config = {
        "host": "localhost",
        "database": "employees",
        "user": "employees",
        "password": "employees",
    }
    conn = connect_to_mariadb(**mariadb_config)
    # main(conn)
    result = run_query(conn, "SELECT yearly_salary FROM employees")
    salaries = [row[0] for row in result]
    print(salaries)
