# Generated by Django 4.2.1 on 2023-07-19 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=110)),
                ('phone_number', models.CharField(max_length=25)),
                ('car_model', models.CharField(max_length=50)),
                ('car_number', models.CharField(max_length=50)),
                ('passport', models.CharField(max_length=50)),
                ('patent', models.CharField(max_length=50)),
                ('busy', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('trips', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.trip')),
            ],
        ),
    ]