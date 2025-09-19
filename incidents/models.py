

# Create your models here.
# incidents/models.py
from django.db import models
from django.contrib.auth.models import User

class SafetyIncident(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    reported_date = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
