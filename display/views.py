
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from administrator.models import Tahun_pelajaran, Kelas,Guru, Tu, Standar, Judul_item, Item,Mata_pelajaran, Detail_berkas
from .decorators import tolakhalaman_ini, ijinkan_pengguna
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import Detail_berkasForm
@tolakhalaman_ini
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cocokan = authenticate(request, username=username, password=password)
        if cocokan is None:
            messages.error(request, 'Usernama dan Password salah')
            return redirect('login_page')
        if cocokan is not None:
            login(request, cocokan)
            return redirect('beranda_admin')
    context = {
       'judul': 'Halaman Beranda Petugas',
        'menu': 'login',
        
    }
    return render(request, 'loginpage.html', context)
def logoutPage(request):
    logout(request)
    return redirect('login_page')

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['tu'])  
def beranda(request):
   
    context = {
       'judul': 'Halaman Beranda Petugas',
        'menu': 'beranda',
        
    }
    return render(request, 'beranda.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['tu'])  
def standarjudul(request, token):
    standar = get_object_or_404(Standar, link_token_standar=token )
    judul = Judul_item.objects.filter(standar__id=standar.id).order_by('id')
    context = {
       'judul': 'Halaman '+ standar.nama_standar ,
        'menu': standar.nama_standar,
        'data': token,
        'judulitem':judul,
        'datastandar':standar,
        'submenu':'deskrpsi'
    }
    return render(request, 'standar_judul.html', context)

def datastandar(request):
    standar = Standar.objects.order_by('id')
    return {'standar':standar}

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['tu'])  
def standarjudulitem(request,token,tokenitem):
    form = Detail_berkasForm()
    standar = get_object_or_404(Standar, link_token_standar=token )
    datajudul = get_object_or_404(Judul_item, link_token_judul_item=tokenitem )
    judul = Judul_item.objects.filter(standar__id=standar.id).order_by('id')
    item = Item.objects.filter(judul_item__id=datajudul.id).order_by('id')
    berkas = Detail_berkas.objects.all().filter(judul_item__link_token_judul_item=tokenitem).order_by('-judul_item__id')
    guru = Guru.objects.order_by('-id')
    mapel = Mata_pelajaran.objects.order_by('-id')
    kelas = Kelas.objects.order_by('-id')
    if request.method == 'POST':
        id_judul_item = request.POST['judul_item']
        idjudulitem = Judul_item.objects.get(id=id_judul_item)
        formsimpan = Detail_berkasForm(request.POST,request.FILES)
        if formsimpan.is_valid():
            simpan = formsimpan.save()
            simpan.judul_item = idjudulitem
            simpan.save()
            return redirect('standarjudulitem', standar.link_token_standar , datajudul.link_token_judul_item)


        
    context = {
       'judul': 'Halaman '+ standar.nama_standar ,
        'menu': standar.nama_standar,
        'data': token,
        'judulitem':judul,
        'datastandar':standar,
        'submenu':tokenitem,
        'keterangan':datajudul,
        'item':item,
        'guru':guru,
        'mapel':mapel,
        'kelas':kelas,
        'form':form,
        'data':berkas

    }
    return render(request, 'standar_judul_item.html', context)

def qrcodestandarjudulitem(request,token,tokenitem):
   
    standar = get_object_or_404(Standar, link_token_standar=token )
    datajudul = get_object_or_404(Judul_item, link_token_judul_item=tokenitem )
    judul = Judul_item.objects.filter(standar__id=standar.id).order_by('id')
    item = Item.objects.filter(judul_item__id=datajudul.id).order_by('id')
    berkas = Detail_berkas.objects.all().filter(judul_item__link_token_judul_item=tokenitem).order_by('-judul_item__id')
    
    

        
    context = {
       'judul': 'Halaman '+ standar.nama_standar ,
        'data': token,
        'judulitem':judul,
        'datastandar':standar,
        'menu':standar.nama_standar,
        'keterangan':datajudul,
        'item':item,
        'data':berkas

    }
    return render(request, 'qrcodestandart.html', context)

def qrcode(request, token_aktifasi):
    data = get_object_or_404(Standar, link_token_standar=token_aktifasi)
    judul = Judul_item.objects.filter(standar__id=data.id).order_by('id')
    
    context = {
        'judul': 'Halaman Qcode Standar',
        'datastandar':data,
         'menu': 'qrcode',
         'judulitem':judul
         
        
    }
    return render(request, 'qrcode.html', context)