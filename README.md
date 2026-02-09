<img width="1916" height="958" alt="image" src="https://github.com/user-attachments/assets/826f502f-91c4-4797-b09a-e7036f774a32" />


# Expense Tracker API (FastAPI)

This project is a **backend-focused Expense Tracker REST API** built using **FastAPI**.

The goal of this project is to practice **API design, request validation, and backend business logic**, rather than frontend UI development.

---

## Features

- Add a new expense
- List all expenses
- Delete an expense by ID
- Calculate total expenses
- Filter expenses by category
- Automatic API documentation using Swagger UI

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## Project Structure

expense-tracker-api/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md


---

## How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Start the server
3. ```bash
uvicorn main:app --reload
```

4. Open API documentation
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

API Endpoints
Method	Endpoint	Description
POST	/expenses	Add a new expense
GET	/expenses	Get all expenses
DELETE	/expenses/{expense_id}	Delete expense
GET	/expenses/total	Get total expenses
GET	/expenses/categories/{category}	Filter by category

Sample Expense JSON
{
  "id": 1,
  "title": "Groceries",
  "amount": 500,
  "category": "food"
}


