# Generated by Django 2.1.2 on 2019-04-30 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [
        ("web", "0001_initial"),
        ("web", "0002_auto_20190325_2127"),
        ("web", "0003_notifs"),
        ("web", "0004_auto_20190423_2012"),
        ("web", "0005_schedule"),
        ("web", "0006_auto_20190428_0818"),
        ("web", "0007_auto_20190428_0859"),
        ("web", "0008_auto_20190428_0901"),
        ("web", "0009_auto_20190428_0907"),
    ]

    initial = True

    dependencies = [
        ("auth", "0009_alter_user_last_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Jids",
            fields=[
                (
                    "jid",
                    models.CharField(
                        db_index=True, max_length=255, primary_key=True, serialize=False
                    ),
                ),
                ("load", models.TextField()),
            ],
            options={"db_table": "jids", "managed": False},
        ),
        migrations.CreateModel(
            name="SaltEvents",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("tag", models.CharField(db_index=True, max_length=255)),
                ("data", models.TextField()),
                ("alter_time", models.DateTimeField()),
                ("master_id", models.CharField(max_length=255)),
            ],
            options={"db_table": "salt_events", "managed": False},
        ),
        migrations.CreateModel(
            name="SaltReturns",
            fields=[
                ("fun", models.CharField(db_index=True, max_length=50)),
                ("jid", models.CharField(db_index=True, max_length=255)),
                ("return_field", models.TextField(db_column="return")),
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("success", models.CharField(max_length=10)),
                ("full_ret", models.TextField()),
                ("alter_time", models.DateTimeField()),
            ],
            options={"db_table": "salt_returns", "managed": False},
        ),
        migrations.CreateModel(
            name="Functions",
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
                ("name", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
            options={"db_table": "salt_functions"},
        ),
        migrations.CreateModel(
            name="Keys",
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
                ("minion_id", models.CharField(max_length=255)),
                ("pub", models.TextField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("accepted", "accepted"),
                            ("rejected", "rejected"),
                            ("denied", "denied"),
                            ("unaccepted", "unaccepted"),
                        ],
                        max_length=64,
                    ),
                ),
            ],
            options={"db_table": "salt_keys"},
        ),
        migrations.CreateModel(
            name="Minions",
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
                ("minion_id", models.CharField(max_length=128)),
                ("grain", models.TextField()),
                ("pillar", models.TextField()),
            ],
            options={"db_table": "salt_minions"},
        ),
        migrations.CreateModel(
            name="MinionsCustomFields",
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
                ("name", models.CharField(max_length=255)),
                ("value", models.TextField()),
                ("function", models.CharField(max_length=255)),
                (
                    "minion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.Minions"
                    ),
                ),
            ],
            options={"db_table": "minions_custom_fields"},
        ),
        migrations.CreateModel(
            name="Schedule",
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
                ("name", models.CharField(max_length=255)),
                ("job", models.TextField()),
                (
                    "minion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.Minions"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserSettings",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="user_settings",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("token", models.CharField(max_length=40)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("notifs_created", models.BooleanField(default=False)),
                ("notifs_published", models.BooleanField(default=False)),
                ("notifs_returned", models.BooleanField(default=True)),
                ("notifs_event", models.BooleanField(default=False)),
                ("salt_permissions", models.TextField()),
            ],
        ),
        migrations.AlterModelTable(name="usersettings", table="user_settings"),
    ]
