from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Expense(BaseModel):
    id: int
    title: str
    amount: int
    category: str

ExpenseList: List[Expense] = []

@app.post("/expense")
def add_expense(expense_obj: Expense):
    ExpenseList.append(expense_obj)
    return {"message": "Expense added successfully."}

@app.get("/expense")
def get_list():
    return ExpenseList

@app.delete("/expense/{expense_id}")
def delete_id(expense_id: int):
    for index, expense_obj in enumerate(ExpenseList):
        if expense_id == expense_obj.id:
            
            ExpenseList.pop(index)
            return {"message":"Item deleted successfully"}
    return {"error": "Expense not found"}


@app.get("/expense/total")
def get_total_expenses():
    total = 0
    for i in ExpenseList:
        total += i.amount
    # return {"total": total}
    return {"message": f"sum is {total}"}
    
@app.get("/expense/categories/{category}")
def filter_by_category(category: str):
    filtered = []
    for i in ExpenseList:
        if i.category == category:
            filtered.append(i)
    return filtered
    