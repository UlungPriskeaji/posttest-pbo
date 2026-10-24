from abc import ABC, abstractmethod

# TEMA/JUDUL: Sistem Penjualan dan Inventaris TCG


# superclass KartuTCG (Diubah menjadi Abstract Base Class)
class KartuTCG(ABC):
    total_kartu = 0

    def __init__(self, nama, jenis_tcg, harga, stok):
        self._nama = nama
        self.jenis_tcg = jenis_tcg
        self._harga = harga
        self.__stok = stok

        KartuTCG.total_kartu += 1

    @property
    def nama(self):
        return self._nama

    @property
    def harga(self):
        return self._harga

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            raise ValueError("Stok tidak boleh negatif.")

        self.__stok = stok_baru

    # abstract method 
    @abstractmethod
    def tampilkan_info_kartu(self):
        pass

    @abstractmethod
    def hitung_value_stok(self):
        pass

    # method konkret yang dipakai bersama oleh semua subclass
    def jalankan(self):
        print(f"Menjalankan sistem untuk kartu koleksi: {self._nama}")

    # overloading
    def __add__(self, other):
        if isinstance(other, KartuTCG):
            return self._harga + other._harga
        return NotImplemented


# subclass KartuPokemon & KartuOnePiece
class KartuPokemon(KartuTCG):

    def __init__(self, nama, harga, stok, seri_kartu, kelangkaan):
        super().__init__(nama, "Pokemon", harga, stok)

        # atribut spesifik KartuPokemon
        self.seri_kartu = seri_kartu
        self.kelangkaan = kelangkaan

    # overriding abstract method
    def tampilkan_info_kartu(self):
        print("Nama Kartu: ", self._nama)
        print("Jenis TCG: ", self.jenis_tcg)
        print("Harga: Rp", self._harga)
        print("Stok: ", self.stok)
        print("Seri Kartu: ", self.seri_kartu)
        print("Kelangkaan: ", self.kelangkaan)

    def hitung_value_stok(self):
        return self.harga * self.stok


class KartuOnePiece(KartuTCG):

    def __init__(self, nama, harga, stok, seri_kartu, kelangkaan):
        super().__init__(nama, "One Piece", harga, stok)

        # atribut spesifik KartuOnePiece
        self.seri_kartu = seri_kartu
        self.kelangkaan = kelangkaan

    # overriding abstract method
    def tampilkan_info_kartu(self):
        print("Nama Kartu: ", self._nama)
        print("Jenis TCG: ", self.jenis_tcg)
        print("Harga: Rp", self._harga)
        print("Stok: ", self.stok)
        print("Seri Kartu: ", self.seri_kartu)
        print("Kelangkaan: ", self.kelangkaan)

    def hitung_value_stok(self):
        return self._harga * self.stok


# class Toko (agregasi)
class Toko:
    status_toko = "Buka"

    def __init__(self, nama_toko, alamat_toko):
        self.__nama_toko = nama_toko
        self.alamat_toko = alamat_toko

        # agregasi
        self.daftar_kartu = []

    @property
    def nama_toko(self):
        return self.__nama_toko

    def tambah_kartu(self, kartu):
        self.daftar_kartu.append(kartu)

    def tampilkan_info_toko(self):
        print("Nama Toko: ", self.nama_toko)
        print("Alamat Toko: ", self.alamat_toko)
        print("Status Toko: ", self.status_toko)

    @classmethod
    def ubah_status_toko(cls, status_baru):
        if status_baru not in ["Buka", "Tutup"]:
            raise ValueError("Status Toko Hanya Boleh Buka/Tutup.")

        cls.status_toko = status_baru

    @staticmethod
    def cek_stok(stok):
        if stok > 0:
            return "Stok tersedia"
        else:
            return "Stok habis"


# class Pelanggan
class Pelanggan:
    def __init__(self, nama_pelanggan, id_pelanggan):
        self.nama_pelanggan = nama_pelanggan
        self.id_pelanggan = id_pelanggan

    def tampilkan_info_pelanggan(self):
        print("Nama Pelanggan: ", self.nama_pelanggan)
        print("ID Pelanggan: ", self.id_pelanggan)


# class DetailTransaksi (komposisi)
class DetailTransaksi:
    def __init__(self, kartu, jumlah):
        self.kartu = kartu
        self.jumlah = jumlah


# class Transaksi (asosiasi dan komposisi)
class Transaksi:
    def __init__(self, pelanggan, kartu, jumlah):
        # asosiasi
        self.pelanggan = pelanggan
        self.kartu = kartu

        # komposisi
        self.detail = DetailTransaksi(kartu, jumlah)

    def tampilkan_info_transaksi(self):
        total_harga = self.kartu.harga * self.detail.jumlah

        print("Pelanggan: ", self.pelanggan.nama_pelanggan)
        print("Kartu TCG: ", self.kartu.nama)
        print("Jumlah: ", self.detail.jumlah)
        print("Total Harga: Rp", total_harga)


