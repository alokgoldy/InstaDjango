# Generated by Django 2.0.2 on 2018-03-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0003_user_profilepic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseurl', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
                ('owner', models.CharField(max_length=20)),
                ('likes', models.IntegerField()),
                ('caption', models.CharField(default='', max_length=140)),
                ('tags', models.IntegerField(default=0)),
                ('main_colour', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
