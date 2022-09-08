# Generated by Django 3.1.7 on 2022-08-07 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mata_pelajaran',
            options={'verbose_name_plural': 'Mata Pelajaran'},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='nama_item',
        ),
        migrations.AlterField(
            model_name='detail_berkas',
            name='keterangan',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='keterangan',
            field=models.CharField(blank=True, choices=[('GURU', 'GURU'), ('MAPEL', 'MAPEL'), ('KELAS', 'KELAS'), ('TEXT', 'TEXT'), ('FILE', 'FILE')], max_length=200, null=True),
        ),
    ]
