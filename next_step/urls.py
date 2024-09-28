from django.contrib import admin
from django.urls import path
from step import views
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('step/', views.step),
    path('offerta/<str:id_offerta>/', views.offerta, name='offerta'),
    path('login/', views.login),
    path('azienda/<str:id_azienda>/', views.azienda, name='azienda'),
]
