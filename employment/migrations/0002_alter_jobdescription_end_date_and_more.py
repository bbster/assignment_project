# Generated by Django 4.2.6 on 2023-10-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdescription',
            name='end_date',
            field=models.DateField(help_text='채용마감일'),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='start_date',
            field=models.DateField(help_text='채용시작일'),
        ),
    ]
