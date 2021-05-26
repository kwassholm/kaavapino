# Generated by Django 2.2.13 on 2021-05-20 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitecontent', '0002_ListViewAttributeColumn'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetFloorArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(unique=True, verbose_name='year')),
                ('target', models.IntegerField(verbose_name='area target')),
            ],
        ),
        migrations.AlterModelOptions(
            name='footerlink',
            options={'ordering': ('index',), 'verbose_name': 'footer link', 'verbose_name_plural': 'footer links'},
        ),
        migrations.AlterModelOptions(
            name='listviewattributecolumn',
            options={'ordering': ('index',), 'verbose_name': 'list view attribute column', 'verbose_name_plural': 'list view attribute columns'},
        ),
    ]