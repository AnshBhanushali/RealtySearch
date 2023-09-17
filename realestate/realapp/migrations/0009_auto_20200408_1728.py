from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0008_auto_20200408_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]