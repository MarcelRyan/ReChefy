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
    add_new_komentar = """INSERT INTO Komentar (komentarFoto, komentarTeks, tanggalKomentar, idResep) VALUES (?, ?, ?, ?);"""
    connect = connection.cursor()
    connect.execute(add_new_komentar, (komentar_foto, komentar_teks, date.today(), id_resep))
    connection.commit()

# Function to add rows or tuple to Artikel table
def addArtikel(connection, foto_artikel, judul_artikel, isi_artikel, tanggal_publikasi):
    add_new_artikel = """INSERT INTO Artikel (fotoArtikel, judulArtikel, isiArtikel, tanggalPublikasi) VALUES (?, ?, ?, ?);"""
    connect = connection.cursor()
    connect.execute(add_new_artikel, (foto_artikel, judul_artikel, isi_artikel, tanggal_publikasi))
    connection.commit()

# Function to get every data in Resep
def getDaftarResep(connection):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Resep;")
    data = connect.fetchall()
    return data

# Function to get data with idResep = resep_id in Resep, Alat, and Bahan table
def getResep(connection, resep_id):
    connect = connection.cursor()

    query = """SELECT *
               FROM Resep
               NATURAL JOIN Alat
               NATURAL JOIN Bahan
               WHERE idResep = ?;"""
    
    connect.execute(query, (resep_id))
    data = connect.fetchall()
    return data

# Function to get every data in Artikel table
def getDaftarArtikel(connection):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Artikel;")
    data = connect.fetchall()
    return data

# Function to get data with idArtikel = artikel_id in Artikel table
def getArtikel(connection, artikel_id):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Artikel WHERE idArtikel = ?;", (artikel_id))
    data = connect.fetchone()
    return data

# Function to get every data with idResep = resep_id in Komentar table
def getKomentar(connection, resep_id):
    connect = connection.cursor()
    connect.execute("SELECT * FROM KOMENTAR WHERE idResep = ?;", (resep_id))
    data = connect.fetchall()
    return data

# Function to get data where namaAlat = alat_name in Alat table
def getIdAlat(connection, alat_name):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Alat WHERE namaAlat = ?;", (alat_name))
    data = connect.fetchone()
    return data

# Function to get data where namaBahan = bahan_name in Bahan table
def getIdBahan(connection, bahan_name):
    connect = connection.cursor()
    connect.execute("SELECT * FROM Bahan WHERE namaBahan = ?;", (bahan_name))
    data = connect.fetchone()
    return data

# Function to create view for every data with namaResep contains keyword substring in Resep table
def searchResepView(connection, keyword):
    connect = connection.cursor()
    connect.execute("DROP VIEW IF EXISTS SearchResepView;")
    connect.execute("CREATE VIEW SearchResepView AS SELECT * FROM Resep WHERE namaMasakan LIKE '%?%';", (keyword))
    data = connect.fetchall()
    connection.commit()
    return data

# Function to create a dummy view for AlatResep table so that data will only be deleted in the database if user confirm their action
def alatResepView(connection):
    connect = connection.cursor()
    connect.execute("DROP VIEW IF EXISTS AlatResepView;")
    connect.execute("CREATE VIEW AlatResepView AS SELECT * FROM AlatResep;")
    data = connect.fetchall()
    connection.commit()
    return data

# Function to create a dummy for BahanResep table view so that data will only be deleted in the database if user confirm their action
def bahanResepView(connection):
    connect = connection.cursor()
    connect.execute("DROP VIEW IF EXISTS BahanResepView;")
    connect.execute("CREATE BahanResepView AS SELECT * FROM BahanResep;")
    data = connect.fetchall()
    connection.commit()
    return data

# Function to delete data with idAlat = alat_id from AlatResepView
def deleteAlatResepView(connection, alat_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM AlatResepView WHERE idAlat = ?;", (alat_id))
    connection.commit()

# Function to delete data with idBahan = bahan_id from BahanResepView
def deleteAlatResepView(connection, bahan_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM BahanResepView WHERE idBahan = ?;", (bahan_id))
    connection.commit()

# Function to insert data into AlatResepView
def addAlatResepView(connection, resep_id, alat_id):
    connect = connection.cursor()
    connect.execute("INSERT INTO AlatResepView (idResep, idAlat) VALUES (?, ?)", (resep_id, alat_id))
    connection.commit()

# Function to insert data into AlatResepView
def addBahanResepView(connection, resep_id, bahan_id):
    connect = connection.cursor()
    connect.execute("INSERT INTO BahanResepView (idResep, idBahan) VALUES (?, ?)", (resep_id, bahan_id))
    connection.commit()

# Function to delete data from AlatResep table if idAlat is not in AlatResepView
def deleteAlatResepDatabase(connection):
    connect = connection.cursor()
    connect.execute("DELETE FROM AlatResep WHERE idAlat NOT IN (SELECT idAlat FROM AlatResepView);")
    connection.commit()

# Function to delete data from BahanResep table if idBahan is not in BahanResepView
def deleteBahanResepDatabase(connection):
    connect = connection.cursor()
    connect.execute("DELETE FROM BahanResep WHERE idBahan NOT IN (SELECT idBahan FROM BahanResepView);")
    connection.commit()

# Function to insert data into AlatResep table if idAlat from AlatResepView is not in AlatResep
def addAlatResepDatabase(connection):
    connect = connection.cursor()
    connect.execute("INSERT INTO AlatResep (idResep, idAlat) SELECT * FROM AlatResepView WHERE idAlat NOT IN (SELECT idAlat FROM AlatResep);") 
    connection.commit()

# Function to insert data into BahanResep table if idBahan from BahanResepView is not in BahanResep
def addBahanResepDatabase(connection):
    connect = connection.cursor()
    connect.execute("INSERT INTO BahanResep (idResep, idBahan) SELECT * FROM BahanResepView WHERE idBahan NOT IN (SELECT idBahan FROM BahanResep);") 
    connection.commit()

# Function to delete tuples from AlatResep table
def deleteAlatResep(connection, resep_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM AlatResep WHERE idResep = ?;", (resep_id))
    connect.commit()

# Function to delete tuples from BahanResep table
def deleteBahanResep(connection, resep_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM BahanResep WHERE idResep = ?;", (resep_id))
    connect.commit()

# Function to delete a tuple from Resep table
def deleteResep(connection, resep_id):
    connect = connection.cursor()
    deleteAlatResep(connection, resep_id)
    deleteBahanResep(connection, resep_id)
    connect.execute("DELETE FROM Resep WHERE idResep = ?;", (resep_id))
    connect.commit()

# Function to delete a tuple from Komentar table
def deleteKomentar(connection, komentar_id):
    connect = connection.cursor()
    connect.execute("DELETE FROM Komentar WHERE idKomentar = ?;", (komentar_id))
    connect.commit()

# Function to update a tuple in Resep table
def editResep(connection, resep_id, gambar_masakan, nama_masakan, deskripsi_masakan, langkah_memasak):
    connect = connection.cursor()
    connect.execute("UPDATE Resep SET gambarMasakan = ?, namaMasakan = ?, deskripsiMasakan = ?, langkahMemasak = ? WHERE idResep = ?;", (gambar_masakan, nama_masakan, deskripsi_masakan, langkah_memasak, resep_id))
    connect.commit()





