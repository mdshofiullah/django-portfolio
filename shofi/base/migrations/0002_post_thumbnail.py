# Generated by Django 4.1.4 on 2022-12-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='p.jpg', null=True, upload_to='images'),
        ),
    ]