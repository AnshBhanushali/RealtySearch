from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0021_auto_20200414_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('zipcode_id', models.AutoField(primary_key=True, serialize=False)),
                ('zipcode', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.City')),
            ],
        ),
    ]