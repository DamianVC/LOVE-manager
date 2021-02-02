# Generated by Django 2.1.10 on 2019-07-17 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_auto_20190528_1552"),
    ]

    operations = [
        migrations.CreateModel(
            name="GlobalPermissions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "permissions": (
                    ("Commands.execute_commands", "Execute Commands"),
                    (
                        "ScriptQueue.run_scripts",
                        "Run and Requeue scripts in ScriptQueues",
                    ),
                ),
                "managed": False,
            },
        ),
    ]
