from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gul/', include('core.urls')),
    path('moshina/', include('core.urls')),
    path('odam/', include('core.urls')),
    path('uy/', include('core.urls')),
    path('tel/', include('core.urls')),
    path('meva/', include('core.urls')),
    path('davlat/', include('core.urls')),
    path('qoshiq/', include('core.urls')),
    path('yegulik/', include('core.urls')),
    path('rasm/', include('core.urls')),
    path('moshinaa/', include('core.urls')),
]
