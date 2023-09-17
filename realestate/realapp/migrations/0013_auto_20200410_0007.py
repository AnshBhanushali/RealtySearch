from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0012_auto_20200410_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_image',
            field=models.ImageField(blank=True, null=True, upload_to='realestate/static/images/', verbose_name='property_image'),
        ),
    ]