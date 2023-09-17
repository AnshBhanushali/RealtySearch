from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0024_address_area_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='area_id',
            new_name='area',
        ),
    ]