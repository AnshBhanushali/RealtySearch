from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0006_layout'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Layout',
        ),
        migrations.AddField(
            model_name='property',
            name='property_image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='prop_img'),
        ),
        migrations.AlterField(
            model_name='property',
            name='date_of_entry',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]