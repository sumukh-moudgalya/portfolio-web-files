# Generated by Django 3.2.6 on 2021-08-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('short_desc', models.TextField()),
                ('long_desc', models.TextField()),
                ('report_link', models.TextField()),
                ('sem', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='media')),
                ('rank', models.PositiveIntegerField()),
                ('google_drive_link', models.TextField()),
            ],
        ),
    ]
