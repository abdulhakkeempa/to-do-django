# Generated by Django 4.0.2 on 2022-05-30 18:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='toDoList',
            fields=[
                ('task', models.CharField(max_length=100)),
                ('remarks', models.TextField(blank=True, max_length=100, null=True)),
                ('timeAdded', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]