# djangoNmap
Django ile Nmap Uygulaması

wsgi.py, views.py, urls.py, settings.py, init.py manage.py,lokalNmap.txt,db.sqlite3 dosyalarından bir üst dizinde django1 klasöründe oluşturulmuştur.

Kullanım:

İlgili dizine erişim sağladıktan sonra sudo python manage.py runserver komutunu girmemiz gerekmektedir.

127.0.0.1:8000/ Anasayfa

127.0.0.1:8000/taramaGoster Tarama sonucunu gosterir

127.0.0.1:8000/taramaBaslat/192.168.100.0-255 Tarama baslatir

127.0.0.1:8000/taramaFiltrele/192.168.100.10 Tarama filtreleme yapar

127.0.0.1:8000/canliIPler Taramadaki canli IP'leri gosterir

127.0.0.1:8000/macAdresler Taramadaki Mac adresleri gosterir

127.0.0.1:8000/acikPortlar Taramadaki acik portlari gosterir
