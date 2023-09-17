from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0017_auto_20200412_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(default='Indore', max_length=30)),
                ('state', models.CharField(default='Madhya Pradesh', max_length=30)),
                ('country', models.CharField(default='India', max_length=30)),
            ],
        ),
    ]