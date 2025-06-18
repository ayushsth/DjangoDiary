from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DiaryEntry(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M')