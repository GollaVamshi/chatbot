# Generated by Django 5.1.6 on 2025-02-28 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdp', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('content', models.TextField()),
            ],
            options={
                'unique_together': {('cdp', 'url')},
            },
        ),
    ]
