from django.db import models

# Create your models here.
class Temperature(models.Model):
    value = models.FloatField()
    owner = models.ManyToManyField("user.User", through="TemperatureUser")
    created_at = models.DateField(auto_now_add=True)


class TemperatureUser(models.Model):
    Temperature = models.ForeignKey("Temperature", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
