# Generated by Django 2.1.15 on 2020-11-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0026_auto_20201110_1711'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Departments',
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
