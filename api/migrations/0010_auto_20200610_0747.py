# Generated by Django 3.0.6 on 2020-06-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='option2',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AddField(
            model_name='questions',
            name='option3',
            field=models.CharField(default='null', max_length=500),
        ),
        migrations.AddField(
            model_name='questions',
            name='option4',
            field=models.CharField(default='null', max_length=500),
        ),
    ]
