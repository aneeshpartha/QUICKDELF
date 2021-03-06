# Generated by Django 2.0.2 on 2018-04-27 03:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOB', models.DateField(blank=True)),
                ('gender', models.CharField(max_length=6)),
                ('Cardnumber', models.BigIntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete='No', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
