from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

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