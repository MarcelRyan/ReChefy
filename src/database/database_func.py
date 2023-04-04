import sqlite3
from sqlite3 import Error
import base64
from datetime import datetime, date

# Function to connect to the database file
def connectToDatabase(databaseFile):
    try:
        connection = sqlite3.connect(databaseFile)
        return connection
    except Error as e:
        print(e)
    
    return None

# Function to initialize all tables for the databases
def initializeTable(connection):
    create_table_resep = """CREATE TABLE IF NOT EXISTS Resep (
                            idResep INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            gambarMasakan BLOB NOT NULL,
                            namaMasakan VARCHAR(100) NOT NULL,
                            deskripsiMasakan VARCHAR(10000) NOT NULL,
                            langkahMemasak VARCHAR(20000) NOT NULL
                        ); """
    
    create_table_bahan = """CREATE TABLE IF NOT EXISTS Bahan (
                            idBahan INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            namaBahan VARCHAR(100) NOT NULL
                        ); """
    
    create_table_alat = """CREATE TABLE IF NOT EXISTS Alat (
                            idAlat INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            namaAlat VARCHAR(100) NOT NULL
                        ); """
    
    create_table_alatresep = """CREATE TABLE IF NOT EXISTS AlatResep (
                                idResep INTEGER NOT NULL,
                                idAlat INTEGER NOT NULL,
                                PRIMARY KEY (idResep, idAlat),
                                FOREIGN KEY (idResep) REFERENCES Resep(idResep),
                                FOREIGN KEY (idAlat) REFERENCES Alat(idAlat)
                            );"""
    
    create_table_bahanresep = """CREATE TABLE IF NOT EXISTS BahanResep (
                                idResep INTEGER NOT NULL,
                                idBahan INTEGER NOT NULL,
                                kuantitasBahan INTEGER NOT NULL,
                                satuanKuantitasBahan VARCHAR(20) NOT NULL,
                                PRIMARY KEY (idResep, idBahan),
                                FOREIGN KEY (idResep) REFERENCES Resep(idResep),
                                FOREIGN KEY (idBahan) REFERENCES Bahan(idBahan)
                            );"""
    
    create_table_komentar = """CREATE TABLE IF NOT EXISTS Komentar (
                            idKomentar INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            komentarFoto BLOB NOT NULL,
                            komentarTeks VARCHAR(1000) NOT NULL,
                            tanggalKomentar DATETIME NOT NULL,
                            idResep INTEGER NOT NULL,
                            FOREIGN KEY (idResep) REFERENCES Resep(idResep)
                            ); """
    
    create_table_artikel = """CREATE TABLE IF NOT EXISTS Artikel (
                            idArtikel INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            fotoArtikel BLOB NOT NULL,
                            judulArtikel VARCHAR(1000) NOT NULL,
                            isiArtikel VARCHAR(100000) NOT NULL,
                            tanggalPublikasi DATETIME NOT NULL
                        ); """
    
    # Execute all commands above
    try: 
        connect = connection.cursor()
        connect.execute(create_table_resep)
        connect.execute(create_table_alat)
        connect.execute(create_table_bahan)
        connect.execute(create_table_alatresep)
        connect.execute(create_table_bahanresep)
        connect.execute(create_table_komentar)
        connect.execute(create_table_artikel)
    except Error as e:
        print(e)

