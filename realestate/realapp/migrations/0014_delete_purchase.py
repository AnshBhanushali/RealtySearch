from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0013_auto_20200410_0007'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]