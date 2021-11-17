from django.db import models


class UserInfo(models.Model):
    emormob = models.CharField(max_length=250, primary_key=True, blank=False)
    user_name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.user_name
