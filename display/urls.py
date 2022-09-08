from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.loginpage, name='login_page'),
    path('beranda', views.beranda, name='beranda'),
    path('logout', views.logoutPage, name='logout'),
    path('standar-judul/<str:token>', views.standarjudul, name='standarjudul'),
    path('standar-judul/<str:token>/<str:tokenitem>', views.standarjudulitem, name='standarjudulitem'),
   
    path('qrcode/<str:token_aktifasi>/', views.qrcode, name='qrcode'),
    path('qrcode-standar/<str:token>/<str:tokenitem>', views.qrcodestandarjudulitem, name='qrcodestandarjudulitem'),

]
  
