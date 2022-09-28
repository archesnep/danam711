# Generated by Django 2.2.24 on 2022-03-23 03:47

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("models", "8042_1_geometry_table_expand_geoms"),
    ]

    operations = [
        migrations.CreateModel(
            name="SpatialView",
            fields=[
                ("spatialviewid", models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ("schema", models.TextField(default="public")),
                (
                    "slug",
                    models.TextField(
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="nomatch",
                                message="Slug must contain only letters, numbers and hyphens, but not begin with a number.",
                                regex="^[a-zA-Z_]([a-zA-Z0-9_]+)$",
                            )
                        ],
                    ),
                ),
                ("description", models.TextField(default="arches spatial view")),
                ("ismixedgeometrytypes", models.BooleanField(default=False)),
                ("attributenodes", django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_column="attributenodes", null=True)),
                ("isactive", models.BooleanField(default=True)),
                (
                    "geometrynodeid",
                    models.ForeignKey(db_column="geometrynodeid", on_delete=django.db.models.deletion.CASCADE, to="models.Node"),
                ),
            ],
            options={
                "db_table": "spatial_views",
                "managed": True,
            },
        ),
    ]
