from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0010_auto_20200408_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='property_image'),
        ),
    ]