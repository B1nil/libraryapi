# Generated by Django 5.0.7 on 2024-07-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('language', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image')),
            ],
        ),
    ]