# Generated by Django 5.0.6 on 2024-07-10 05:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apidataupload', '0008_remove_leave_leave_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leave_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apidataupload.leavetype'),
        ),
    ]