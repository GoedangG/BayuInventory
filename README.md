# Nama        : Rizqi Bayu Utama
# NPM         : 2206826330
# Kelas       : PBP - C

## Link Aplikasi
Link untuk Aplikasi [Bayu's Inventory](https://bayuinventory.adaptable.app/)

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
1. Pertama saya membuat projek django baru dan mengaktifkan virtual environment yang berguna untuk mengisolasi package serta dependencies dari aplikasi. Mengaktifkan virtual environment dengan perintah berikut:
 '''
 python -m venv env
 '''
 Karena saya menjalankannya di windows maka:
 '''
 env\Scripts\activate.bat
 '''

2. Menyiapkan Dependencies (library, framework, package) dengan membuat requirements.txt dan menjalankan perintah:
'''
pip install -r requirements.txt
'''
dan buat proyek Django bernama BayuInventory dengan perintah:
'''
django-admin startproject BayuInventory
'''

3. Mengonfigurasi proyek dan menjalankan server
- Menambahkan "*" pada ALLOWED_HOST di settings.py untuk keperluan deploy
- Menjalankan command ''' python manage.py runserver ''' di shell
- cek di http://localhost:8000 untuk melihat apakah berhasil atau tidak

4. Membuat aplikasi main dalam Proyek
- jalankan '''python manage.py startapp main'''
- Mendaftarkan aplikasi 'main' pada INSTALLED_APPS di settings.py

5. Buat direktori bernama templates didalam direktori main dan buat file main.html yang akan berisi template bagaimana tampilan web nanti

6. Mengubah models.py sesuai dengan yang dibutuhkan atau diinginkan

7. Membuat dan mengaplikasikan Migrasi Model
- melakukannya dengan cara menjalankan perintah ''' python manage.py makemigrations '''
- Penerapan migrasi dengan ''' python manage.py migrate '''

8. Menghubungkan views dengan template
- Tambahkan code berikut pada views.py di dalam aplikasi main ''' from django.shortcuts import render '''
- Menambahkan fungsi show_main yang akan mengembalikan tampilan yang sesuai

9. Konfigurasi URL
- Konfigurasi url agar aplikasi main dapat diakses melalui web
- jalankan proyek dengan perintah ''' python manage.py runserver ''' dan cek di http://localhost:8000 apakah berhasil

10. Melakukan Deploy pada Adaptable

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, dan models.py, dan berkas html



### 3. Jelaskan mengapa kita menggunakan virtual environment, apakah bisa membuat aplikasi web berbasis Django tanpa virtual environment?

Alasan menggunakan virtual environment adalah agar ketika rilis Django versi baru kita tetap dapat menjalankan aplikasi kita tanpa masalah seperti masalah perubahan fungsi ataupun tidak bisa berjalan pada modul terbaru. 

Kita tetap bisa membuat aplikasi web berbasis Django tanpa virtual environment, namun dengan resiko seperti yang sudah dijelaskan diatas.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan ketiganya
- MVT: arsitektur untuk memisahkan konponen utama dari sebuah aplikasi (Model, View, Template)
- MVC: framework yang memisahkan aplikasi menjadi 3 logical components (Model, View, Controller)
- MVVM: arsitektur yang memisahkan code menjadi 3 bagian (Model, View, ViewModel)

Perbedaaan: MVT lebih sederhana dengan Template yang fokus pada tampilan, MVC menggunakan Controller untuk mengendalikan alur aplikasi, sedangkan MVVM memperkenalkan ViewModel untuk mengelola tampilan dan memisahkan logika bisnis dari tampilan. 