# Generated by Django 5.0.6 on 2024-07-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apidataupload', '0005_remove_employee_issuer_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='issuer_first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='leave',
            name='issuer_last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='leave',
            name='issuer_middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='leave_issuer_id',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]