# Generated by Django 5.1.6 on 2025-03-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20250306_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
