# Generated by Django 4.1.13 on 2024-09-28 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_shop_session'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop_session',
            old_name='isAdmin',
            new_name='is_superuser',
        ),
    ]