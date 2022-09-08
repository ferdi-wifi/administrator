# Generated by Django 3.1.7 on 2022-07-28 06:45

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_guru', models.CharField(max_length=200, null=True)),
                ('alamat', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Data Guru',
            },
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_kelas', models.CharField(max_length=200, null=True)),
                ('nama_kelas', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Data Kelas',
            },
        ),
        migrations.CreateModel(
            name='Mata_pelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_mata_pelajaran', models.CharField(max_length=200, null=True)),
                ('nama_mata_pelajaran', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Mat Pelajaran',
            },
        ),
        migrations.CreateModel(
            name='Standar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_standar', models.CharField(max_length=200, null=True)),
                ('deskripsi', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('link_token_standar', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Data Standar',
            },
        ),
        migrations.CreateModel(
            name='Tahun_pelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('aktif', models.BooleanField(default=True)),
                ('link_token_tahun_pelajaran', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tahun Pelajaran',
            },
        ),
        migrations.CreateModel(
            name='Tu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
                ('wa', models.CharField(max_length=200, null=True, verbose_name='No Whatsapp')),
                ('alamat', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Data TU',
            },
        ),
        migrations.CreateModel(
            name='Judul_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_item', models.CharField(max_length=200, null=True)),
                ('link_token_judul_item', models.CharField(max_length=200, null=True)),
                ('standar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.standar')),
                ('tahun_pelajaran', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.tahun_pelajaran')),
            ],
            options={
                'verbose_name_plural': 'Data Judul Item',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200, null=True)),
                ('keterangan', models.CharField(max_length=200, null=True)),
                ('link_token_item', models.CharField(max_length=200, null=True)),
                ('judul_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.judul_item')),
            ],
            options={
                'verbose_name_plural': 'Data Item',
            },
        ),
        migrations.CreateModel(
            name='Detail_berkas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.CharField(max_length=200, null=True)),
                ('berkas', models.FileField(blank=True, null=True, upload_to='arsip/berkas')),
                ('teks', models.CharField(blank=True, max_length=200, null=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.item')),
            ],
            options={
                'verbose_name_plural': 'Data Item',
            },
        ),
    ]