# Generated by Django 4.0.6 on 2023-02-16 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_tasks_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
