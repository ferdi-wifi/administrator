from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tahun_pelajaran, Kelas,Guru, Tu, Standar, Judul_item, Item,Mata_pelajaran, Detail_berkas


class Tahun_pelajaranForm(ModelForm):
    class Meta:
        model = Tahun_pelajaran
        fields=['nama','aktif']
    labels = {
            'nama': 'Nama Jenis:',
        }
class GuruForm(ModelForm):
    class Meta:
        model = Guru
        fields=['nama_guru','alamat']
    labels = {
            'nama_guru': 'Nama Guru:',
        }
class KelasForm(ModelForm):
    class Meta:
        model = Kelas
        fields=['kode_kelas','nama_kelas']
   
class Mata_pelajaranForm(ModelForm):
    class Meta:
        model = Mata_pelajaran
        fields=['kode_mata_pelajaran','nama_mata_pelajaran']
   
class StandarForm(ModelForm):
    class Meta:
        model = Standar
        fields=['nama_standar','deskripsi']
class Judul_itemForm(ModelForm):
    class Meta:
        model = Judul_item
        fields=['tahun_pelajaran','standar','judul_item']
   
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields=['judul_item','nama_item','keterangan']
   

class TuForm(ModelForm):
    class Meta:
        model = Tu
        fields=['nama','wa','alamat','email']
        widgets = {
            'wa': forms.TextInput(attrs={'class': 'form-control','placeholder':'628xxxxxxxxxx'}),

        }
class UserForm(ModelForm):
    class Meta:
        model= User
        fields =['username']
        help_texts ={
            'username':''
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','required':'required'}),
        }
        labels = {
            'username': 'Username*',
        }
