# Generated by Django 5.2.1 on 2025-06-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_studentprofile_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='staff_photos/'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='student_photos/'),
        ),
    ]
