# Generated by Django 4.1.3 on 2022-11-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_moshinaa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moshinaa',
            name='rasm',
            field=models.TextField(max_length=31),
        ),
    ]
