# Generated by Django 5.1.4 on 2025-01-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0005_alter_socialinformation_phone_number1'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialinformation',
            name='behance',
            field=models.URLField(blank=True, help_text='Your behance profile link', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='socialinformation',
            name='dribble',
            field=models.URLField(blank=True, help_text='Your dribble profile link', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='socialinformation',
            name='facebook',
            field=models.URLField(blank=True, help_text='Your facebook profile link', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='socialinformation',
            name='instagram',
            field=models.URLField(blank=True, help_text='Your instagram profile link', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='socialinformation',
            name='reddit',
            field=models.URLField(blank=True, help_text='Your reddit profile link', max_length=300, null=True),
        ),
    ]
