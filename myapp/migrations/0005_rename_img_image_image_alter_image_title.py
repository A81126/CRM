# Generated by Django 4.2.3 on 2023-11-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_image_delete_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='img',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
