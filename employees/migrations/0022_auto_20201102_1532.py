# Generated by Django 3.1.2 on 2020-11-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0021_auto_20201102_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='phone_num2',
        ),
        migrations.AddField(
            model_name='employee',
            name='task_details',
            field=models.TextField(default='Not Defined', null=True),
        ),
    ]