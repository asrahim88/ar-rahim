# Generated by Django 5.1.4 on 2024-12-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0003_skillsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cv/uploads'),
        ),
    ]