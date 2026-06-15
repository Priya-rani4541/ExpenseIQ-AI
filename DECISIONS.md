# DECISIONS.md

## Decision 1: Django REST Framework

Options:

* Flask
* FastAPI
* Django REST Framework

Chosen:

* Django REST Framework

Reason:

* Built-in ORM, authentication support, admin panel, and rapid API development.

---

## Decision 2: React Frontend

Options:

* HTML/CSS/JS
* Angular
* React

Chosen:

* React

Reason:

* Industry-standard frontend framework and easier integration with REST APIs.

---

## Decision 3: SQLite During Initial Development

Options:

* PostgreSQL
* SQLite

Chosen:

* SQLite

Reason:

* Faster local development and simpler deployment during MVP phase.

Future:

* PostgreSQL migration planned.

---

## Decision 4: CSV-Based Import

Options:

* Manual Expense Entry
* CSV Import

Chosen:

* CSV Import

Reason:

* Assignment requirement and bulk expense ingestion support.

---

## Decision 5: Cloud Deployment

Options:

* Local Hosting
* Render + Vercel

Chosen:

* Render for Backend
* Vercel for Frontend

Reason:

* Free hosting, CI/CD integration, and simple deployment workflow.
