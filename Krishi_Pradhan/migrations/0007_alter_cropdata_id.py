# Generated by Django 3.2.4 on 2021-08-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Krishi_Pradhan', '0006_cropdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropdata',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
