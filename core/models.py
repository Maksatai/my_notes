from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Notes(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    description=models.TextField()
    image = models.ImageField(upload_to='images',null=True,blank=True)
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.description


    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['description']