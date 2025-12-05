from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_alter_address_id_alter_letting_address_and_more'),
        ('lettings', '0002_transfer_data'),
        ('profiles', '0002_transfer_data'),
    ]

    operations = [
        migrations.DeleteModel(name='Letting'),
        migrations.DeleteModel(name='Address'),
        migrations.DeleteModel(name='Profile'),
    ]