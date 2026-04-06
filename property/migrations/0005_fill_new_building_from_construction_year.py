from django.db import migrations


def fill_new_building_from_construction_year(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        year = flat.construction_year
        if year is None:
            flat.new_building = None
        elif year >= 2015:
            flat.new_building = True
        else:
            flat.new_building = False
        flat.save(update_fields=['new_building'])


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [('property', '0004_flat_new_building')]
    operations = [
        migrations.RunPython(
            fill_new_building_from_construction_year, noop_reverse
        )
    ]
