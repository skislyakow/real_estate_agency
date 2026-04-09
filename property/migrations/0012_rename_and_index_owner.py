import phonenumber_field.modelfields
from django.db import migrations, models


def reverse_rename_and_index_owner(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [('property', '0011_fill_owners')]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='owner',
            new_name='owner_deprecated',
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(
                'ФИО собственника', max_length=200, db_index=True
            ),
        ),
        migrations.AlterField(
            model_name='owner',
            name='pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(
                'Нормализованный телефон',
                region='RU',
                blank=True,
                db_index=True
            ),
        )
    ]
