# Generated by Django 5.0.1 on 2024-01-29 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
