from django.db import models


# Create your models here.
class EmailDetail(models.Model):
    email = models.EmailField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f"{self.email}"

