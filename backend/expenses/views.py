from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Expense


class ExpenseListView(APIView):

    def get(self, request):

        expenses = Expense.objects.all()

        data = []

        for expense in expenses:

            data.append({
                "id": expense.id,
                "date": expense.date,
                "description": expense.description,
                "paid_by": expense.paid_by,
                "amount": str(expense.amount),
                "currency": expense.currency
            })

        return Response(data)
