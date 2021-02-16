# Generated by Django 2.2.13 on 2021-02-15 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0098_projectattributefile_archived_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdeadline',
            name='confirmed',
        ),
        migrations.AddField(
            model_name='deadline',
            name='confirmation_attribute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='confirms_deadline', to='projects.Attribute', verbose_name='attribute for confirmation'),
        ),
    ]
