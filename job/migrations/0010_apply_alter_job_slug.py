# Generated by Django 4.1.2 on 2022-10-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_job_slug_alter_job_image_alter_job_job_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('coverlitter', models.TextField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
