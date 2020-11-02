# Generated by Django 3.1.2 on 2020-11-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20201102_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='task_urgency',
            field=models.CharField(choices=[('H', 'High'), ('N', 'Normal'), ('L', 'Low')], default='L', max_length=1),
        ),
    ]