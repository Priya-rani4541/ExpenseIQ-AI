# ExpenseIQ AI – Intelligent Expense Analytics Platform

## Live Demo

Frontend: https://expense-iq-ai.vercel.app

Backend: https://expenseiq-ai.onrender.com

GitHub Repository:
https://github.com/Priya-rani4541/ExpenseIQ-AI

---

## Project Overview

ExpenseIQ AI is a full-stack expense management and analytics platform designed to simplify personal finance tracking.

The system allows users to:

* Upload expense data through CSV files
* Store and manage expenses
* Generate expense reports
* View analytics dashboards
* Detect spending anomalies
* Receive AI-powered financial insights

---

## Features Implemented

### Backend (Django REST Framework)

* CSV Upload API
* Expense Management API
* Import Logs
* Data Validation
* REST APIs

### Frontend (React + Vite)

* Home Page
* Project Information Dashboard
* Deployment Setup

---

## AI Component

Planned AI Features:

* Expense Pattern Analysis
* Spending Recommendations
* Budget Optimization Suggestions
* Expense Categorization
* Anomaly Detection

AI Technology:

* OpenAI API (Planned Integration)
* Pandas for Data Processing
* Machine Learning Based Analytics (Upcoming)

---

## Tech Stack

Frontend:

* React.js
* Vite
* Axios

Backend:

* Django
* Django REST Framework
* Python

Database:

* SQLite (Current)
* PostgreSQL (Planned)

Deployment:

* Vercel
* Render

Version Control:

* Git
* GitHub

---

## Setup Instructions

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Backend URL:

```text
http://127.0.0.1:8000
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## API Endpoints

### Upload CSV

POST

```text
/api/imports/upload/
```

### Expense List

GET

```text
/api/expenses/
```

---

## Current Project Status

Completed:

* CSV Import
* Expense Storage
* REST APIs
* Frontend Deployment
* Backend Deployment

In Progress:

* Dashboard Analytics
* AI Insights
* Anomaly Detection

Future Enhancements:

* PostgreSQL Migration
* Authentication
* Advanced AI Recommendations
* Expense Forecasting
* Interactive Charts
