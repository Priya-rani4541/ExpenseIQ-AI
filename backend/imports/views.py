from rest_framework.views import APIView
from rest_framework.response import Response

from services.csv_import_service import read_csv


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

        return Response(
            {
                "total_rows": len(rows),
                "sample_data": rows[:3]
            }
        )