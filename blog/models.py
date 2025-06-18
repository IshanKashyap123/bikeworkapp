from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blogs/')
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
