# Generated by Django 4.2.4 on 2023-09-11 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customization', '0002_rename_students_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student Detail', 'verbose_name_plural': 'Student Details'},
        ),
    ]
