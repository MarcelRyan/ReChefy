import database_func
from PIL import Image
import base64
import io
import os

file = r".\src\database\rechefy.db"
# print(file)
connection = database_func.connectToDatabase(file)
database_func.initializeTable(connection)

langkahMemasak = """1. Campurkan daging kepiting, daun bawang, bawang putih, seledri, wortel, susu cair, keju, tapioka, dan telur (sisakan sedikit sebagai bahan oles).
2. Tambahkan saus tiram, kecap asin, minyak wijen, dan gula, aduk hingga merata.
3. Ambil satu lembar kulit pangsit. Kemudian, oles pinggiran kulit pangsit dengan putih telur. Taruh adonan crab rangoon di atasnya.
4. Lekatkan pinggiran kulit pangsit satu sama lain agar menempel dan adonan tidak keluar.
5. Panaskan minyak di atas wajan. Masukkan pangsit berisi adonan crab rangoon lalu goreng hingga matang dan berubah warna keemasan. Angkat lalu tiriskan.
6. Sajikan crab rangoon bersama saus atau mayonaise sesuai selera kamu."""

namaMasakan = """Brown Sugar Chocochips Cookies"""

# gambarMasakan = database_func.imageToBlob(r".\src\database\crab.jpg")

deskripsiMasakan = """Rasanya yang crunchy dan gurih cocok banget untuk nemenin kamu nonton film favorit sambil nyemil santai. Bahan utama dari crab rangoon ini tentu kepiting. Namun, kalau kamu sulit mendapat kepiting, kamu bisa ganti dengan bahan yang lebih simple dan mudah ditemukan yaitu crab stick. Penasaran resepnya? Ini dia!"""

# Bagian tambah resep
# database_func.addResep(connection, namaMasakan, deskripsiMasakan, gambarMasakan, langkahMemasak)

# Bagian tambah bahan (WARNING TAMBAH BAHAN YANG BELUM ADA DI DATABASE SAJA)
# database_func.addBahan(connection, "Daging Kepiting")
# database_func.addBahan(connection, "Seledri")
# database_func.addBahan(connection, "Wortel Parut")
# database_func.addBahan(connection, "Keju Parut")
# database_func.addBahan(connection, "Bawang Putih Bubuk")
# database_func.addBahan(connection, "Kulit Pangsit")
# database_func.addBahan(connection, "Minyak Wijen")

# Bagian tambah bahanresep
# database_func.addBahanResep(connection, 15, 78, 100, "gram")
# database_func.addBahanResep(connection, 15, 28, 0.5, "batang")
# database_func.addBahanResep(connection, 15, 79, 1, "lembar")
# database_func.addBahanResep(connection, 15, 80, 50, "gram")
# database_func.addBahanResep(connection, 15, 81, 30, "gram")
# database_func.addBahanResep(connection, 15, 82, 0.5, "sdm")
# database_func.addBahanResep(connection, 15, 2, 1, "butir")
# database_func.addBahanResep(connection, 15, 47, 3, "sdm")
# database_func.addBahanResep(connection, 15, 52, 2, "sdm")
# database_func.addBahanResep(connection, 15, 83, 12, "lembar")
# database_func.addBahanResep(connection, 15, 24, 1, "sdt")
# database_func.addBahanResep(connection, 15, 84, 1, "sdt")
# database_func.addBahanResep(connection, 15, 72, 1, "sdt")
# database_func.addBahanResep(connection, 15, 8, 1, "sdt")
# database_func.addBahanResep(connection, 10, 40, 5, "gram")

# Bagian tambah alat (WARNING TAMBAH ALAT YANG BELUM ADA DI DATABASE AJA)


# Bagian tambah alatresep
# database_func.addAlatResep(connection, 15, 1)
# database_func.addAlatResep(connection, 15, 2)
# database_func.addAlatResep(connection, 15, 3)
# database_func.addAlatResep(connection, 15, 4)
# database_func.addAlatResep(connection, 15, 5)
# database_func.addAlatResep(connection, 15, 6)
# database_func.addAlatResep(connection, 15, 9)
# database_func.addAlatResep(connection, 15, 8)
# database_func.addAlatResep(connection, 15, 7)
# database_func.addAlatResep(connection, 15, 11)
# database_func.addAlatResep(connection, 15, 10)
# database_func.addAlatResep(connection, 15, 14)
# database_func.addAlatResep(connection, 15, 16)
# database_func.addAlatResep(connection, 15, 17)
