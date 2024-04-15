# Generated by Django 5.0.4 on 2024-04-13 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=255)),
                ('technology', models.CharField(choices=[('Python', 'Python'), ('React', 'React'), ('Devops', 'Devops')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
