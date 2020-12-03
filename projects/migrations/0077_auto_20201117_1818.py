# Generated by Django 2.2.13 on 2020-11-17 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0076_deadline_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPhaseDeadlineSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(default=0, verbose_name='index')),
            ],
            options={
                'verbose_name': 'project phase deadline section',
                'verbose_name_plural': 'project phase deadline sections',
                'ordering': ('index',),
            },
        ),
        migrations.AddField(
            model_name='deadline',
            name='attribute',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deadline', to='projects.Attribute', verbose_name='attribute'),
        ),
        migrations.AlterField(
            model_name='deadline',
            name='condition_attributes',
            field=models.ManyToManyField(blank=True, related_name='condition_to_deadlines', to='projects.Attribute', verbose_name='show if any attribute is set'),
        ),
        migrations.AlterUniqueTogether(
            name='deadline',
            unique_together={('abbreviation', 'subtype')},
        ),
        migrations.CreateModel(
            name='ProjectPhaseSectionDeadline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(default=0, verbose_name='index')),
                ('deadline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Deadline', verbose_name='deadline')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectPhaseDeadlineSection', verbose_name='deadline phase section')),
            ],
            options={
                'verbose_name': 'project phase deadline section item',
                'verbose_name_plural': 'project phase deadline section items',
                'ordering': ('index',),
            },
        ),
        migrations.AddField(
            model_name='projectphasedeadlinesection',
            name='deadlines',
            field=models.ManyToManyField(related_name='phase_sections', through='projects.ProjectPhaseSectionDeadline', to='projects.Deadline', verbose_name='deadlines'),
        ),
        migrations.AddField(
            model_name='projectphasedeadlinesection',
            name='phase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deadline_sections', to='projects.ProjectPhase', verbose_name='phase'),
        ),
        migrations.RemoveField(
            model_name='deadline',
            name='identifier',
        ),
    ]
