import database_func
from PIL import Image
import base64
import io
import os

file = r".\src\database\rechefy.db"
# print(file)
connection = database_func.connectToDatabase(file)
database_func.initializeTable(connection)

langkahMemasak = """1. Isi tumis bawang putih dan sampai harum. Tambahkan daging. Aduk hingga matang dan berbulir bulir, angkat
2. Aduk tumisan daging, daun bawang, telur, garam, dan merica bubuk
3. Ambil selembar kulit lumpia. Sendokkan bahan isi, lipat seperti amplop, rekatkan dengan telur
4. Panaskan minyak dalam wajan datar. Masukkan martabak. Goreng sampai matang sambil disiram minyak."""

namaMasakan = """Martabak Telur"""

gambarMasakan = database_func.imageToBlob(r".\src\database\martabak.jpg")

deskripsiMasakan = """Martabak telur merupakan panganan dengan rasa gurih. Sayur, daging, dan berbagai bumbu lainnya digabung menjadi satu dalam sebuah kulit adonan padat yang ditipiskan secukupnya, kemudian dilipat, kemudian digoreng hingga matang. Panganan ini cukup digemari di Indonesia dan banyak dijual mulai dari tempat makan hingga di gerobak pinggir jalan."""

# Bagian tambah resep
# database_func.addResep(connection, namaMasakan, deskripsiMasakan, gambarMasakan, langkahMemasak)

# Bagian tambah bahan
# database_func.addBahan(connection, "Kulit Lumpia")
# database_func.addBahan(connection, "Daging Giling")
# database_func.addBahan(connection, "Telur Ayam")
# database_func.addBahan(connection, "Merica")
# database_func.addBahan(connection, "Royco")
# database_func.addBahan(connection, "Margarin")
# database_func.addBahan(connection, "Ketumbar")

# Bagian tambah bahanresep
# database_func.addBahanResep(connection, 6, 37, 10, "buah")
# database_func.addBahanResep(connection, 6, 38, 200, "gram")
# database_func.addBahanResep(connection, 6, 13, 3, "siung")
# database_func.addBahanResep(connection, 6, 28, 200, "gram")
# database_func.addBahanResep(connection, 6, 39, 3, "butir")
# database_func.addBahanResep(connection, 6, 40, 0.5, "sdt")
# database_func.addBahanResep(connection, 6, 9, 1.25, "sdt")
# database_func.addBahanResep(connection, 5, 36, 2, "batang")

# Bagian tambah alat


# Bagian tambah alatresep
# database_func.addAlatResep(connection, 6, 1)
# database_func.addAlatResep(connection, 6, 2)
# database_func.addAlatResep(connection, 6, 3)
# database_func.addAlatResep(connection, 6, 4)
# database_func.addAlatResep(connection, 6, 5)
# database_func.addAlatResep(connection, 6, 6)
# database_func.addAlatResep(connection, 6, 9)
# database_func.addAlatResep(connection, 6, 8)
# database_func.addAlatResep(connection, 6, 16)
# database_func.addAlatResep(connection, 6, 17)
