# Generated by Django 2.0.13 on 2020-11-30 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0008_auto_20201130_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='Comment',
        ),
        migrations.AddField(
            model_name='workshop',
            name='Comment',
            field=models.ManyToManyField(to='workshop.Comment'),
        ),
    ]