# Generated by Django 3.2.9 on 2023-11-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger', '0003_auto_20231119_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='BurgerMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('alt_text', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
