# Generated by Django 5.1.4 on 2024-12-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0002_alter_experience_expdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(blank=True, help_text='The name of your university (e.g., Harvard University).', max_length=300, null=True, verbose_name='University Name')),
                ('description', models.TextField(blank=True, help_text='A brief description of your role and responsibilities.', max_length=1000, null=True, verbose_name='Experience Summary')),
                ('degree', models.CharField(blank=True, help_text='The degree of your education (e.g., Bsc, Msc).', max_length=100, null=True, verbose_name='Education Degree')),
                ('start_date', models.DateField(help_text='The date when you started this job.', verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, help_text='The date when you left this job. Leave blank if currently working.', null=True, verbose_name='End Date')),
                ('is_current', models.BooleanField(default=False, help_text='Check if you are currently working in this position.', verbose_name='Currently Working')),
            ],
        ),
    ]