# Function to change image to BLOB 
def imageToBlob(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

# Function to convert string to datetime format
def stringToDatetime(date):
    return datetime.strptime(date, "%Y-%m-%d")

# Function to add rows or tuple to Resep table
def addResep(connection, nama_masakan, deskripsi_masakan, gambar_masakan, langkah_memasak):
    add_new_resep = """INSERT INTO Resep (gambarMasakan, namaMasakan, deskripsiMasakan, langkahMemasak) VALUES (?, ?, ?, ?);"""
    connect = connection.cursor()
    connect.execute(add_new_resep, (gambar_masakan, nama_masakan, deskripsi_masakan, langkah_memasak))
    connection.commit()

# Function to add rows or tuple to Alat table
def addAlat(connection, nama_alat):
    add_new_alat = """INSERT INTO Alat (namaAlat) VALUES (?);"""
    connect = connection.cursor()
    connect.execute(add_new_alat, (nama_alat))
    connection.commit()

# Function to add rows or tuple to Bahan table
def addBahan(connection, nama_bahan):
    add_new_bahan = """INSERT INTO Bahan (namaBahan) VALUES (?);"""
    connect = connection.cursor()
    connect.execute(add_new_bahan, (nama_bahan))
    connection.commit()

# Function to add rows or tuple to AlatResep table
def addAlatResep(connection, id_alat, id_resep):
    add_new_alatresep = """INSERT INTO AlatResep (idResep, idAlat) VALUES (?, ?);"""
    connect = connection.cursor()
    connect.execute(add_new_alatresep, (id_resep, id_alat))
    connection.commit()

# Function to add rows or tuple to BahanResep table
def addAlatResep(connection, id_bahan, id_resep, kuantitas_bahan, satuan_kuantitas_bahan):
    add_new_bahanresep = """INSERT INTO BahanResep (idResep, idBahan, kuantitasBahan, satuanKuantitasBahan) VALUES (?, ?, ?, ?);"""
    connect = connection.cursor()
    connect.execute(add_new_bahanresep, (id_resep, id_bahan, kuantitas_bahan, satuan_kuantitas_bahan))
    connection.commit()

# Function to add rows or tuple to Komentar table
def addKomentar(connection, komentar_foto, komentar_teks, id_resep):
    add_new_komentar = """INSERT INTO Komentar (komentarFoto, komentarTeks, tanggalKomentar, idResep) VALUES (?, ?, ?, ?)"""
    connect = connection.cursor()
    connect.execute(add_new_komentar, (komentar_foto, komentar_teks, date.today(), id_resep))
    connection.commit()

# Function to add rows or tuple to Artikel table
def addArtikel(connection, foto_artikel, judul_artikel, isi_artikel, tanggal_publikasi):
    add_new_artikel = """INSERT INTO Artikel (fotoArtikel, judulArtikel, isiArtikel, tanggalPublikasi)"""
    connect = connection.cursor()
    connect.execute(add_new_artikel, (foto_artikel, judul_artikel, isi_artikel, tanggal_publikasi))
    connection.commit()

# Function to create view for every data in Resep
def daftarResepView(connection):
    connect = connection.cursor()
    connect.execute("DROP VIEW IF EXISTS DaftarResepView")
    connect.execute("SELECT gambarMasakan, namaMasakan, deskripsiMasakan, langkahMemasak FROM Resep")
    data = connect.fetchall()
    return data

# Function to create view for data with idResep = resep_id in Resep, Alat, and Bahan table
def resepView(connection, resep_id):
    connect = connection.cursor()
    connect.execute("DROP VIEW IF EXISTS ResepView")

    query = """SELECT gambarMasakan, namaMasakan, deskripsiMasakan, langkahMemasak, namaAlat, namaBahan, kuantitasBahan, satuanKuantitasBahan
               FROM Resep
               NATURAL JOIN Alat
               NATURAL JOIN Bahan
               WHERE idResep = ?"""
    
    connect.execute(query, (resep_id))
    data = connect.fetchall()
    return data

# Function to create view for every data in Artikel table
def daftarArtikelView(connection):
    connect = connection.cursor()
    connect.execute("DROP VIEW IF EXISTS DaftarArtikelView")
    connect.execute("SELECT fotoArtikel, judulArtikel, isiArtikel, tanggalPublikasi FROM Artikel")
    data = connect.fetchall()
    return data

# Function to create view for data with idArtikel = artikel_id in Artikel table
def artikelView(connection, artikel_id):
    connect = connection.cursor()
    connect.execute("DROP VIEW IF EXISTS ArtikelView")
    connect.execute("SELECT fotoArtikel, judulArtikel, isiArtikel, tanggalPublikasi FROM Artikel WHERE idArtikel = ?", (artikel_id))
    data = connect.fetchone()
    return data

# Function to create view for every data with idResep = resep_id in Komentar table
def komentarView(connection, resep_id):
    connect = connection.cursor()
    connect.execute("DROP VIEW IF EXISTS KomentarView")
    connect.execute("SELECT komentarFoto, komentarTeks, tanggalKomentar FROM KOMENTAR WHERE idResep = ?", (resep_id))
    data = connect.fetchall()
    return data

# Function to create view for every data with namaResep contains keyword substring in Resep table
def searchResepView(connection, keyword):
    connect = connection.cursor()
    connect.execute("DROP VIEW IF EXISTS SearchResepView")
    connect.execute("SELECT gambarMasakan, namaMasakan, deskripsiMasakan, langkahMemasak FROM Resep WHERE namaMasakan LIKE '%?%'", (keyword))
    data = connect.fetchall()
    return data

# Function to delete tuples from AlatResep table
def deleteAlatResep(connection, resep_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM AlatResep WHERE idResep = ?", (resep_id))
    connect.commit()

# Function to delete tuples from BahanResep table
def deleteBahanResep(connection, resep_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM BahanResep WHERE idResep = ?", (resep_id))
    connect.commit()

# Function to delete a tuple from Resep table
def deleteResep(connection, resep_id):
    connect = connection.cursor()
    deleteAlatResep(connection, resep_id)
    deleteBahanResep(connection, resep_id)
    connect.execute("DELETE FROM Resep WHERE idResep = ?", (resep_id))
    connect.commit()

# Function to delete a tuple from Komentar table
def deleteKomentar(connection, komentar_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM Komentar WHERE idKomentar = ?", (komentar_id))
    connect.commit()

# Function to update a tuple in Resep table
def editResep(connection, resep_id, gambar_masakan, nama_masakan, deskripsi_masakan, langkah_memasak):
    connect = connection.cursor()
    connect.execute("UPDATE Resep SET gambarMasakan = ?, namaMasakan = ?, deskripsiMasakan = ?, langkahMemasak = ? WHERE idResep = ?", (gambar_masakan, nama_masakan, deskripsi_masakan, langkah_memasak, resep_id))
    connect.commit()




