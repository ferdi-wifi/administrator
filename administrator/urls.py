from django.urls import path
from . import views


urlpatterns = [
    path('', views.beranda_admin, name='beranda_admin'),

    path('tahun-pelajaran-admin/', views.tahun_pelajaran_admin, name='tahun_pelajaran_admin'),
    path('form-tahun_pelajaran/', views.formtahun_pelajaran_admin, name='formtahun_pelajaran_admin'),
    path('edit-tahun_pelajaran/<str:pk>', views.edittahun_pelajaran_admin, name='edittahun_pelajaran_admin'),
    path('delete-tahun_pelajaran/<str:pk>', views.deletetahun_pelajaran_admin, name='deletetahun_pelajaran_admin'),


    path('tu-admin/', views.tu_admin, name='tu_admin'),
     path('form-tu/', views.formtu_admin, name='formtu_admin'),
    path('edit-tu/<str:pk>', views.edittu_admin, name='edittu_admin'),
    path('delete-tu/<str:pk>', views.deletetu_admin, name='deletetu_admin'),
    
    path('guru-admin/', views.guru_admin, name='guru_admin'),
    path('form-guru/', views.formguru_admin, name='formguru_admin'),
    path('edit-guru/<str:pk>', views.editguru_admin, name='editguru_admin'),
    path('delete-guru/<str:pk>', views.deleteguru_admin, name='deleteguru_admin'),

     path('kelas-admin/', views.kelas_admin, name='kelas_admin'),
    path('form-kelas/', views.formkelas_admin, name='formkelas_admin'),
    path('edit-kelas/<str:pk>', views.editkelas_admin, name='editkelas_admin'),
    path('delete-kelas/<str:pk>', views.deletekelas_admin, name='deletekelas_admin'),

    
     path('mata_pelajaran-admin/', views.mata_pelajaran_admin, name='mata_pelajaran_admin'),
    path('form-mata_pelajaran/', views.formmata_pelajaran_admin, name='formmata_pelajaran_admin'),
    path('edit-mata_pelajaran/<str:pk>', views.editmata_pelajaran_admin, name='editmata_pelajaran_admin'),
    path('delete-mata_pelajaran/<str:pk>', views.deletemata_pelajaran_admin, name='deletemata_pelajaran_admin'),

    path('standar-admin/', views.standar_admin, name='standar_admin'),
    path('form-standar/', views.formstandar_admin, name='formstandar_admin'),
    path('edit-standar/<str:pk>', views.editstandar_admin, name='editstandar_admin'),
    path('delete-standar/<str:pk>', views.deletestandar_admin, name='deletestandar_admin'),


    path('judul_item-admin/', views.judul_item_admin, name='judul_item_admin'),
    path('form-judul_item/', views.formjudul_item_admin, name='formjudul_item_admin'),
    path('edit-judul_item/<str:pk>', views.editjudul_item_admin, name='editjudul_item_admin'),
    path('delete-judul_item/<str:pk>', views.deletejudul_item_admin, name='deletejudul_item_admin'),


    path('item-admin/', views.item_admin, name='item_admin'),
    path('form-item/', views.formitem_admin, name='formitem_admin'),
    path('edit-item/<str:pk>', views.edititem_admin, name='edititem_admin'),
    path('delete-item/<str:pk>', views.deleteitem_admin, name='deleteitem_admin'),

    path('detail-berkas-admin/', views.detail_berkas_admin, name='detail_berkas_admin'),
    path('delete-detailberkas/<str:pk>', views.deletedetail_berkas_admin, name='deletedetail_berkas_admin'),
    

]
  
