# ReChefy

ReChefy merupakan aplikasi berbasis desktop yang hadir sebagai teman memasak Anda. Bersama ReChefy, Anda dapat memasak dengan lebih mudah dengan adanya fitur untuk melihat resep masakan. Anda juga dapat menambahkan resep pada aplikasi, serta menyunting dan menghapus resep buatan Anda. ReChefy juga dapat meningkatkan pengalaman memasak Anda dengan adanya fitur komentar pada setiap resep, sehingga Anda dapat memberikan catatan mengenai resep-resep pada aplikasi. Selain itu, ReChefy juga dilengkapi dengan kumpulan artikel memasak yang dapat Anda baca.

## Cara Menjalankan Aplikasi
1. Clone repository dengan menjalankan perintah ```git clone git@gitlab.informatika.org:Raylouis/if2250-2023-k01-11-rechify.git``` pada terminal.
2. Install requirements.txt pada repository dengan menjalankan perintah ```pip install -r requirements.txt``` pada terminal.
3. Pada directory repository, jalankan perintah ```./run.bat``` pada terminal.
4. Aplikasi ReChefy sudah dapat Anda gunakan.

## Daftar Modul yang Diimplementasikan
### Welcome Page
Berikut adalah tampilan dari Welcome Page.

### Menu
Berikut adalah tampilan dari Menu

### Daftar Artikel
Berikut adalah tampilan dari Daftar Artikel

### Lihat Artikel
Berikut adalah tampilan dari Lihat Artikel

### Daftar Resep
Berikut adalah tampilan dari Daftar Resep

### Lihat Resep
Berikut adalah tampilan dari Lihat Resep

### Tambah Resep
Berikut adalah tampilan dari Tambah Resep

### Sunting Resep
Berikut adalah tampilan dari Sunting Resep


## Daftar Tabel Basis Data yang Diimplementasikan
### Resep
| Atribut | Tipe | Key | Constraint |
|---------|------| ----|------------|
| idResep | integer | primary key | autoincrement, not null |
| gambarMasakan| blob | | not null |
| namaMasakan | text | | not null|
| deskripsiMasakan| text|| not null|
| langkahMemasak|text||not null|
| isDefault|integer||not null, default 0, isDefault = 0 or isDefault = 1|

### Bahan
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idBahan|integer|primary key|autoincrement, not null|
|namaBahan|text||not null|

### Alat
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idAlat|integer|primary key|autoincrement, not null|
|namaAlat|text||not null|

### AlatResep
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idResep|integer|primary key, foreign key references Resep(idResep)|not null|
|idAlat|integer|primary key, foreign key references Alat(idAlat)|not null|

### BahanResep
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idResep|integer|primary key, foreign key references Resep(idResep)|not null|
|idBahan|integer|primary key, foreign key references Bahan(idBahan)|not null|
|kuantitasBahan|real||not null|
|satuanKuantitasBahan|text||not null|

### Komentar
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idKomentar|integer|primary key|autoincrement, not null|
|komentarFoto|blob||not null|
|komentarTeks|text||not null|
|tanggalKomentar|text||not null|
|idResep|integer|foreign key references Resep(idResep)|not null|

### Artikel
|Atribut|Tipe|Key|Constraint|
|-----|----|----|---|
|idArtikel|integer|primary key|autoincrement, not null|
|fotoArtikel|blob||not null|
|judulArtikel|text||not null|
|isiArtikel|text||not null|
|tanggalPublikasi|text||not null|

## Anggota Kelompok dan Pembagian Tugas
|NIM|Nama|Tugas|
|-|-|-|
|13521059|Arleen Chrysantha Gunardi||
|13521127|Marcel Ryan Antony||
|13521143|Raynard Tanadi||
|13521145|Kenneth Dave Bahana||