# Generated by Django 2.1.3 on 2018-11-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa_xyz', '0005_auto_20181118_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='comissao',
            new_name='comissao_servico',
        ),
        migrations.AddField(
            model_name='servico',
            name='empresa_prestadora',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
