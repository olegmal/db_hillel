from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
# from alchemy.models.role_model import RoleModel

Base = declarative_base()

class BicycleModel(Base):
    __tablename__ = "bicycle"

    id = Column(INTEGER, primary_key=True)
    make = Column(VARCHAR(100))
    type = Column(VARCHAR(30))
    price = Column(VARCHAR(5))
    employee = relationship("EmployeeModel", back_populates="bicycle")

    def __str__(self):
        return f"id = {self.id},make = {self.make}, type = {self.type}, price = {self.price}"

class EmployeeModel(Base):
    __tablename__ = "employee"

    id = Column(INTEGER, primary_key=True)
    first_name = Column(VARCHAR(50))
    last_name = Column(VARCHAR(50))
    gender = Column(VARCHAR(15))
    email = Column(VARCHAR(70))
    date_of_birth = Column(INTEGER)
    country_of_birth = Column(VARCHAR(50))
    bicycle_id = Column(INTEGER, ForeignKey("employee.bicycle.id"))
    bicycle = relationship("BicycleModel", back_populates="employee")


    def __str__(self):
        return f"id = {self.id},fname={self.first_name},lname={self.last_name}, gender={gender}, email = {self.email},\
         dbirth = {self.date_of_birth}, cbirth = {self.country_of_birth}, bicycle_id ={self.bicycle_id}"