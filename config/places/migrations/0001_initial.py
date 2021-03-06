# Generated by Django 3.2.3 on 2021-05-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('is_pamyatnik', models.BooleanField(default=False)),
                ('image_1', models.ImageField(upload_to='place/')),
                ('image_2', models.ImageField(upload_to='place/')),
                ('image_3', models.ImageField(upload_to='place/')),
                ('text_1', models.TextField()),
                ('text_2', models.TextField()),
                ('text_3', models.TextField()),
            ],
        ),
    ]
