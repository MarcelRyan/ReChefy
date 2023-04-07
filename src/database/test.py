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

isiArtikel = """Jagung merupakan salah satu bahan makanan yang digemari berbagai kalangan. Selain rasanya yang lezat dan mengenyangkan, jagung mudah diolah menjadi berbagai macam makanan mulai dari camilan, kudapan hingga lauk. Salah satu olahan jagung yang paling banyak digemari adalah jagung rebus. Apalagi kalau jajan jagung rebus di abang-abang keliling, baunya saja sudah nikmat menggoda~

Meski sangat mudah dibanding olahan jagung lainnya, tapi masih banyak yang belum bisa menghasilkan jagung rebus yang empuk, manis, dan harum. Bahkan sering kali jagung berubah mengkerut setelah direbus. Selain itu, masih banyak yang merebus jagung terlalu lama supaya empuk, padahal bisa merusak kandungan gizinya. Nah, supaya menghasilkan jagung yang matang sempurna dan gizinya tetap terjaga, berikut ini Hipwee Tips bagikan cara merebus jagung manis yang tepat. Yuk, simak!

Sebelum merebus jagung, kamu harus memastikan jagungmu benar-benar manis dan empuk setelah direbus. Caranya, pilih jagung yang benar-benar segar. Jika kamu membeli jagung kupas, maka pilih yang bijinya masih kencang alias belum keriput, dan warnanya masih kuning keruh dan segar. Jagung yang berwarna kuning keputih-putihan biasanya kurang manis jika direbus, karena kandungan patinya cukup tinggi.

Jika kamu membeli jagung yang masih ada kulitnya, maka pilih yang kulit dan rambutnya masih segar. Jagung segar biasanya tetap enak dikonsumsi sampai 3 hari setelah dipanen jika disimpan di suhu ruang dan 7 hari di dalam kulkas. Semakin segar, maka semakin cepat empuk saat direbus, rasanya juga lebih manis dan aromanya lebih harum.

Setelah memilih jagung yang bagus, kamu bisa mengupas seluruh kulitnya jika ingin lebih cepat empuk. Cara merebus jagung ini cukup mudah, tinggal rebus air hingga mendidih, kemudian tambahkan 1 sendok makan garam dan aduk hingga larut. Penambahan garam disesuaikan dengan air dan jagungnya ya, nggak perlu asin tapi penambahan garam ini bertujuan untuk mempercepat perebusan dan menambah cita rasa.

Setelah itu, masukkan jagung yang sudah dikupas ke dalam panci. Usahakan semuanya terendam air. Nah, jika ukuran jagung terlalu besar, maka bisa dipotong sesuai selera. Kemudian, tutup panci dan tunggu 5-10 menit. Tanda jagung sudah matang biasanya warnanya berubah dari kuning keruh menjadi kuning terang, jadi nggak perlu menunggu bijinya terkelupas sendiri ya, karena bisa merusak kandungan gizinya.

Jika kamu ingin membuat jagung rebus rumahan tapi memiliki aroma khas seperti yang dijual abang-abang keliling, maka kamu bisa menambahkan beberapa lembar kulit jagung pada air rebusan. Kulit jagung yang direbus memang bisa menghasilkan aroma khas yang tentunya bisa menambah kenikmatan jagung. Selain kulit jagung, kamu juga bisa menambahkan beberapa lembar daun salam supaya makin lezat dan aromanya makin nikmat. Ini nih, yang jadi rahasia jagung rebus di abang-abang jualan~

Buat kamu yang hobi jajan jagung rebus, karena rasanya cukup beda jika merebus sendiri di rumah, maka coba nih cara merebus jagung yang benar. Merebus jagung tanpa mengupas kulitnya memang terasa lebih nikmat, tapi kamu harus rela merebusnya lebih lama. Kulit jangung memiliki pori-pori yang cukup kecil dan tahan air. Mesti tanpa mengupas kulit, usahakan buka 2-3 lembar kulit terluar dan beri sedikit lubang seperempat bagian jagung atau sayatan memanjang.

Sebelum merebus jagung tanpa mengupas kulitnya, pastikan sudah dicuci bersih, ya. Kemudian dimasukkan ke dalam panci yang sudah berisi air mendidih dan diberi garam serta daun  salam. Pastikan semuanya terendam air, lalu tutup rapat. Rebus jagung selama 15-30 menit. Semakin segar jagung, otomatis semakin cepat matang. Tanda jagung sudah matang, kulitnya layu dan bijinya berwarna kuning terang.

Satu lagi rahasia jagung rebus keliling yang bisa kamu coba di rumah. Beberapa penjual jagung rebus menyiasati aroma dan rasa jagung rebusannya dengan air kelapa. Ya, supaya rasanya lebih manis dan aromanya lebih kuat, jagung direbus dengan air kelapa. Caranya pun cukup mudah, kamu bisa menggunakan air kelapa murni, atau hanya sebagai campuran air biasa dengan perbandingan 1:1. Proses lainnya tetap sama, hanya airnya saja yang diganti.

Salah satu tantangan merebus jagung selain waktu perebusan yang tepat adalah hasilnya rebusan yang kurang bagus. Biasanya jagung rebus akan menyusut sehingga membuat bijinya jadi keriput. Hal ini karena jagung kurang segar atau sudah lebih dari 3 hari. Untuk menyiasati hal ini, selain memilih jagung yang bagus, kamu juga bisa merendam jagung lebih dulu setelah direbus.

Cara merebus jagung memang terlihat simpel dan mudah, tapi perlu diingat juga jika merebus jagung terlalu lama bisa merusak kandungan gizinya. Maka dari itu, penting untuk memilih jagung yang masih segar sehingga proses perebusan cukup 5-10 menit saja. Selain itu, pastikan panci tertutup rapat supaya panasnya bisa maksimal. Ciri-ciri jagung overcook hingga kandungan gizinya rusak biasanya bijinya sangat lunak sehingga saat diangkat jadi mudah hancur. Gimana, bisa nggak buat jagung rebus yang manis, aromanya harum dan gizinya tetap oke? Selamat mencoba!
"""

judulArtikel = """6 Cara Merebus Jagung Manis Biar Empuk"""

tanggalPublikasi = database_func.stringToDatetime("2023-03-30")

gambarArtikel = database_func.imageToBlob(r".\src\database\jagung.jpg")

database_func.addArtikel(connection, gambarArtikel, judulArtikel, isiArtikel, tanggalPublikasi)

