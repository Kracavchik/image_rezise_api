# Generated by Django 3.0.7 on 2020-06-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_logic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawimage',
            name='image_path',
            field=models.ImageField(upload_to='source_images', verbose_name='Путь к картинке'),
        ),
    ]