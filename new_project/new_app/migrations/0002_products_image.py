# Generated by Django 3.2.16 on 2023-01-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='hfsery', upload_to='gallery'),
            preserve_default=False,
        ),
    ]