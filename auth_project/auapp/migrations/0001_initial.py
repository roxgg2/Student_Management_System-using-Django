# Generated by Django 4.2.5 on 2023-10-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentModel',
            fields=[
                ('rno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
