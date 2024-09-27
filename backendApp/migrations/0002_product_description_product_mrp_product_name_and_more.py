# Generated by Django 4.1.13 on 2024-09-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='No description available', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='mrp',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='nike shirt', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]