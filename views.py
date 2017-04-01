# -*- coding: utf-8 -*-
from django.http import *
import subprocess

def taramaGoster(request):
    try:
        dosya=open("lokalNmap.txt","r")
        sonuc=dosya.readlines()
        dosya.close()
        r=""
        for i in sonuc:
            r=r+"<br>"+i
        response=u"Nmap tarama sonucu: %s" %r
        return HttpResponse(response)
    except:
        return HTTPResponse(u"Sonuc bulunamadi...")

def taramaBaslat(request,IP):
    komut="/usr/local/bin/nmap -sS -sV "+str(IP)+" > lokalNmap.txt"
    subprocess.Popen(komut,shell=True)
    return HttpResponse(u"Tarama basladi")

def taramaFiltrele(request,IP):
    try:
        dosya=open("lokalNmap.txt","r")
        sonuc=dosya.readlines()
        dosya.close()
        r=""
        for i in sonuc:
            if " on "+str(IP) in i:
                r=r+"<br>"+i
        response=u"Nmap tarama sonucu filtrelenmis sonuc: %s" %r
        return HttpResponse(response)
    except:
        return HTTPResponse(u"Sonuc bulunamadi...")

def canliIPler(request):
    try:
        dosya=open("lokalNmap.txt","r")
        sonuc=dosya.readlines()
        dosya.close()
        r=""
        for i in sonuc:
            if "Nmap scan report for" in i:
                r=r+"<br>"+i
        response=u"Nmap tarama sonucu canli IP'ler: %s" %r
        return HttpResponse(response)
    except:
        return HTTPResponse(u"Sonuc bulunamadi...")

def macAdresler(request):
    try:
        dosya=open("lokalNmap.txt","r")
        sonuc=dosya.readlines()
        dosya.close()
        r=""
        for i in sonuc:
            if "MAC Address" in i:
                r=r+"<br>"+i
        response=u"Nmap tarama sonucu bulunan MAC adresler: %s" %r
        return HttpResponse(response)
    except:
        return HTTPResponse(u"Sonuc bulunamadi...")

def acikPortlar(request):
    try:
        dosya=open("lokalNmap.txt","r")
        sonuc=dosya.readlines()
        dosya.close()
        r=""
        for i in sonuc:
            if " open " in i:
                r=r+"<br>"+i
        response=u"Nmap tarama sonucu bulunan acik portlar: %s" %r
        return HttpResponse(response)
    except:
        return HTTPResponse(u"Sonuc bulunamadi...")

def ana_sayfa(request):
    return HttpResponse("""<h1>Nmap Tarama Uygulamasi</h1>
    <br>127.0.0.1:8000/taramaGoster  Tarama sonucunu gosterir
    <br>127.0.0.1:8000/taramaBaslat/192.168.100.0-255  Tarama baslatir
    <br>127.0.0.1:8000/taramaFiltrele/192.168.100.10  Tarama filtreleme yapar
    <br>127.0.0.1:8000/canliIPler  Taramadaki canli IP'leri gosterir
    <br>127.0.0.1:8000/macAdresler  Taramadaki Mac adresleri gosterir
    <br>127.0.0.1:8000/acikPortlar  Taramadaki acik portlari gosterir
    """)