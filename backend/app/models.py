# models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True, index=True)
    month = Column(String, unique=True, index=True)  # e.g., "2024-10"
    total_budget = Column(Float)
    expenses = relationship("Expense", back_populates="budget")

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, index=True)
    budget_id = Column(Integer, ForeignKey('budgets.id'))
    category = Column(String)
    amount = Column(Float)
    date = Column(Date)
    budget = relationship("Budget", back_populates="expenses")
