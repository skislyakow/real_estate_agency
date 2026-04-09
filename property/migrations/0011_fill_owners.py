from django.db import migrations


def fill_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(
            name=flat.owner,
            defaults={
                'owners_phonenumber': flat.owners_phonenumber,
                'pure_phone': flat.owner_pure_phone,
            }
    )

def reverse_fill_owners(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Owner.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [('property', '0010_owner')]
    operations = [migrations.RunPython(fill_owners, reverse_fill_owners)]
