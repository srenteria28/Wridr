from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.CharField(max_length=250)
    body_text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']    