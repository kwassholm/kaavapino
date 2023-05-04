# Generated by Django 3.2.16 on 2023-04-06 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0151_auto_20230406_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributelock',
            name='fieldset_attribute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attribute_lock_fieldset', to='projects.attribute', verbose_name='fieldset attribute'),
        ),
        migrations.AlterField(
            model_name='attributelock',
            name='fieldset_attribute_index',
            field=models.IntegerField(blank=True, null=True, verbose_name='index'),
        ),
    ]