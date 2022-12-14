# Generated by Django 4.1.1 on 2022-09-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('institution_url', models.URLField(blank=True, null=True)),
                ('institution_city', models.CharField(max_length=100)),
                ('expected_grad_date', models.DateField(blank=True, null=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('certificate_url', models.URLField(blank=True, max_length=300, null=True)),
                ('related_course_work', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Education',
                'ordering': ['-date_completed', '-expected_grad_date'],
            },
        ),
        migrations.CreateModel(
            name='Referees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Referees',
                'ordering': ['-created'],
            },
        ),
    ]
