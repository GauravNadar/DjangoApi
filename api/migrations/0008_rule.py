# Generated by Django 3.0.6 on 2020-05-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_to', models.CharField(max_length=200)),
                ('offence', models.TextField()),
                ('penalty', models.CharField(max_length=200)),
                ('section', models.TextField()),
            ],
        ),
    ]
