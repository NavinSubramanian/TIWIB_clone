# Generated by Django 4.2.2 on 2023-06-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TWIB1', '0002_content_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='type',
            field=models.CharField(default='men', max_length=200),
        ),
        migrations.AddField(
            model_name='webpage',
            name='type',
            field=models.CharField(default='men', max_length=200),
        ),
    ]
