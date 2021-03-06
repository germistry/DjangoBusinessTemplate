# Generated by Django 2.2.17 on 2020-12-01 14:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='employees/default.jpg', null=True, upload_to='employees/')),
                ('image_caption', models.CharField(max_length=100)),
                ('about', models.TextField(null=True)),
                ('show_homepage', models.BooleanField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='website.JobTitle')),
            ],
            options={
                'ordering': ['full_name'],
            },
        ),
    ]
