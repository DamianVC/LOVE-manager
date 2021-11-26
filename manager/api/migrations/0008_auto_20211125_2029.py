# Generated by Django 3.1.13 on 2021-11-25 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0007_emergencycontact"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="globalpermissions",
            options={
                "managed": False,
                "permissions": (
                    ("command.execute_command", "Execute Commands"),
                    ("command.run_script", "Run and Requeue scripts in ScriptQueues"),
                    ("authlist.administrator", "Access and resolve AuthList requests"),
                ),
            },
        ),
        migrations.CreateModel(
            name="CSCAuthorizationRequest",
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
                ("cscs_to_change", models.TextField()),
                ("authorized_users", models.TextField(blank=True)),
                ("unauthorized_cscs", models.TextField(blank=True)),
                ("requested_by", models.CharField(max_length=50)),
                (
                    "requested_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Requested at"
                    ),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Restriction duration (seconds)",
                    ),
                ),
                ("message", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Authorized", "Authorized"),
                            ("Denied", "Denied"),
                        ],
                        default="Pending",
                        max_length=10,
                    ),
                ),
                (
                    "resolved_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Resolved at"
                    ),
                ),
                (
                    "resolved_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Resolved by",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
            ],
            options={
                "ordering": [
                    django.db.models.expressions.OrderBy(
                        django.db.models.expressions.F("resolved_at"),
                        descending=True,
                        nulls_last=True,
                    ),
                    "-requested_at",
                ],
            },
        ),
    ]
