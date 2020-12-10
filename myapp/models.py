from django.db import models

# Create your models here.
class PurchaseModel(models.Model):

    purchaser_name = models.CharField(max_length=120)
    quantity = models.IntegerField(default=0)


class PurchaseStatusModel(models.Model):
    status_choices = (
        ("open", "Open"),
        ("verified", "Verified"),
        ("dispatched", "Dispatched"),
        ("delivered", "Delivered"),
    )

    purchase = models.ForeignKey(PurchaseModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=status_choices)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)