import database_func
from PIL import Image
import base64
import io
import os

file = r".\src\database\rechefy.db"
# print(file)
connection = database_func.connectToDatabase(file)
database_func.initializeTable(connection)

# print(database_func.imageToBlob("tes.jpg"))

# lihat = Image.open(io.BytesIO(database_func.imageToBlob("tes.jpg")))
# lihat.show()

langkahMemasak = """- Goreng kentang sisihkan.
                    - Panaskan minyak tumis bahan halus sampai kering dan pecah minyak.
                    - Masukkan ayam tumis sebentar kemudian masukkan santan dengan air aduk rata.
                    - Masukkan kerisik, daun jeruk, daun salam, dan daun kunyit.
                    - Kemudian masukkan kentang dan telur rebus tambahkan garam, gula malaka dan perasa.
                    - Masak dengan api kecil sampai air kering, jika ingin berkuah jangan masak sampai kering"""

namaMasakan = """ Rendang paha ayam """
# gambarMasakan = database_func.imageToBlob("rendangayam.jpg")

deskripsiMasakan = """ Rendang ayam yang dibuat dengan resep khas dan cinta :) """

connect = connection.cursor()



