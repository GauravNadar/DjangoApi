# Generated by Django 3.0.3 on 2020-05-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='pic2',
            field=models.BinaryField(blank=True),
        ),
    ]
