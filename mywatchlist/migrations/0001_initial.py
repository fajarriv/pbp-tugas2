# Generated by Django 4.1 on 2022-09-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_watched', models.CharField(max_length=3)),
                ('movie_title', models.TextField()),
                ('release_date', models.TextField()),
                ('rating', models.IntegerField()),
                ('review', models.TextField()),
            ],
        ),
    ]
