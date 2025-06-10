from sqlalchemy import Column, Date, Float, Integer, String
from .database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    value = Column(Float, nullable=False)

    def __init__(self, name: str = None, value: float = None):
        self.name = name 
        self.value = value

class Income(Base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float, nullable=False)

    def __init__(self, value: float = None):
        self.value = value
    