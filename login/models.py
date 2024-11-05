from django.db import models
from django.contrib.auth.models import User

class UserActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"
