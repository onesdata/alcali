# Generated by Django 2.1.2 on 2019-03-17 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("status", models.CharField(max_length=64)),
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
                (
                    "function",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.Functions"
                    ),
                ),
                (
                    "minion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.Minions"
                    ),
                ),
            ],
            options={"db_table": "minions_custom_fields"},
        ),
    ]
