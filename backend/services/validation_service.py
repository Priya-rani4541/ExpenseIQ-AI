def validate_expense_row(row):

    errors = []

    # Date Validation
    if not row.get("date"):
        errors.append("Date is required")

    # Description Validation
    if not row.get("description"):
        errors.append("Description is required")

    # Paid By Validation
    if not row.get("paid_by"):
        errors.append("Paid By is required")

    # Currency Validation
    if not row.get("currency"):
        errors.append("Currency is required")

    # Amount Validation
    amount = str(
        row.get("amount", "")
    ).replace(",", "").strip()

    if amount == "":
        errors.append("Amount is required")

    else:
        try:

            amount_value = float(amount)

            if amount_value <= 0:
                errors.append(
                    "Amount must be greater than zero"
                )

        except ValueError:

            errors.append(
                "Invalid amount format"
            )

    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }