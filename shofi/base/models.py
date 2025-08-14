# from django.db import models
# from django.contrib.auth.models import User

# from django.utils.text import slugify

# from django_ckeditor_5.fields import CKEditor5Field



# # Create your models here.

# class Tags(models.Model):
#     name = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.name
    

# class Post(models.Model):
#     headline = models.CharField(max_length=200)
#     sub_headline = models.CharField(max_length=200, null=True, blank=True)
#     thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="p.jpg")
#     body = CKEditor5Field('Body', config_name='default', null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     activate = models.BooleanField(default=False)
#     featured = models.BooleanField(default=False)
#     tags = models.ManyToManyField(Tags, blank=True)
#     slug = models.SlugField(null=True, blank=True) 
    
#     def __str__(self):
#         return self.headline
    
#     def save(self, *args, **kwargs):
#         if self.slug is None or self.slug == '':
#             slug = slugify(self.headline)
#             has_slug = Post.objects.filter(slug=slug).exists()
#             count = 1
#             while has_slug:
#                 count += 1
#                 slug = slugify(self.headline) + '-' + str(count)
#                 has_slug = Post.objects.filter(slug=slug).exists()
#             self.slug = slug
#         super().save(*args, **kwargs)

# base/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Tags(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField(default=0)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.name

class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    badge = models.CharField(max_length=50, blank=True)
    popular = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.name

class Feature(models.Model):
    plan = models.ForeignKey(PricingPlan, related_name='features', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    included = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='clients/')
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.TextField()
    order = models.IntegerField(default=0)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return f"Testimonial by {self.client.name}"

class ContactInfo(models.Model):
    location = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    def __str__(self):
        return "Contact Information"

class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    class Meta:
        ordering = ['order']
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