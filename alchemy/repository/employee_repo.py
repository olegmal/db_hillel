from alchemy.models.employee_model import EmployeeModel
from alchemy.session import session


class EmployeeRepository:
    def __init__(self):
        self.__session = session
        self.__model = EmployeeModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def get_by_id(self, id):
        employee = self.__session.get(self.__model, {'id': id})
        return employee

    def add_employee(self, employee: EmployeeModel):
        self.__session.add(employee)

    def remove_employee_by_id(self, id):
        bicycle = self.__session.get(self.__model, {'id': id})
        self.__session.delete(bicycle)


if __name__ == "__main__":
    repo = EmployeeRepository()
    result = repo.get_all()
    for employee in result:
        print(employee)

    repo.add_employee('Vinona', 'Rider', 'Female', 'vrider@themeforest.net', '1973-06-28', 'USA')
    repo.remove_employee_by_id(10)
    print(repo.get_all())
    print(repo.get_by_id(5))


