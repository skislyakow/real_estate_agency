from django.db import migrations, transaction
from django.db.models import Q

import phonenumbers


def fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.filter(
        Q(owner_pure_phone__isnull=True) | Q(owner_pure_phone='')
    ).exclude(owners_phonenumber__isnull=True)
    for flat in flats.iterator():
        raw = (flat.owners_phonenumber or '').strip()
        if not raw:
            continue
        try:
            parsed = phonenumbers.parse(raw, region='RU')
            if not phonenumbers.is_valid_number(parsed):
                continue
            pure_number = phonenumbers.format_number(
                parsed, phonenumbers.PhoneNumberFormat.E164
            )
            flat.owner_pure_phone = pure_number
            try:
                with transaction.atomic():
                    flat.save(update_fields=['owner_pure_phone'])
            except Exception as e:
                print(f"Ошибка в объекте {flat.id}: {e}")
        except phonenumbers.NumberParseException:
            continue


def reverse_fill_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(owner_pure_phone__isnull=False).update(
        owner_pure_phone=''
    )


class Migration(migrations.Migration):
    dependencies = [('property', '0008_flat_owner_pure_phone')]
    operations = [migrations.RunPython(
        fill_owner_pure_phone, reverse_fill_owner_pure_phone
    )]
