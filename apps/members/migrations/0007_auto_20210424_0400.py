# Generated by Django 3.1 on 2021-04-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20210424_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='registration_date',
            field=models.DateField(verbose_name='Registration Date'),
        ),
    ]
