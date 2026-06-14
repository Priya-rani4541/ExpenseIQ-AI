from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ImportLog
from expenses.models import Expense

from services.csv_import_service import read_csv
from services.validation_service import validate_expense_row

from datetime import datetime


class CSVUploadView(APIView):

    def post(self, request):

        csv_file = request.FILES.get("file")

        if not csv_file:
            return Response(
                {
                    "error": "No file uploaded"
                },
                status=400
            )

        rows = read_csv(csv_file)

        print("FIRST ROW:", rows[0])

        import_log = ImportLog.objects.create(
            filename=csv_file.name,
            total_rows=len(rows),
            valid_rows=0,
            invalid_rows=0,
            status="PROCESSING"
        )

        success_count = 0
        failed_count = 0

        for row in rows:

            print("ROW:", row)

            validation = validate_expense_row(row)

            print("VALIDATION:", validation)

            if not validation["is_valid"]:

                failed_count += 1

                continue

            try:

                date_value = str(
                    row.get("date", "")
                ).strip()

                try:

                    expense_date = datetime.strptime(
                        date_value,
                        "%d-%m-%Y"
                    ).date()

                except ValueError:

                    expense_date = datetime.strptime(
                        date_value,
                        "%b-%d"
                    ).replace(year=2026).date()

                amount_value = str(
                    row.get("amount", "0")
                ).replace(",", "")

                Expense.objects.create(
                    date=expense_date,
                    description=str(
                        row.get("description", "")
                    ),

                    paid_by=str(
                        row.get("paid_by", "")
                    ),

                    amount=amount_value,

                    currency=str(
                        row.get("currency", "INR")
                    ),

                    split_type=str(
                        row.get("split_type", "")
                    ),

                    split_with=str(
                        row.get("split_with", "")
                    ),

                    split_details=str(
                        row.get("split_details", "")
                    ),

                    notes=str(
                        row.get("notes", "")
                    ),

                    import_log=import_log
                )

                success_count += 1

            except Exception as e:

                print("ROW ERROR:", e)

                failed_count += 1

        import_log.valid_rows = success_count
        import_log.invalid_rows = failed_count
        import_log.status = "SUCCESS"
        import_log.save()

        return Response(
            {
                "import_id": import_log.id,
                "filename": csv_file.name,
                "total_rows": len(rows),
                "valid_rows": success_count,
                "invalid_rows": failed_count,
                "message": "CSV imported successfully"
            }
        )