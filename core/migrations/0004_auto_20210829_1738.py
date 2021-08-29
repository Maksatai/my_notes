# Generated by Django 3.2.6 on 2021-08-29 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_notes_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]