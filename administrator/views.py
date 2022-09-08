import imp
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import uuid
from .models import Tahun_pelajaran, Kelas,Guru, Tu, Standar, Judul_item, Item,Mata_pelajaran, Detail_berkas
from .forms import ItemForm, Tahun_pelajaranForm, TuForm, UserForm,GuruForm, KelasForm,Mata_pelajaranForm, StandarForm, Judul_itemForm
from django.contrib.auth.decorators import login_required
from display.decorators import ijinkan_pengguna,pilihan_login


@login_required(login_url='login_page')
@pilihan_login
def beranda_admin (request):
    jmlStandar = Standar.objects.all().count()
    jmlKelas = Kelas.objects.all().count()
    jmlGuru = Guru.objects.all().count()
    jmlMata_pelajaran = Mata_pelajaran.objects.all().count()
    context = {
        'judul': 'Halaman Beranda',
        'menu': 'beranda',
        'jmlStandar':jmlStandar,
        'jmlKelas':jmlKelas,
        'jmlGuru':jmlGuru,
        'jmlMata_pelajaran':jmlMata_pelajaran



    


    }
    return render(request, 'admin_beranda.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def tahun_pelajaran_admin(request):
    tahun_pelajaran = Tahun_pelajaran.objects.all()
    context = {
        'judul': 'Halaman Tahun Pelajaran',
        'menu': 'tahun_pelajaran',
        'data':tahun_pelajaran,
    }
    return render(request, 'admin_tahun_pelajaran.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formtahun_pelajaran_admin(request):
    form = Tahun_pelajaranForm()
    auth_token = str(uuid.uuid4())
    if request.method == 'POST':
        formsimpan = Tahun_pelajaranForm(request.POST)
        if formsimpan.is_valid():
            simpan = formsimpan.save()
            simpan.link_token_tahun_pelajaran = auth_token
            simpan.save()
            return redirect('tahun_pelajaran_admin')
    context = {
        'judul': 'Form Tahun_pelajaran',
        'menu': 'tahun_pelajaran',
        'form':form
    }
    return render(request, 'admin_formtahun_pelajaran.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def edittahun_pelajaran_admin(request, pk):
    tahun_pelajaran = Tahun_pelajaran.objects.get(id=pk)
    form = Tahun_pelajaranForm(instance=tahun_pelajaran)
    if request.method == 'POST':
        formsimpan = Tahun_pelajaranForm(request.POST, instance=tahun_pelajaran)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('tahun_pelajaran_admin')
    context = {
        'judul': 'Form Edit Tahun_pelajaran',
        'menu': 'tahun_pelajaran',
        'form':form
    }
    return render(request, 'admin_formtahun_pelajaran.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deletetahun_pelajaran_admin(request, pk):
    hapus = Tahun_pelajaran.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('tahun_pelajaran_admin')

    context = {
        'judul': 'Form Hapus Tahun_pelajaran',
        'menu': 'tahun_pelajaran',
        'hapus':hapus  
    }
    return render(request, 'admin_hapustahun_pelajaran.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def tu_admin(request):
    tu = Tu.objects.all()
    context = {
        'data': tu,
        'judul': 'Halaman Tu',
        'menu': 'tu',
    }
    return render(request, 'admin_tu.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formtu_admin(request):
    form = TuForm()
    formuser = UserForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.is_active = True
        user.save()

        akses = Group.objects.get(name='tu')
        user.groups.add(akses)

        formsimpan = TuForm(request.POST)
        if formsimpan.is_valid():
            data = formsimpan.save()
            data.user = user
            data.save()
            return redirect('tu_admin')
    context = {
        'judul': 'Halaman Form Tu',
        'menu': 'tu',
        'form':form,
        'formuser':formuser
    }
    return render(request, 'admin_formtu.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def edittu_admin(request, pk):
    tu = Tu.objects.get(id=pk)
    user = User.objects.get(id=tu.user.id)
    form = TuForm(instance=tu)
    formuser = UserForm(instance=user)
    if request.method == 'POST':
        formsimpan = TuForm(request.POST,request.FILES, instance=tu)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('tu_admin')
    context = {
       'judul': 'Halaman Form Edit Tu',
        'menu': 'tu',
        'form':form,
        'formuser':formuser
    }
    return render(request, 'admin_formtu.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deletetu_admin(request, pk):
    hapus = Tu.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('tu_admin')
    context = {
        'judul': 'Halaman Hapus Tu',
        'menu': 'tu',
        'hapus':hapus  
    }
    return render(request, 'admin_hapustu.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def guru_admin(request):
    guru = Guru.objects.all()
    context = {
        'judul': 'Halaman Guru',
        'menu': 'guru',
        'data':guru,
    }
    return render(request, 'admin_guru.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formguru_admin(request):
    form = GuruForm()
    if request.method == 'POST':
        formsimpan = GuruForm(request.POST)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('guru_admin')
    context = {
        'judul': 'Form Guru',
        'menu': 'guru',
        'form':form
    }
    return render(request, 'admin_formguru.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def editguru_admin(request, pk):
    guru = Guru.objects.get(id=pk)
    form = GuruForm(instance=guru)
    if request.method == 'POST':
        formsimpan = GuruForm(request.POST, instance=guru)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('guru_admin')
    context = {
        'judul': 'Form Edit Guru',
        'menu': 'guru',
        'form':form
    }
    return render(request, 'admin_formguru.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deleteguru_admin(request, pk):
    hapus = Guru.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('guru_admin')

    context = {
        'judul': 'Form Hapus Guru',
        'menu': 'guru',
        'hapus':hapus  
    }
    return render(request, 'admin_hapusguru.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def kelas_admin(request):
    kelas = Kelas.objects.all()
    context = {
        'judul': 'Halaman Kelas',
        'menu': 'kelas',
        'data':kelas,
    }
    return render(request, 'admin_kelas.html', context)
@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formkelas_admin(request):
    form = KelasForm()
    if request.method == 'POST':
        formsimpan = KelasForm(request.POST)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('kelas_admin')
    context = {
        'judul': 'Form Kelas',
        'menu': 'kelas',
        'form':form
    }
    return render(request, 'admin_formkelas.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def editkelas_admin(request, pk):
    kelas = Kelas.objects.get(id=pk)
    form = KelasForm(instance=kelas)
    if request.method == 'POST':
        formsimpan = KelasForm(request.POST, instance=kelas)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('kelas_admin')
    context = {
        'judul': 'Form Edit Kelas',
        'menu': 'kelas',
        'form':form
    }
    return render(request, 'admin_formkelas.html', context)
@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deletekelas_admin(request, pk):
    hapus = Kelas.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('kelas_admin')

    context = {
        'judul': 'Form Hapus Kelas',
        'menu': 'kelas',
        'hapus':hapus  
    }
    return render(request, 'admin_hapuskelas.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def mata_pelajaran_admin(request):
    mata_pelajaran = Mata_pelajaran.objects.all()
    context = {
        'judul': 'Halaman Mata_pelajaran',
        'menu': 'mata_pelajaran',
        'data':mata_pelajaran,
    }
    return render(request, 'admin_mata_pelajaran.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formmata_pelajaran_admin(request):
    form = Mata_pelajaranForm()
    if request.method == 'POST':
        formsimpan = Mata_pelajaranForm(request.POST)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('mata_pelajaran_admin')
    context = {
        'judul': 'Form Mata_pelajaran',
        'menu': 'mata_pelajaran',
        'form':form
    }
    return render(request, 'admin_formmata_pelajaran.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def editmata_pelajaran_admin(request, pk):
    mata_pelajaran = Mata_pelajaran.objects.get(id=pk)
    form = Mata_pelajaranForm(instance=mata_pelajaran)
    if request.method == 'POST':
        formsimpan = Mata_pelajaranForm(request.POST, instance=mata_pelajaran)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('mata_pelajaran_admin')
    context = {
        'judul': 'Form Edit Mata_pelajaran',
        'menu': 'mata_pelajaran',
        'form':form
    }
    return render(request, 'admin_formmata_pelajaran.html', context)
@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deletemata_pelajaran_admin(request, pk):
    hapus = Mata_pelajaran.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('mata_pelajaran_admin')

    context = {
        'judul': 'Form Hapus Mata_pelajaran',
        'menu': 'mata_pelajaran',
        'hapus':hapus  
    }
    return render(request, 'admin_hapusmata_pelajaran.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def standar_admin(request):
    standar = Standar.objects.all()
    context = {
        'judul': 'Halaman Standar',
        'menu': 'standar',
        'data':standar,
    }
    return render(request, 'admin_standar.html', context)
@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formstandar_admin(request):
    form = StandarForm()
    auth_token = str(uuid.uuid4())
    if request.method == 'POST':
        formsimpan = StandarForm(request.POST)
        if formsimpan.is_valid():
            simpan = formsimpan.save()
            simpan.link_token_standar =auth_token
            simpan.save()
            return redirect('standar_admin')
    context = {
        'judul': 'Form Standar',
        'menu': 'standar',
        'form':form
    }
    return render(request, 'admin_formstandar.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def editstandar_admin(request, pk):
    standar = Standar.objects.get(id=pk)
    form = StandarForm(instance=standar)
    if request.method == 'POST':
        formsimpan = StandarForm(request.POST, instance=standar)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('standar_admin')
    context = {
        'judul': 'Form Edit Standar',
        'menu': 'standar',
        'form':form
    }
    return render(request, 'admin_formstandar.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deletestandar_admin(request, pk):
    hapus = Standar.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('standar_admin')

    context = {
        'judul': 'Form Hapus Standar',
        'menu': 'standar',
        'hapus':hapus  
    }
    return render(request, 'admin_hapusstandar.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def judul_item_admin(request):
    judul_item = Judul_item.objects.all().order_by('-standar__id')
    context = {
        'judul': 'Halaman Judul_item',
        'menu': 'judul_item',
        'data':judul_item,
    }
    return render(request, 'admin_judul_item.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formjudul_item_admin(request):
    auth_token = str(uuid.uuid4())
    form = Judul_itemForm()
    if request.method == 'POST':
        formsimpan = Judul_itemForm(request.POST)
        if formsimpan.is_valid():
            simpan = formsimpan.save()
            simpan.link_token_judul_item =auth_token
            simpan.save()
            return redirect('judul_item_admin')
    context = {
        'judul': 'Form Judul_item',
        'menu': 'judul_item',
        'form':form
    }
    return render(request, 'admin_formjudul_item.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def editjudul_item_admin(request, pk):
    judul_item = Judul_item.objects.get(id=pk)
    form = Judul_itemForm(instance=judul_item)
    if request.method == 'POST':
        formsimpan = Judul_itemForm(request.POST, instance=judul_item)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('judul_item_admin')
    context = {
        'judul': 'Form Edit Judul_item',
        'menu': 'judul_item',
        'form':form
    }
    return render(request, 'admin_formjudul_item.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator'])  
def deletejudul_item_admin(request, pk):
    hapus = Judul_item.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('judul_item_admin')

    context = {
        'judul': 'Form Hapus Judul_item',
        'menu': 'judul_item',
        'hapus':hapus  
    }
    return render(request, 'admin_hapusjudul_item.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def item_admin(request):
    item = Item.objects.all().order_by('-judul_item__standar__id')
    context = {
        'judul': 'Halaman Item',
        'menu': 'item',
        'data':item,
    }
    return render(request, 'admin_item.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formitem_admin(request):
    form = ItemForm()
    auth_token = str(uuid.uuid4())
    if request.method == 'POST':
        formsimpan = ItemForm(request.POST)
        if formsimpan.is_valid():
            simpan = formsimpan.save()
            simpan.link_token_item = auth_token
            simpan.save()
            return redirect('item_admin')
    context = {
        'judul': 'Form Item',
        'menu': 'item',
        'form':form
    }
    return render(request, 'admin_formitem.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def edititem_admin(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        formsimpan = ItemForm(request.POST, instance=item)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('item_admin')
    context = {
        'judul': 'Form Edit Item',
        'menu': 'item',
        'form':form
    }
    return render(request, 'admin_formitem.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator'])  
def deleteitem_admin(request, pk):
    hapus = Item.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('item_admin')

    context = {
        'judul': 'Form Hapus Item',
        'menu': 'item',
        'hapus':hapus  
    }
    return render(request, 'admin_hapusitem.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def detail_berkas_admin(request):
    berkas = Detail_berkas.objects.all().order_by('-judul_item__standar__id')
    context = {
        'judul': 'Halaman Data Berkas',
        'menu': 'berkas',
        'data':berkas,
    }
    return render(request, 'admin_berkas.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator'])  
def deletedetail_berkas_admin(request, pk):
    hapus = Detail_berkas.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('detail_berkas_admin')

    context = {
        'judul': 'Form Hapus Berkas',
        'menu': 'detail_berkas',
        'hapus':hapus  
    }
    return render(request, 'admin_hapusdetail_berkas.html', context)