# Generated by Django 3.1.13 on 2021-07-21 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authent', '0005_remove_userprofile_language'),
        ('infrastructure', '0024_auto_20210716_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructure',
            name='maintenance_difficulty',
            field=models.ForeignKey(blank=True, help_text="Danger level of maintenance agents' interventions on infrastructure", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='infrastructures_set', to='infrastructure.infrastructuremaintenancedifficultylevel', verbose_name='Maintenance difficulty'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='usage_difficulty',
            field=models.ForeignKey(blank=True, help_text="Danger level of end users' infrastructure usage", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='infrastructures_set', to='infrastructure.infrastructureusagedifficultylevel', verbose_name='Usage difficulty'),
        ),
        migrations.AlterField(
            model_name='infrastructureusagedifficultylevel',
            name='label',
            field=models.CharField(max_length=250, unique=True, verbose_name='Label'),
        ),
        migrations.AlterUniqueTogether(
            name='infrastructuremaintenancedifficultylevel',
            unique_together={('label', 'structure')},
        ),
        migrations.AlterUniqueTogether(
            name='infrastructureusagedifficultylevel',
            unique_together={('label', 'structure')},
        ),
    ]