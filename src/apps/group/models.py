from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey("user.User",on_delete=models.CASCADE)
    code = models.CharField(max_length=255,unique=True)
    members = models.ManyToManyField("user.User",through="LinkedUserGroup")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



class LinkedUserGroup(models.Model):
    group = models.ForeignKey("Group",on_delete=models.CASCADE)
    member = models.ForeignKey("user.User",on_delete=models.CASCADE)
    joined_at = models.DateField(auto_now_add=True)


