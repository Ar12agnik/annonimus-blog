# Generated by Django 5.0.1 on 2024-01-18 16:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_posts_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='pub_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
