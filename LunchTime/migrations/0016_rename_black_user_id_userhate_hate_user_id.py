# Generated by Django 4.1.3 on 2023-05-22 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LunchTime', '0015_rename_userblacklist_userhate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userhate',
            old_name='black_user_id',
            new_name='hate_user_id',
        ),
    ]
