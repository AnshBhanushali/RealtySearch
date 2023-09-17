from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0023_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='area_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realestate.Area'),
        ),
    ]