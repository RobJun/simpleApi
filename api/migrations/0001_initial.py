# Generated by Django 4.0.5 on 2022-06-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('userId', models.BigIntegerField()),
                ('title', models.TextField()),
                ('body', models.TextField()),
            ],
        ),
    ]
