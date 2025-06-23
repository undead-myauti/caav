from typing import Dict, List
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Expense
from .models import Income

class Model():
    def __init__(self):
        self.db: Session = SessionLocal()
    
    def get_expenses(self) -> List[Expense]:
        try:
            expenses = self.db.query(Expense).all()
            return expenses
        finally:
            self.db.close()

    def get_expense_by_id(self, id: int) -> Expense:
        try:
            expense = self.db.query(Expense).filter(Expense.id == id).first()
            return expense
        finally:
            self.db.close()

    def add_expense(self, data: Dict) -> Expense:
        expense = Expense(
            name=data["name"],
            value=data["value"]
        )

        self.db.add(expense)
        self.db.commit()
        self.db.refresh(expense)
        return expense

    def update_expense(self, id: int, name: str, value: float) -> Expense:
        expense = self.db.query(Expense).filter(Expense.id == id).first()
        expense.name = name
        expense.value = value
        self.db.commit()
        self.db.refresh(expense)
        return expense

    def get_annual_income(self) -> float:
        try:
            income = self.db.query(Income).first()
            return income.value*12
        finally:
            self.db.close()

    def get_monthly_income(self) -> float:
        try:
            income = self.db.query(Income).first()
            return income.value
        finally:
            self.db.close()

    def get_monthly_expenses(self) -> float:
        try:
            expenses = self.db.query(Expense).all()
            return sum(expense.value for expense in expenses)
        finally:
            self.db.close()

    def get_highest_expense(self) -> float:
        try:
            expenses = self.db.query(Expense).all()
            if expenses:
                return max(expense.value for expense in expenses)
            else:
                return 0
        finally:
            self.db.close()

    def get_remaining_income(self) -> float:
        try:
            income = self.get_monthly_income()
            expenses = self.get_monthly_expenses()
            return income - expenses
        finally:
            self.db.close()

    def update_income(self, value: float) -> Income:
        try:
            income = self.db.query(Income).first()
            income.value = value
            self.db.commit()
            self.db.refresh(income)
            return income
        finally:
            self.db.close()
