from django.urls import path
from .views import *

urlpatterns = [
    path('gul/', gul),
    path('moshina/', moshina),
    path('odam/', odam),
    path('uy/', uy),
    path('tel/', tel),
    path('mevaa/', meva),
    path('davlat/', davlat),
    path('qoshiq/', qoshiq),
    path('yegulik/', yegulik),
    path('rasm/', rasm),
    path('moshinaa/', moshinaa),
]