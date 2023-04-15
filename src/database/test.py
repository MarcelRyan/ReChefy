import database_func
from datetime import datetime
from PIL import Image
import base64
import io
import os

file = r".\src\database\rechefy.db"
connection = database_func.connectToDatabase(file)
database_func.initializeTable(connection)

langkahMemasak = """- Goreng kentang sisihkan.
- Panaskan minyak tumis bahan halus sampai kering dan pecah minyak.
- Masukkan ayam tumis sebentar kemudian masukkan santan dengan air aduk rata.
- Masukkan kerisik, daun jeruk, daun salam, dan daun kunyit.
- Kemudian masukkan kentang dan telur rebus tambahkan garam, gula malaka dan perasa.
- Masak dengan api kecil sampai air kering, jika ingin berkuah jangan masak sampai kering."""

namaMasakan = """Kue Cubit Mini Mangga"""

# gambarMasakan = database_func.imageToBlob(r".\src\database\cubit.jpg")

deskripsiMasakan = """Kue cubit dengan tambahan buah mangga merupakan perpaduan yang menyegarkan sekaligus memberikan rasa manis"""

# connect = connection.cursor()

# connect.execute("UPDATE Resep SET langkahMemasak = ? WHERE idResep = 1;", (langkahMemasak, ))
# connection.commit()

resep = database_func.getResep(connection, 1)
alatresep = database_func.getAlatResep(connection, 1)
bahanresep = database_func.getBahanResep(connection, 1)
path = database_func.resepBlobToImage(connection, 1)

artikel = database_func.getDaftarArtikel(connection)
pathartikel = database_func.artikelBlobToImage(connection, 3)

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
