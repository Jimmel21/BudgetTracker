# schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ExpenseBase(BaseModel):
    category: str
    amount: float
    date: date

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    budget_id: int

    class Config:
        orm_mode = True

class BudgetBase(BaseModel):
    month: str  # Format: "YYYY-MM"
    total_budget: float

class BudgetCreate(BudgetBase):
    pass

class Budget(BudgetBase):
    id: int
    expenses: List[Expense] = []

    class Config:
        orm_mode = True
