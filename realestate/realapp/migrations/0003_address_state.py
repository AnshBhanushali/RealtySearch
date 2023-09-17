from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0002_auto_20200405_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(default='Madhya Pradesh', max_length=30),
        ),
    ]