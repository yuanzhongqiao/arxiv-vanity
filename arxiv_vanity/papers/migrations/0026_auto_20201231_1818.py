# Generated by Django 2.2.13 on 2020-12-31 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0025_auto_20200418_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='render',
            name='state',
            field=models.CharField(choices=[('unstarted', 'Unstarted'), ('running', 'Running'), ('success', 'Success'), ('failure', 'Failure')], db_index=True, default='unstarted', max_length=20),
        ),
    ]