# Generated by Django 4.1.3 on 2023-05-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LunchTime', '0004_post_postcomment_postlove_postpicture_postsave'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='create_time',
            field=models.DateField(auto_now=True),
        ),
    ]
