# Generated by Django 4.0.1 on 2022-03-16 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_post_readmore_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.TextField(default='', max_length=200),
        ),
    ]
