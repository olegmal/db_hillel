import psycopg2

class BaseRepository:
    def __init__(self):
        self.connection = psycopg2.connect(user='postgres',
                              password = 'q9896',
                              host = '127.0.0.1',
                              port = '5432',
                              database = 'artlesscoder')

        self.connection.set_session(autocommit=True)
        self._cursor = self.connection.cursor()

class EmployeeRepository (BaseRepository):
    def __int__(self):
        super().__init__()

    def get_all_employee(self):
        self._cursor.execute("SELECT* FROM employee;")
        return self._cursor.fetchall()

    def get_employee_by_id(self, id):
        self._cursor.execute(f"SELECT * FROM employee WHERE employee.id = {id};")
        return self._cursor.fetchone()

    def insert_employee(self, first_name, last_name, gender, email, date_of_birth, country_of_birth):
        self.__cursor.execute(f"INSERT INTO users(first_name, last_name, gender, email, date_of_birth, country_of_birth)\
         VALUES ('{first_name}','{last_name}','{gender}', '{email}', '{date_of_birth}', '{country_of_birth}');")
        # self.__connection.commit()

    def delete_by_id(self, id):
        self._cursor.execute(f"DELETE FROM employee WHERE id ={id};")
        # self._connection.commit()

if __name__ == "__main__":
    rep = EmployeeRepository()
    rep.insert_employee('Reyna', 'Witsey', 'Female', 'rwitsey1v@themeforest.net', '1976-06-28', 'Philippines')
    rep.delete_by_id(10)
    print(rep.get_all_employee())
    print(rep.get_employee_by_id(5))
