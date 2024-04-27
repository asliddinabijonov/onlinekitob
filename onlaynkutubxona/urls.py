from django.contrib import admin
from django.urls import path

from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolim/', BolimView.as_view(), name='bolim'),
    path('kitoblar/', KitobView.as_view(), name='kitoblar'),
    path('kitoblar/<int:pk>/kitob/', KitobHaqidaView.as_view(), name='kitob'),
    path('kitoblar/<int:pk>/tahrirlash/', KitobEditView.as_view(), name='tahrirlash'),
    path('yangi_asarlar/', YangiView.as_view(), name='yangi'),
]
