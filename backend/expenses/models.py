from django.db import models
from imports.models import ImportLog


class Expense(models.Model):

    date = models.DateField()

    description = models.TextField()

    paid_by = models.CharField(max_length=100)

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    currency = models.CharField(max_length=10)

    split_type = models.CharField(max_length=50)

    split_with = models.TextField()

    split_details = models.TextField(
        blank=True,
        null=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    import_log = models.ForeignKey(
        ImportLog,
        on_delete=models.CASCADE,
        related_name="expenses"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.description