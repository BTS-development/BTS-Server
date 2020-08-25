from django.db import models

# Create your models here.
class Temperature(models.Model):
    value = models.FloatField()
    owner = models.ForeignKey("user.User", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
