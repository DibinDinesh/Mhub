# Generated by Django 5.0.3 on 2024-05-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('picture', models.ImageField(null=True, upload_to='image')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('run_time', models.PositiveIntegerField()),
                ('language', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('producer', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
