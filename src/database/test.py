import database_func
from PIL import Image
import base64
import io
import os

file = r".\src\database\rechefy.db"
# print(file)
connection = database_func.connectToDatabase(file)
database_func.initializeTable(connection)

langkahMemasak = """1. Lelehkan mentega lalu sisihkan. Kemudian campur susu dan mangga lalu blender
2. Masukkan telur dalam mangkuk, tambahkan gula dan kocok sampai mengembang
3. Campurkan baking soda, baking powder, vanili bubuk ke dalam terigu
4. Masukkan semua mangga yang sudah diblender, lalu aduk rata
5. Tambahkan mentega cair setengahnya dulu dan aduk kembali
6. Ayak terigu dan masukkan dalam adonan aduk rata, kemudian tambahkan sisa mentega cair
7. Taruh adonan di dalam gelas takar
8. Panaskan loyang kue cubit, olesi minyak goreng dan tuang adonan. Setelah keluar gelembung kecil taruh topping sesuai selera. Jika permukaan sudah berwarna cokelat bisa langsung diangkat."""

namaMasakan = """Kue Cubit Mini Mangga"""

gambarMasakan = database_func.imageToBlob(r".\src\database\cubit.jpg")

deskripsiMasakan = """Kue cubit dengan tambahan buah mangga merupakan perpaduan yang menyegarkan sekaligus memberikan rasa manis"""

# Bagian tambah resep
# database_func.addResep(connection, namaMasakan, deskripsiMasakan, gambarMasakan, langkahMemasak)

# Bagian tambah bahan (WARNING TAMBAH BAHAN YANG BELUM ADA DI DATABASE SAJA)
# database_func.addBahan(connection, "Baking Soda")
# database_func.addBahan(connection, "Potongan Mangga")
# database_func.addBahan(connection, "Tepung Maizena")
# database_func.addBahan(connection, "Vanilla Bubuk")
# database_func.addBahan(connection, "Bawang Putih Bubuk")
# database_func.addBahan(connection, "Kulit Pangsit")
# database_func.addBahan(connection, "Minyak Wijen")

# Bagian tambah bahanresep
# database_func.addBahanResep(connection, 17, 2, 2, "butir")
# database_func.addBahanResep(connection, 17, 56, 45, "gram")
# database_func.addBahanResep(connection, 17, 43, 130, "gram")
# database_func.addBahanResep(connection, 17, 42, 100, "gram")
# database_func.addBahanResep(connection, 17, 89, 2.5, "gram")
# database_func.addBahanResep(connection, 17, 46, 5, "gram")
# database_func.addBahanResep(connection, 17, 88, 2.5, "gram")
# database_func.addBahanResep(connection, 17, 47, 100, "ml")
# database_func.addBahanResep(connection, 17, 90, 100, "gram")
# database_func.addBahanResep(connection, 17, 83, 12, "lembar")
# database_func.addBahanResep(connection, 17, 24, 1, "sdt")
# database_func.addBahanResep(connection, 15, 84, 1, "sdt")
# database_func.addBahanResep(connection, 15, 72, 1, "sdt")
# database_func.addBahanResep(connection, 15, 8, 1, "sdt")
# database_func.addBahanResep(connection, 10, 40, 5, "gram")

# Bagian tambah alat (WARNING TAMBAH ALAT YANG BELUM ADA DI DATABASE AJA)
# database_func.addAlat(connection, "Sendok Makan")
# database_func.addAlat(connection, "Sendok Teh")
# database_func.addAlat(connection, "Loyang")
# database_func.addAlat(connection, "Timbangan Dapur")
# database_func.addAlat(connection, "Oven")


# Bagian tambah alatresep
# database_func.addAlatResep(connection, 17, 1)
# database_func.addAlatResep(connection, 17, 2)
# database_func.addAlatResep(connection, 17, 3)
# database_func.addAlatResep(connection, 17, 4)
# database_func.addAlatResep(connection, 17, 5)
# database_func.addAlatResep(connection, 17, 6)
# database_func.addAlatResep(connection, 17, 9)
# database_func.addAlatResep(connection, 17, 8)
# database_func.addAlatResep(connection, 17, 7)
# database_func.addAlatResep(connection, 17, 11)
# database_func.addAlatResep(connection, 17, 25)
# database_func.addAlatResep(connection, 17, 26)
# database_func.addAlatResep(connection, 17, 18)
# database_func.addAlatResep(connection, 17, 19)
# database_func.addAlatResep(connection, 17, 10)
