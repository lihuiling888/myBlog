# Generated by Django 3.1.4 on 2021-01-04 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210104_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='created',
            new_name='created_at',
        ),
    ]