# Generated by Django 5.0.6 on 2024-07-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_is_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskDescription',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskTitle',
            field=models.CharField(max_length=20),
        ),
    ]
