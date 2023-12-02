from django.db import models

# Create your models here.
class Image(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(unique=True)
    tags=models.TextField()
    image=models.ImageField(upload_to='img/%y')
    def __str__(self):
        return self.title
    class Meta :
        ordering=('-id',)
    

