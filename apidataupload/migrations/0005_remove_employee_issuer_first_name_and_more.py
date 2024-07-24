# Generated by Django 5.0.6 on 2024-07-10 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apidataupload', '0004_alter_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='issuer_first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='issuer_last_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='issuer_middle_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='leave_issuer_id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='team_manager_id',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]