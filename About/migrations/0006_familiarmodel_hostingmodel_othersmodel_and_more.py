# Generated by Django 5.1.4 on 2024-12-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0005_webskillsmodel_skillsmodel_skilllogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(blank=True, max_length=100, null=True)),
                ('skillLogo', models.ImageField(blank=True, null=True, upload_to='logo/photos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HostingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(blank=True, max_length=100, null=True)),
                ('skillLogo', models.ImageField(blank=True, null=True, upload_to='logo/photos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OthersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(blank=True, max_length=100, null=True)),
                ('skillLogo', models.ImageField(blank=True, null=True, upload_to='logo/photos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='WebSkillsModel',
            new_name='ComfortableModel',
        ),
        migrations.RenameModel(
            old_name='SkillsModel',
            new_name='ExpertiseModel',
        ),
    ]