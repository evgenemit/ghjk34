# Generated by Django 4.2.3 on 2023-07-13 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('json_processing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
    ]