# Generated by Django 2.0.4 on 2018-04-28 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_delete_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('itemdescription', models.CharField(max_length=200)),
                ('itemphoto', models.CharField(max_length=200)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.hotels')),
            ],
        ),
    ]
