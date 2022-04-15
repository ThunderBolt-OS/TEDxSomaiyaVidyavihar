from django.db import models
from email.policy import default
from ckeditor.fields import RichTextField

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200, default='')
    author = models.TextField(max_length=200, default='')
    slug = models.SlugField(max_length=200, unique=True, default="1")
    body = RichTextField(blank = True, null = True)
    readmore_body = models.TextField(max_length=200, default='')
    image = models.ImageField(upload_to='blogs/images/')
    image_banner = models.ImageField(upload_to='blogs/images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return str(self.created_at) + '\n' + self.title