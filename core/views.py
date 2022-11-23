from django.shortcuts import render

from .models import *


def gul(request):
    ag = Atirgul.objects.all()
    aglar = {
        'ag': ag
    }
    return render(request, 'meva.html', aglar)

def moshina(request):
    moshinalar = Moshina.objects.all()
    moshina = {
        'moshinalar': moshinalar
    }
    return render(request, 'moshina.html', moshina)

def odam(request):
    odamlar = Odam.objects.all()
    odam = {
        'odamlar': odamlar
    }
    return render(request, 'odam.html', odam)


def uy(request):
    uylar = Uy.objects.all()
    uy = {
        'uylar': uylar
    }
    return render(request, 'uy.html', uy)

def tel(request):
    tellar = Telefon.objects.all()
    tel = {
        "tellar": tellar
    }
    return render(request, 'uy.html', tel)

def meva(request):
    mevalar = Meva.objects.all()
    meva = {
        'mevalar': mevalar
    }
    return render(request, 'mevaa.html', meva)

def davlat(request):
    davlatlar = Davlat.objects.all()
    davlat = {
        'davlatlar': davlatlar
    }
    return render(request, 'davlat.html', davlat)

def qoshiq(request):
    qoshiqlar = Qoshiq.objects.all()
    qoshiq = {
        'qoshiqlar': qoshiqlar
    }
    return render(request, 'qoshiq.html', qoshiq)

def yegulik(request):
    yeguliklar = Yegulik.objects.all()
    yegulik = {
        'yeguliklar': yeguliklar
    }
    return render(request, 'yegulik.html', yegulik)

def rasm(request):
    rasmlar = Rasm.objects.all()
    rasm = {
        'rasmlar': rasmlar
    }
    return render(request, 'rasm.html', rasm)

def moshinaa(request):
    moshinaalar = Moshinaa.objects.all()
    moshinaa = {
        'moshinaalar': moshinaalar
    }
    return  render(request, 'moshinaa.html', moshinaa)