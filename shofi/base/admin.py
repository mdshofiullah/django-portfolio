# from django.contrib import admin
# from .models import Post, Tags
# # Register your models here.

# admin.site.register(Post)
# admin.site.register(Tags)

from django.contrib import admin
from .models import Post, Tags, Skill, PricingPlan, Feature, Client, Testimonial, ContactInfo, SocialLink, Service

admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Skill)
admin.site.register(PricingPlan)
admin.site.register(Feature)
admin.site.register(Client)
admin.site.register(Testimonial)
admin.site.register(ContactInfo)
admin.site.register(SocialLink)
admin.site.register(Service)