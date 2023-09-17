from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0015_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_image',
            field=models.ImageField(blank=True, default='static/images/default.png', null=True, upload_to='static/images/', verbose_name='property_image'),
        ),
    ]