from django.db import models
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User

import qrcode 
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Tu(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=False, null=True)
    wa = models.CharField(max_length=200, blank=False, null=True,verbose_name="No Whatsapp")
    alamat = RichTextField(blank=True, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True)
    # date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural ="Data TU"

class Tahun_pelajaran(models.Model):
    nama = models.CharField(max_length=200, blank=False, null=True)
    aktif = models.BooleanField(default=True)
    link_token_tahun_pelajaran = models.CharField(max_length=200, blank=False, null=True)
    
   
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural ="Tahun Pelajaran"

class Standar(models.Model):
    
    nama_standar = models.CharField(max_length=200, blank=False, null=True)
    deskripsi = RichTextField(blank=True, null=True)
    link_token_standar = models.CharField(max_length=200, blank=False, null=True)
    qr_code = models.ImageField(upload_to='arsip/data_qrcode',null=True, blank=True)

    @property
    def get_judul_item(self):
        return Judul_item.objects.filter(standar__id=self.id)
    def __str__(self):
        return self.nama_standar
    class Meta:
        verbose_name_plural ="Data Standar"
    def save(self,*args, **kwargs):
        # current_site = get_current_site()
        domain = 'localhost:8000'
        qrcode_img = qrcode.make(f'http://{domain}/qrcode/{self.link_token_standar}/')
        canvas = Image.new('RGB', (450,440), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'{self.nama_standar}-{self.id}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Judul_item(models.Model):
    standar = models.ForeignKey(Standar,  null=True, blank=False, on_delete=models.SET_NULL)
    tahun_pelajaran = models.ForeignKey(Tahun_pelajaran,  null=True, blank=False, on_delete=models.SET_NULL)
    judul_item = models.CharField(max_length=200, blank=False, null=True)
    link_token_judul_item = models.CharField(max_length=200, blank=False, null=True)

    @property
    def get_item(self):
        return Item.objects.filter(judul_item__id=self.id)
    def __str__(self):
        return self.judul_item
    class Meta:
        verbose_name_plural ="Data Judul Item"

class Item(models.Model):
    KETERANGAN=(
        ('GURU' , 'GURU'),
        ('MAPEL' , 'MAPEL'),
        ('KELAS' , 'KELAS'),
        ('TEXT' , 'TEXT'),
        ('FILE' , 'FILE'),
    )
    judul_item = models.ForeignKey(Judul_item,  null=True, blank=False, on_delete=models.SET_NULL)
    nama_item = models.CharField(max_length=200, blank=False, null=True)
    keterangan = models.CharField(max_length=200, blank=True, null=True, choices=KETERANGAN)
    link_token_item = models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.judul_item
    class Meta:
        verbose_name_plural ="Data Item"




class Guru(models.Model):
      
    nama_guru = models.CharField(max_length=200, blank=False, null=True)
    alamat = models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.nama_guru
    class Meta:
        verbose_name_plural ="Data Guru"
class Kelas(models.Model):
      
    kode_kelas = models.CharField(max_length=200, blank=False, null=True)
    nama_kelas = models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.nama_kelas
    class Meta:
        verbose_name_plural ="Data Kelas"
class Mata_pelajaran(models.Model):
  
    kode_mata_pelajaran = models.CharField(max_length=200, blank=False, null=True)
    nama_mata_pelajaran = models.CharField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.nama_mata_pelajaran
    class Meta:
        verbose_name_plural ="Mata Pelajaran"
        
class Detail_berkas(models.Model):
    judul_item = models.ForeignKey(Judul_item,  null=True, blank=True, on_delete=models.SET_NULL)
    guru = models.ForeignKey(Guru,  null=True, blank=True, on_delete=models.SET_NULL)
    kelas = models.ForeignKey(Kelas,  null=True, blank=True, on_delete=models.SET_NULL)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran,  null=True, blank=True, on_delete=models.SET_NULL)
    berkas = models.FileField(upload_to='arsip/berkas',null=True, blank=True)
    teks = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.judul_item.judul_item
    class Meta:
        verbose_name_plural ="Detail Berkas"