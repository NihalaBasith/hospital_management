# Generated by Django 3.0.1 on 2022-10-12 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
