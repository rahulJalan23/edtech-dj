# Generated by Django 3.2.5 on 2021-07-19 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_alter_subject_unique_together'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Portion',
        ),
    ]