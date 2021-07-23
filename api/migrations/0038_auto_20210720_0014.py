# Generated by Django 3.2.5 on 2021-07-19 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_contributor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='author',
        ),
        migrations.RemoveField(
            model_name='material',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='material',
            name='description',
        ),
        migrations.RemoveField(
            model_name='material',
            name='posted_by',
        ),
        migrations.AddField(
            model_name='material',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='materials', to='api.college'),
        ),
        migrations.AddField(
            model_name='material',
            name='contributor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='materials', to='api.contributor'),
        ),
        migrations.AlterField(
            model_name='material',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='materials', to='api.subject'),
        ),
    ]