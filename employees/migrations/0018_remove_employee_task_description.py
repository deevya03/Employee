# Generated by Django 3.1.2 on 2020-11-02 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0017_auto_20201102_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='task_description',
        ),
    ]
