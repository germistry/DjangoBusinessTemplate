# Generated by Django 2.2.17 on 2020-12-02 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20201202_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='project_title',
        ),
    ]
