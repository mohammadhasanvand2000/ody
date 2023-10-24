# Generated by Django 4.2.3 on 2023-10-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_alter_medicine_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='drug_interactions',
            field=models.CharField(default=1, help_text='نام دارویی کا بااین دارو تداخل دارد :', max_length=10000, verbose_name='فیلد تداخل دارویی اجباری'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.IntegerField(blank=True, default='1000', null=True),
        ),
    ]