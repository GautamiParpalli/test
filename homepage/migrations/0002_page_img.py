# Generated by Django 3.2.3 on 2021-05-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='img',
            field=models.ImageField(default='https://cdn.pixabay.com/photo/2020/07/06/01/33/forest-5375005__340.jpg', upload_to='field'),
        ),
    ]
