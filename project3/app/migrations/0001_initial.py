# Generated by Django 4.2.11 on 2024-04-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=50)),
                ('pno', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('add', models.CharField(max_length=50)),
            ],
        ),
    ]
