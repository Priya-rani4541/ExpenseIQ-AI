# AI_USAGE.md

## AI Tools Used

1. ChatGPT
2. GitHub Copilot (if used)

---

## Key Prompts

### Prompt 1

Design a production-ready PostgreSQL database schema for an expense management and anomaly detection platform.

Outcome:
Generated initial database architecture.

---

### Prompt 2

Generate Django REST Framework APIs for CSV upload and expense ingestion.

Outcome:
Accelerated backend development.

---

### Prompt 3

Create deployment configuration for Render and Vercel.

Outcome:
Successfully deployed backend and frontend.

---

## AI Mistakes and Corrections

### Case 1

AI Output:
Incorrect Django URL configuration.

Issue Found:
Application routes returned 404 errors.

Fix:
Manually updated urls.py and verified endpoint mappings.

---

### Case 2

AI Output:
Incorrect CSV date parsing logic.

Issue Found:
Date conversion errors during import.

Fix:
Implemented explicit datetime.strptime validation.

---

### Case 3

AI Output:
Dependency versions causing deployment conflicts.

Issue Found:
Render build failed because of incompatible Google AI packages.

Fix:
Removed conflicting dependencies and redeployed successfully.

---

## Human Validation Process

All AI-generated code was:

* Reviewed manually
* Tested locally
* Verified through API testing
* Validated before deployment
