# Generated by Django 4.2.2 on 2023-10-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_staff_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Working',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Working')),
            ],
        ),
    ]
