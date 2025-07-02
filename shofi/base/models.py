from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

from django_ckeditor_5.fields import CKEditor5Field



# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="p.jpg")
    body = CKEditor5Field('Body', config_name='default', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, blank=True)
    slug = models.SlugField(null=True, blank=True) 
    
    def __str__(self):
        return self.headline
    
    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == '':
            slug = slugify(self.headline)
            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)

