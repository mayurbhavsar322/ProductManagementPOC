# Generated by Django 3.2.8 on 2021-10-28 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(blank=True, upload_to='my_picture')),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
