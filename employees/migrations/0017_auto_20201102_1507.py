# Generated by Django 3.1.2 on 2020-11-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0016_auto_20201102_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='task_description',
            field=models.DateField(),
        ),
    ]
