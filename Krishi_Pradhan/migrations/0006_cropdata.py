# Generated by Django 3.2.3 on 2021-07-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Krishi_Pradhan', '0005_delete_cropdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='cropdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region1', models.CharField(max_length=255)),
                ('soil1', models.CharField(max_length=255)),
                ('crop1', models.CharField(max_length=255)),
            ],
        ),
    ]
