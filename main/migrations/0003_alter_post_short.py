# Generated by Django 3.2.9 on 2021-11-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_short'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='short',
            field=models.TextField(max_length=106),
        ),
    ]
