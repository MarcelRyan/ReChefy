import database_func
from PIL import Image
import base64
import io
import os

file = r".\src\database\rechefy.db"
# print(file)
connection = database_func.connectToDatabase(file)
database_func.initializeTable(connection)

langkahMemasak = """1. Lelehkan coklat dan mentega dengan cara ditim
2. Kocok telur dan gula dengan mixer, nggak perlu sampai mengembang cukup sampai tercampur rata. Lalu masukkan cokelat yang sudah dilelehkan tadi dalam telur. Aduk-aduk tanpa mixer sampai rata
3. Masukkan tepung, cokelat bubuk, baking powder, milo sambil diayak dengan saringan. Aduk
4. Agar adonan tidak terlalu kental, tambahkan susu cair sampai adonan agak encer. Tambahkan sejumput garam dan aduk lagi
5. Siapkan cetakan kue balok. Panaskan terlebih dahulu di atas kompor dengan api kecil, setelah panas oleskan mentega, masukkan bahan ke loyang
6. Tutup dan tunggu sampai matang sekitar 5 menit, angkat dan sajikan."""

namaMasakan = """Kue Balok"""

# gambarMasakan = database_func.imageToBlob(r".\src\database\kuebalok.jpg")

deskripsiMasakan = """Para penjajah Belanda yang tinggal di Indonesia, khususnya di kawasan Bandung sangat suka makan kue dan roti. Masuknya tepung terigu ke Indonesia membuat dua makanan ini mudah diolah.

Kue balok jadi makanan sehari-hari warga Belanda. Resep kue padat ini lambat laun diketahui warga Bandung yang mulai mencoba membuat kue balok.

Ternyata kue ini disukai banyak orang dan dipilih sebagai menu sarapan. Teksturnya yang padat membuat cepat kenyang sehingga popularitas kue balok mengalahkan roti pada saat itu."""

# Bagian tambah resep
# database_func.addResep(connection, namaMasakan, deskripsiMasakan, gambarMasakan, langkahMemasak)

# Bagian tambah bahan (WARNING TAMBAH BAHAN YANG BELUM ADA DI DATABASE SAJA)
# database_func.addBahan(connection, "Dark Chocolate")
# database_func.addBahan(connection, "Mentega")
# database_func.addBahan(connection, "Tepung Terigu")
# database_func.addBahan(connection, "Dark Chocolate Bubuk")
# database_func.addBahan(connection, "Sachet Milo")
# database_func.addBahan(connection, "Baking Powder")
# database_func.addBahan(connection, "Susu")

# Bagian tambah bahanresep
# database_func.addBahanResep(connection, 7, 41, 150, "gram")
# database_func.addBahanResep(connection, 7, 42, 75, "gram")
# database_func.addBahanResep(connection, 7, 2, 3, "butir")
# database_func.addBahanResep(connection, 7, 8, 45, "gram")
# database_func.addBahanResep(connection, 7, 43, 150, "gram")
# database_func.addBahanResep(connection, 7, 44, 1.5, "sdm")
# database_func.addBahanResep(connection, 7, 45, 2, "bungkus")
# database_func.addBahanResep(connection, 7, 46, 1.5, "sdt")
# database_func.addBahanResep(connection, 7, 47, 250, "ml")
# database_func.addBahanResep(connection, 7, 9, 1, "jumput")

# Bagian tambah alat (WARNING TAMBAH ALAT YANG BELUM ADA DI DATABASE AJA)


# Bagian tambah alatresep
# database_func.addAlatResep(connection, 7, 1)
# database_func.addAlatResep(connection, 7, 2)
# database_func.addAlatResep(connection, 7, 3)
# database_func.addAlatResep(connection, 7, 4)
# database_func.addAlatResep(connection, 7, 5)
# database_func.addAlatResep(connection, 7, 6)
# database_func.addAlatResep(connection, 7, 9)
# database_func.addAlatResep(connection, 7, 8)
# database_func.addAlatResep(connection, 7, 7)
# database_func.addAlatResep(connection, 7, 11)
# database_func.addAlatResep(connection, 7, 10)
# database_func.addAlatResep(connection, 7, 14)
# database_func.addAlatResep(connection, 7, 16)
# database_func.addAlatResep(connection, 7, 17)
