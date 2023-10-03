# Nama        : Rizqi Bayu Utama
# NPM         : 2206826330
# Kelas       : PBP - C

## Link Aplikasi
Link untuk Aplikasi [Bayu's Inventory](https://bayuinventory.adaptable.app/main/)


# Jawaban Tugas  2

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
1. Pertama saya membuat projek django baru dan mengaktifkan virtual environment yang berguna untuk mengisolasi package serta dependencies dari aplikasi. Mengaktifkan virtual environment dengan perintah berikut:

    ```shell
    python -m venv env
    ```
    ```shell
    #Windows
    env\Scripts\activate.bat
    # Linux/Unix, e.g. Ubuntu, MacOS
    source env/bin/activate
    ```

2. Menyiapkan Dependencies (library, framework, package) dengan membuat requirements.txt 
    - jalankan perintah:

    ```shell
    pip install -r requirements.txt
    ```

    - dan buat proyek Django bernama BayuInventory dengan perintah:

    ```shell
    django-admin startproject BayuInventory
    ```

3. Mengonfigurasi proyek dan menjalankan server
    - Menambahkan `"*"` pada `ALLOWED_HOST` di `settings.py` untuk keperluan deploy
    - Menjalankan command:

    ```shell
    python manage.py runserver 
    ``` 

    - cek di http://localhost:8000 untuk melihat apakah berhasil atau tidak

4. Membuat aplikasi main dalam Proyek
    - jalankan 
    ```shell
    python manage.py startapp main
    ```

    - Mendaftarkan aplikasi `main` pada `INSTALLED_APPS` di `settings.py`

5. Buat direktori bernama `templates` didalam direktori main dan buat file `main.html` yang akan berisi template bagaimana tampilan web nanti

6. Mengubah `models.py` sesuai dengan yang dibutuhkan atau diinginkan

7. Membuat dan mengaplikasikan Migrasi Model
    - melakukannya dengan cara menjalankan perintah 

    ```shell 
    python manage.py makemigrations
    ```
    - Penerapan migrasi dengan

    ```shell
    python manage.py migrate 
    ```

8. Menghubungkan views dengan template
    - Tambahkan code berikut pada `views.py` di dalam aplikasi `main` 

    ```shell
    from django.shortcuts import render 
    ```

    - Menambahkan fungsi show_main yang akan mengembalikan tampilan yang sesuai

9. Konfigurasi URL
    - Konfigurasi url agar aplikasi main dapat diakses melalui web
    - jalankan proyek 

10. Melakukan Deploy pada Adaptable

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, dan models.py, dan berkas html

<img src= "image/FlowChartOrDiagram.png">

### 3. Jelaskan mengapa kita menggunakan virtual environment, apakah bisa membuat aplikasi web berbasis Django tanpa virtual environment?

Alasan menggunakan virtual environment adalah agar ketika rilis Django versi baru kita tetap dapat menjalankan aplikasi kita tanpa masalah seperti masalah perubahan fungsi ataupun tidak bisa berjalan pada modul terbaru. 

Kita tetap bisa membuat aplikasi web berbasis Django tanpa virtual environment, namun dengan resiko seperti yang sudah dijelaskan diatas.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan ketiganya
- MVT: arsitektur untuk memisahkan konponen utama dari sebuah aplikasi (Model, View, Template)
- MVC: framework yang memisahkan aplikasi menjadi 3 logical components (Model, View, Controller)
- MVVM: arsitektur yang memisahkan code menjadi 3 bagian (Model, View, ViewModel)

    Perbedaaan: MVT lebih sederhana dengan Template yang fokus pada tampilan, MVC menggunakan Controller untuk mengendalikan alur aplikasi, sedangkan MVVM memperkenalkan ViewModel untuk mengelola tampilan dan memisahkan logika bisnis dari tampilan. 

# Jawaban Tugas 3

### 1. Perbedaan antara form `POST` dan form `GET` dalam Django?
- **`POST`**:
    - Mengirim informasi ke tujuan tanpa menampilkannya pada URL
    - Variabel `$_POST` menampung informasi yang dikirim
    - Memungkinkan pengiriman informasi dalam jumlah besar tanpa batasan khusus
- **`GET`**:
    - Mengirim informasi dengan menampilkan data di URL
    - Variabel `$_GET` menampung informasi dari URL
    - Keterbatasan panjang URL: hingga 2047 karakter

### 2. Perbedaan antara `XML`, `JSON`, dan `HTML` dalam konteks pengiriman data?
- **`XML`**:
    - Fasilitasi pertukaran data dengan format yang kuat melalui tag-tag khusus
    - Berguna untuk konfigurasi aplikasi dan integrasi lintas platform

- **`JSON`**:
    - Menyajikan data dengan format intuitif, menyerupai notasi objek
    - Ideal untuk komunikasi web dan API

- **`HTML`**:
    - Fokus pada tampilan konten di browser
    - Mengatur tampilan dan interaksi konten

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- **Ringkas dan Mudah Dibaca.**
- **Mendukung Struktur Data yang Kompleks.** 
- **Ringan dan Efisien.**
- **Responsif untuk Aplikasi Web.**

### 4. Jelaskan bagaimana mengimplementasikan checklist di atas secara step-by-step
1. Mengembangkan form input:
    - Membuat `forms.py` di dalam folder "main". Hal ini untuk membuat struktur form yang dapat menerima data produk baru
    - Pada `views.py` definisikan fungsi dengan nama `create_product` yang berguna dalam proses pengisian form
    - Menambahkan fungsi untuk merender `create_product.html`
    - Menambahkan `products = Product.objects.all()` di fungsi `show_main` pada `views.py` 
    - Import fungsi `create_product` yang baru tadi dibuat, lalu tambahkan path url pada `urls.py` untuk bisa diakses
    - Buat file `create_product.html` dalam folder "templates" di main
    - Tambahkan kode di `main.html` untuk menampilkan data item dalam bentuk tabel dan menambahkan tombol "Add New Item" yang mengarahkan ke halaman pengisian item yang ingin ditambahkan
2. Menyediakan fungsi views dalam berbagai format:
    - Di dalam `views.py` definisikan fungsi `show_xml` lalu tambahkan path url agar dapat mengakses fungsi tersebut
    - Definisikan fungsi `show_json` di `views.py` lalu ulangi hal yang sama pada fungsi `show_xml`
    - Definisikan fungsi `show_json_by_id` (untuk json) dan `show_xml_by_id` (untuk xml) dan tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi.

### 5. Mengakses kelima URL
<img src= "image/image.png">
<img src = "image/2.png">
<img src = "image/3.png">
<img src = "image/4.png">
<img src = "image/5.png">

# Jawaban Tugas 4

### 1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah salah satu komponen framework Django yang digunakan untuk membuat user registration form dalam aplikasi web yang memungkinkan user untuk membuat akun baru.
1. Kelebihan:
    - Mudah digunakan
    - Fleksibel
    - terintegrasi dengan Model User Django
    - Kompatibel dengan Django's Authentication System
2. Kekurangan:
    - Tidak mendukung fitur lanjutan
    - Tidak menjamin keamanan
    - Memerlukan penanganan kesalahan tambahan

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    Autentikasi adalah proses verifikasi identitas pengguna yang mencoba mengakses sistem atau aplikasi. Ini adalah langkah awal untuk menentukan siapa pengguna yang mencoba mengakses sumber daya.

    Otorisasi adalah proses yang terjadi setelah autentikasi dan melibatkan pengendalian akses pengguna ke sumber daya tertentu atau tindakan dalam aplikasi. Ini berkaitan dengan perizinan yang diberikan kepada pengguna yang sudah terautentikasi.

    Dalam kombinasi, autentikasi dan otorisasi membantu memastikan bahwa pengguna yang telah diotentikasi memiliki akses yang sesuai dan aman ke sumber daya dalam aplikasi 

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
    Cookies adalah mekanisme kecil yang digunakan dalam pengembangan aplikasi web untuk menyimpan data pada sisi klien 

    Django memanfaatkan cookies untuk mengelola data sesi pengguna dengan cara:
        - Membuat Sesi: Menghasilkan sesi pengguna dan ID sesi unik saat pertama kali masuk
        - Menyimpan Data Sesi: Menyimpan informasi sesi dalam cookies dan mengenkripsinya jika diperlukan
        - Mengakses Data Sesi: Membaca cookies pengguna saat permintaan berikutnya
        - Memperbarui Data Sesi: Memperbolehkan pembuat untuk memperbarui data sesi pengguna
        - Mengakhiri Sesi: Menghapus data sesi saat pengguna keluar atau sesi berakhir

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    Penggunaan cookies tidak selalu aman, ada risiko potensial yang harus diwaspadai seperti:
    1. Kemanan data
    2. Serangan Cross-Site Scripting
    3. Cookie Theft

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Mengimplementasikan fungsi regist, login, dan logout
- Regist:
    - menambahkan `redirect`, `UserCreationForm`, dan `messages` di `views.py`
    - buat fungsi `register` yang membuat form registrasi dan membuat akun pengguna
    - buat file HTML bernama `register.html` di `main/templates`
    - masukan url di `urlpatterns`
- Login:
    - tambahkan fungsi `authenticate` dan `login` di `views.py`
    - buat fungsi `login`
    - buat file HTML baru bernama `login.html` di `main/templates` untuk tampilan halaman login
    - tambahkan `login_user` ke `urls.py`
    - masukan url di `urlpatterns`
- Logout
    - tambahkan fungsi `logout` di `views.py`
    - buat fungsi `logout`
    - di file `main.html` tambahkan code untuk tombol logout
    - tambahkan `logout_user` ke `urls.py`
    - masukan url di `urlpatterns`

2. Membuat 2 akun dengan 3 dummy data
    Melakukan registrasi 2 akun dan menambahkan 3 item sebagai dummy data

3. Menghubungkan model Item dengan User
- menambahkan `user` di `models.py`
- sisipkan `ForeignKey` pada model untuk mengaitkan satu pengguna dengan satu produk
    - modifikasi `create_item` di `views.py`
    - sisipkan parameter `commit=false` untuk mencegah Django menyimpan objek ke database secara langsung
    
4. Menampilkan detail info yang sedang logged in
- Menerapkan kondisi yang memeriksa apakah pengguna telah masuk atau belum dengan menggunakan `request.user.is_authenticated`
- Jika telah masuk, tampilkan info pengguna dengan `request.user.username` dan `request.user.last_login`
- Menggunakan cookies untuk menyimpan sesi login dengan menggunakan `django.contrib.sessions`

# JAWABAN TUGAS 5

### 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya

1. Selector Element (h1, div):
- Manfaat: Memilih elemen berdasarkan jenis atau nama elemen HTML.
- Waktu yang tepat: Digunakan ketika ingin menerapkan gaya umum pada semua elemen dengan jenis yang sama.

2. Selector Class (nama class):
- Manfaat: Memilih elemen berdasarkan nama kelas yang diberikan.
- Waktu yang tepat: Digunakan ketika ingin mengubah dengan class yang sama.

3. Selector ID:
- Manfaat: Memilih elemen berdasarkan ID unik yang diberikan.
- Waktu yang tepat: Biasanya digunakan untuk menargetkan elemen yang sangat spesifik dan tidak digunakan berulang kali.

### 2.  Jelaskan HTML5 Tag yang kamu ketahui.
- <header>: Tag ini digunakan untuk menentukan bagian kepala dari sebuah elemen atau bagian dari halaman web, seperti judul, logo, atau navigasi.

- <nav>: Digunakan untuk mengelompokkan tautan navigasi atau menu dalam halaman web.

- <main>: Mendefinisikan konten utama dalam sebuah dokumen HTML dan biasanya hanya ada satu elemen <main> dalam satu halaman.

- <section>: Mengelompokkan konten terkait dalam sebuah dokumen dan biasanya memiliki judul atau heading yang mendefinisikan bagian tersebut.

- <article>: Menunjukkan konten independen yang dapat berdiri sendiri, seperti artikel berita atau postingan blog.

- <aside>: Digunakan untuk mengelompokkan konten sampingan yang terkait dengan konten utama, seperti sidebar.

- <footer>: Menggambarkan bagian bawah dari sebuah elemen atau halaman web, biasanya berisi informasi penulis, tautan ke kebijakan privasi, atau tautan sosial media.

- <figure> dan <figcaption>: <figure> digunakan untuk mengelompokkan konten media, seperti gambar, video, atau grafik, sementara <figcaption> digunakan untuk menambahkan keterangan untuk media tersebut.

- <a>: Tag ini digunakan untuk membuat tautan atau hyperlink ke halaman web lain atau ke bagian lain dalam halaman yang sama.

- <img>: Untuk menampilkan gambar pada halaman web. Tag ini memiliki atribut src untuk menentukan sumber gambar.

- <video>: Digunakan untuk menampilkan video pada halaman web. Anda dapat mengatur sumber video menggunakan atribut src dan mengontrol video dengan JavaScript.

- <audio>: Mirip dengan <video>, tag ini digunakan untuk menampilkan file audio pada halaman web.

- <canvas>: Digunakan untuk menggambar grafis, membuat animasi, atau melakukan rendering gambar dengan JavaScript.

- <form>: Untuk membuat formulir interaktif yang memungkinkan pengguna untuk mengirimkan data ke server.

- <input>: Bagian dari tag <form>, digunakan untuk membuat elemen input seperti teks, kata sandi, checkbox, dan banyak lagi.

- <textarea>: Digunakan untuk membuat area teks yang lebih besar, seperti kolom komentar atau masukan teks panjang.

- <button>: Membuat tombol interaktif yang dapat di-klik oleh pengguna.

- <ul>, <ol>, dan <li>: Digunakan untuk membuat daftar tak terurut (unordered list) dan daftar terurut (ordered list) serta item-item dalam daftar tersebut.

- <div>: Tag kontainer umum yang digunakan untuk mengelompokkan elemen-elemen HTML dan diberikan kelas atau ID untuk styling dan manipulasi JavaScript.

### 3. Jelaskan perbedaan antara margin dan padding.
1. Margin digunakan untuk mengatur ruang di luar batas elemen, yaitu antara elemen dan elemen-elemen lain di sekitarnya. Margin tidak mempengaruhi tampilan atau isi dari elemen itu sendiri, melainkan hanya menambahkan ruang ekstra di sekitarnya.

2. Padding digunakan untuk mengatur ruang di antara batas elemen dan kontennya sendiri. Padding memengaruhi ruang di dalam elemen, di antara batas elemen dan kontennya, sehingga mengubah ukuran sebenarnya dari elemen tersebut.

### 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step