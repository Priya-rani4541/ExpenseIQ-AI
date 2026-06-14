from django.db import models

# Create your models here.


class ImportLog(models.Model):
    filename = models.CharField(max_length=255)

    total_rows = models.IntegerField(default=0)

    valid_rows = models.IntegerField(default=0)

    invalid_rows = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename