# Generated by Django 2.1.15 on 2020-11-10 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0024_auto_20201110_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('task_details', models.TextField(default='Not Defined', null=True)),
                ('supervisor', models.CharField(choices=[('s', 'Choose'), ('A', 'A'), ('d2', 'B'), ('d3', 'C')], default='s', max_length=10)),
                ('task_urgency', models.CharField(choices=[('L', 'Low'), ('N', 'Normal'), ('H', 'High')], default='L', max_length=1)),
                ('task_completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='supervisor',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='task_completed',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='task_details',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='task_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='task_urgency',
        ),
        migrations.AddField(
            model_name='task',
            name='email_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee'),
        ),
    ]