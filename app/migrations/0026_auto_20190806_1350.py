# Generated by Django 2.1.7 on 2019-08-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app", "0025_auto_20190805_1551")]

    operations = [
        migrations.RemoveField(model_name="gameplayer", name="user"),
        migrations.AlterField(
            model_name="gameplayer",
            name="id",
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
