# Generated by Django 2.2.13 on 2021-03-19 20:17
from arches.app.models.fields.i18n import I18n_JSONField
from django.db import migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ("models", "7809_i18n_concept_datatype"),
    ]

    sql = """
        UPDATE public.cards_x_nodes_x_widgets
        SET config =
        jsonb_set(
            jsonb_set(
                jsonb_set(config,
                '{{suffix}}', json_build_object('{0}', config->>'suffix')::jsonb, true),
            '{{prefix}}', json_build_object('{0}', config->>'prefix')::jsonb, true),
        '{{placeholder}}', json_build_object('{0}', config->>'placeholder')::jsonb, true
        ) ||
        '{{"i18n_properties": ["placeholder", "prefix", "suffix"]}}'
        WHERE nodeid in (SELECT nodeid FROM nodes WHERE datatype = 'number');

        UPDATE public.widgets
        SET defaultconfig = defaultconfig ||
        '{{"i18n_properties": ["placeholder", "prefix", "suffix"]}}'
        WHERE datatype = 'number';

    """.format(
        settings.LANGUAGE_CODE
    )

    reverse_sql = """
        UPDATE public.cards_x_nodes_x_widgets
        set config = config - 'i18n_properties' ||
        json_build_object('placeholder', jsonb_extract_path(config, 'placeholder', '{0}'))::jsonb ||
        json_build_object('prefix', jsonb_extract_path(config, 'prefix', '{0}'))::jsonb ||
        json_build_object('suffix', jsonb_extract_path(config, 'suffix', '{0}'))::jsonb
        WHERE nodeid in (SELECT nodeid FROM nodes WHERE datatype = 'number');

        UPDATE public.widgets
        SET defaultconfig = defaultconfig - 'i18n_properties'
        WHERE datatype = 'number';
    """.format(
        settings.LANGUAGE_CODE
    )

    operations = [
        migrations.RunSQL(sql, reverse_sql),
        migrations.AlterField(
            model_name="cardxnodexwidget",
            name="config",
            field=I18n_JSONField(blank=True, null=True),
        ),
    ]
