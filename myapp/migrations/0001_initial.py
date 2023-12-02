# Generated by Django 4.2.3 on 2023-11-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('tags', models.TextField()),
                ('img', models.FileField(upload_to='pic/%y/')),
            ],
        ),
    ]
