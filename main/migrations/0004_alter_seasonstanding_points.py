# Generated by Django 3.2.6 on 2021-12-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211202_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seasonstanding',
            name='points',
            field=models.PositiveIntegerField(default=0, verbose_name='Total points'),
        ),
    ]