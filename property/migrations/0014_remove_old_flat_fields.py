from django.db import migrations


def reverse_remove_old_flat_fields(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [('property', '0013_link_owners_flats')]
    operations = [
        migrations.RemoveField(model_name='flat', name='owner_deprecated'),
        migrations.RemoveField(model_name='flat', name='owner_pure_phone'),
        migrations.RemoveField(model_name='flat', name='owners_phonenumber'),
    ]
