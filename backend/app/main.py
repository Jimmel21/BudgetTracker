# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import Budget as BudgetModel, Expense as ExpenseModel
from schemas import BudgetCreate, Budget as BudgetSchema, ExpenseCreate, Expense as ExpenseSchema
from database import SessionLocal, init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Budget Tracker API")

# Configure CORS
origins = [
    "http://localhost:3000",  # Vue.js dev server
    "http://localhost:8080",
    "http://localhost:8000",
    # Add other origins if deploying
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD for Budget
@app.post("/budgets/", response_model=BudgetSchema)
def create_budget(budget: BudgetCreate, db: Session = Depends(get_db)):
    db_budget = db.query(BudgetModel).filter(BudgetModel.month == budget.month).first()
    if db_budget:
        raise HTTPException(status_code=400, detail="Budget for this month already exists")
    new_budget = BudgetModel(month=budget.month, total_budget=budget.total_budget)
    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)
    return new_budget

@app.get("/budgets/", response_model=List[BudgetSchema])
def read_budgets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    budgets = db.query(BudgetModel).offset(skip).limit(limit).all()
    return budgets

@app.get("/budgets/{month}", response_model=BudgetSchema)
def read_budget(month: str, db: Session = Depends(get_db)):
    budget = db.query(BudgetModel).filter(BudgetModel.month == month).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    return budget

# CRUD for Expense
@app.post("/expenses/", response_model=ExpenseSchema)
def create_expense(expense: ExpenseCreate, budget_id: int, db: Session = Depends(get_db)):
    budget = db.query(BudgetModel).filter(BudgetModel.id == budget_id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    new_expense = ExpenseModel(**expense.dict(), budget_id=budget_id)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@app.get("/expenses/{budget_id}", response_model=List[ExpenseSchema])
def read_expenses(budget_id: int, db: Session = Depends(get_db)):
    expenses = db.query(ExpenseModel).filter(ExpenseModel.budget_id == budget_id).all()
    return expenses