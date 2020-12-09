# Generated by Django 3.1.3 on 2020-12-08 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_image', models.ImageField(upload_to='')),
                ('processed_image', models.ImageField(upload_to='')),
                ('result', models.CharField(choices=[('Normal', 'Normal'), ('Pneumonia', 'Pneumonia'), ('COVID', 'COVID')], max_length=15)),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=4)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
