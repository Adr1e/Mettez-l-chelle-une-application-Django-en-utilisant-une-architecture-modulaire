from django.db import migrations


def transfer_profiles_data(apps, schema_editor):
    """Transfère les données des anciens profils vers les nouveaux."""
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            id=old_profile.id,
            user=old_profile.user,
            favorite_city=old_profile.favorite_city,
        )


def reverse_transfer(apps, schema_editor):
    """Permet de revenir en arrière si nécessaire."""
    NewProfile = apps.get_model('profiles', 'Profile')
    NewProfile.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0002_alter_address_id_alter_letting_address_and_more'),
    ]

    operations = [
        migrations.RunPython(transfer_profiles_data, reverse_transfer),
    ]