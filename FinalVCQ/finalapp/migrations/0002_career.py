# Generated by Django 4.0.6 on 2022-08-01 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('corto', models.TextField()),
                ('image', models.TextField()),
                ('state', models.CharField(max_length=1)),
            ],
        ),
    ]
