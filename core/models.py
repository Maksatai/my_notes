from django.db import models


class Notes(models.Model):
    description=models.TextField()
    image = models.ImageField(upload_to='images',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.description

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['description']