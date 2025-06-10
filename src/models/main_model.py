from typing import Dict, List
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Expense

class Model():
    def __init__(self):
        self.db: Session = SessionLocal()
    
    def get_expenses(self) -> List[Expense]:
        try:
            expenses = self.db.query(Expense).all()
            return expenses
        finally:
            self.db.close()

    def add_expense(self, data: Dict):
        expense = Expense(
            name=data["name"],
            value=data["value"]
        )

        self.db.add(expense)
        self.db.commit()
        self.db.refresh(expense)
        return expense
    
    def get_incomes(self):
        return self.incomes
