from django.conf import settings
from django.db import models

#
# class Token(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
#     token = models.CharField(max_length=500)
#     auth_number = models.CharField(max_length=6)
#     expired_at = models.DateTimeField()
#
#     def __str__(self):
#         return self.token


class AccountUser(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["username"],
                name="unique_username",
            )
        ]

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
