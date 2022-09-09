# Generated by Django 4.1 on 2022-09-08 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('mobile', models.PositiveIntegerField(null=True)),
                ('address', models.TextField(max_length=50)),
                ('designation', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
            ],
        ),
    ]
