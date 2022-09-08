from django import forms
from django.forms import ModelForm
from administrator.models import Detail_berkas


class Detail_berkasForm(ModelForm):
    class Meta:
        model = Detail_berkas
        fields=['guru','kelas','mata_pelajaran','berkas','teks']
        widgets = {
            'guru': forms.Select(attrs={'class': 'form-control'}),
            'kelas': forms.Select(attrs={'class': 'form-control'}),
            'mata_pelajaran': forms.Select(attrs={'class': 'form-control'}),
            'berkas': forms.FileInput(attrs={'class': 'form-control'}),
            'teks': forms.TextInput(attrs={'class': 'form-control'}),

        }
