# Generated by Django 4.1.3 on 2022-12-14 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=15)),
                ('input1', models.FloatField(default=0)),
                ('input2', models.FloatField(default=0)),
                ('result', models.FloatField()),
            ],
        ),
    ]
