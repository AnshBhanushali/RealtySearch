from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0003_address_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]