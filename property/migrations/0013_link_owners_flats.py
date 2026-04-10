from django.db import migrations


def link_owners_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all().iterator():
        if flat.owner_deprecated:
            owner = Owner.objects.filter(name=flat.owner_deprecated).first()
            if owner:
                owner.flats.add(flat)


def reverse_link_owners_flats(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all().iterator():
        owner.flats.clear()


class Migration(migrations.Migration):
    dependencies = [('property', '0012_rename_and_index_owner')]

    operations = [migrations.RunPython(
        link_owners_flats, reverse_link_owners_flats
        )]
