class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0014_delete_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_purchase', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Agent')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Client')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.Property')),
            ],
        ),
    ]