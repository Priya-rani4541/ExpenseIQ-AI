# SCOPE.md

## Project Scope

ExpenseIQ AI is an expense management and analytics platform designed to ingest expense data from CSV files, validate records, detect anomalies, store normalized expense data, and provide reporting and AI-driven insights.

---

## Data Problems Found in CSV

### 1. Invalid Date Formats

Problem:

* Some records used inconsistent date formats.

Handling:

* Standardized dates using Python datetime parsing.
* Invalid dates were marked as failed imports.

---

### 2. Missing Required Fields

Problem:

* Some records had missing descriptions or amounts.

Handling:

* Validation rules rejected incomplete rows.
* Rows counted as invalid_rows.

---

### 3. Invalid Amount Values

Problem:

* Empty or non-numeric amount values.

Handling:

* Validation layer prevented insertion into database.

---

### 4. Duplicate Expense Records

Problem:

* Similar expense entries appeared multiple times.

Handling:

* Logged as potential anomalies.
* Currently stored but flagged for future duplicate detection.

---

## Database Schema

### ImportLog

| Field        | Type      |
| ------------ | --------- |
| id           | PK        |
| filename     | CharField |
| total_rows   | Integer   |
| valid_rows   | Integer   |
| invalid_rows | Integer   |
| status       | CharField |
| created_at   | DateTime  |

### Expense

| Field         | Type         |
| ------------- | ------------ |
| id            | PK           |
| date          | DateField    |
| description   | CharField    |
| paid_by       | CharField    |
| amount        | DecimalField |
| currency      | CharField    |
| split_type    | CharField    |
| split_with    | TextField    |
| split_details | TextField    |
| notes         | TextField    |
| import_log    | FK           |

Relationship:

ImportLog (1) ----> (Many) Expense
