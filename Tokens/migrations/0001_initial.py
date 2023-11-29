# Generated by Django 4.2.7 on 2023-11-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refresh_token', models.CharField(max_length=255)),
                ('access_token', models.CharField(max_length=255)),
                ('expires_at', models.IntegerField()),
                ('athlete_id', models.IntegerField(unique=True)),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('sex', models.CharField(blank=True, max_length=5, null=True)),
                ('follower_count', models.IntegerField(blank=True, null=True)),
                ('following_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]