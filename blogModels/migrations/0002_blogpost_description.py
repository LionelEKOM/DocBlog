# Generated by Django 4.2.11 on 2024-05-14 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogModels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