# class untuk duck typing
class PembayaranQRIS:
    def proses_pembayaran(self, jumlah):
        print("Memproses pembayaran QRIS sebesar Rp", jumlah)


class PembayaranTunai:
    def proses_pembayaran(self, jumlah):
        print("Memproses pembayaran tunai sebesar Rp", jumlah)


def bayar_pesanan(metode, jumlah):
    metode.proses_pembayaran(jumlah)


# main program
print("Sistem Penjualan dan Inventaris TCG")
print("-" * 40)

# bukti abstraksi tidak bisa diinstansiasi
print("\nBukti Abstraksi (TypeError)")
try:
    kartu_salah = KartuTCG("Test", "Dummy", 1000, 10)
except TypeError as e:
    print("Error tertangkap:", e)
    print()
print("-" * 40)

# Data Toko
print("Data Toko")

toko1 = Toko(
    "IlhamGOD TCG Store",
    "Samarinda"
)

toko2 = Toko(
    "IlhamGOD TCG Store BPP",
    "Balikpapan"
)

daftar_toko = [toko1, toko2]

for data_toko in daftar_toko:
    data_toko.tampilkan_info_toko()
print("-" * 40)

# class method
print("Class Method")

Toko.ubah_status_toko("Tutup")

print("Status Toko:", Toko.status_toko)
print("-" * 40)

# static method
print("Static Method")

print("Stok 5:", Toko.cek_stok(5))
print("Stok 0:", Toko.cek_stok(0))
print("-" * 40)

# Data Kartu TCG
print("Data Kartu TCG")

kartu1 = KartuPokemon(
    "Mega Gengar EX (PSA10)",
    12500000,
    5,
    "High Class Pack MEGA Dream ex",
    "Special Art Rare"
)

kartu2 = KartuOnePiece(
    "Monkey D. Luffy",
    80500000,
    1,
    "OP-05",
    "Secret Rare (Manga)"
)

kartu3 = KartuPokemon(
    "Mew - R/RGB",
    88600000,
    2,
    "Pokémon TCG: 30th Celebration",
    "Secret Rare"
)

daftar_kartu = [kartu1, kartu2, kartu3]


# agregasi
toko1.tambah_kartu(kartu1)
toko1.tambah_kartu(kartu2)
toko1.tambah_kartu(kartu3)


# polimorfisme via pewarisan
for kartu in daftar_kartu:
    kartu.jalankan()
    kartu.tampilkan_info_kartu()
    print("Nilai Stok: Rp", kartu.hitung_value_stok())
    print()

print("Total Kartu:", KartuTCG.total_kartu)
print("-" * 40)

# overloading 
print("Operator Overloading (+)")
total_harga_kartu = kartu1 + kartu3
print("Total harga kartu 1 dan 3: Rp", total_harga_kartu)
print("-" * 40)

# property getter
print("Property Getter")

print("Nama Toko:", toko1.nama_toko)

for kartu in daftar_kartu:
    print("Stok", kartu.nama, ":", kartu.stok)
print("-" * 40)

# property setter valid
print("Property Setter Valid")

kartu1.stok = 10

print("Stok Kartu 1 setelah diubah:", kartu1.stok, "(stok)")
print("-" * 40)

# property setter invalid
print("Property Setter Invalid")

try:
    kartu2.stok = -5
except ValueError as e:
    print("Error:", e)
print("-" * 40)

# Data Pelanggan
print("Data Pelanggan")

pelanggan1 = Pelanggan(
    "Herlambang",
    "P001"
)

pelanggan2 = Pelanggan(
    "Joseph",
    "P002"
)

daftar_pelanggan = [
    pelanggan1,
    pelanggan2
]

for pelanggan in daftar_pelanggan:
    pelanggan.tampilkan_info_pelanggan()
print("-" * 40)

# Data Transaksi
print("Data Transaksi")

# asosiasi dan komposisi
transaksi1 = Transaksi(
    pelanggan1,
    kartu1,
    2
)

transaksi2 = Transaksi(
    pelanggan2,
    kartu2,
    1
)

daftar_transaksi = [
    transaksi1,
    transaksi2
]

for transaksi in daftar_transaksi:
    transaksi.tampilkan_info_transaksi()
print("-" * 40)

# uji duck typing
print("Uji Duck Typing")
qris = PembayaranQRIS()
tunai = PembayaranTunai()

bayar_pesanan(qris, 15000000)
bayar_pesanan(tunai, 10000000)
print("-" * 40)