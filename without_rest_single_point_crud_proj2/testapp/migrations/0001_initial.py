# Generated by Django 3.2 on 2022-01-05 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('gf', models.CharField(max_length=10)),
                ('bf', models.CharField(max_length=10)),
            ],
        ),
    ]