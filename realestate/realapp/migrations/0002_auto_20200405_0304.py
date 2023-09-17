from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realestate.Person'),
        ),
    ]