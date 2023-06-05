from alchemy.models.bicycle_model import BicycleModel
from alchemy.session import session

class BicycleRepository:
    def __init__(self):
        self.__session = session
        self.__model = BicycleModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def get_by_id(self, role_id):
        bicycle = self.__session.get(self.__model, {'id': id})
        return bicycle

    def add_item(self, bicycle: BicycleModel):
        self.__session.add(bicycle)

    def remove_item_by_id(self, id):
        bicycle = self.__session.get(self.__model, {'id': id})
        self.__session.delete(bicycle)



if __name__ == "__main__":
    bicycle_repo = BicycleRepository()
    result = bicycle_repo.get_all()
    for bicycle in result:
        print(bicycle)
        print(bicycle.type)

    bicycle_to_insert = BicycleModel(type="cruiser bike")
    bicycle_repo.add_item(bicycle_to_insert)
    bicycle_repo.remove_item_by_id(2)
    result = bicycle_repo.get_all()
    for i in result:
        print(i)
        print(i.type)
    # test_get_by_id_bicycle = bicycle_repo.get_by_id(1)
    # print(test_get_by_id_bicycle)
