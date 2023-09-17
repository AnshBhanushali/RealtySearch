from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0026_auto_20200414_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='city',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='realestate.City'),
        ),
    ]