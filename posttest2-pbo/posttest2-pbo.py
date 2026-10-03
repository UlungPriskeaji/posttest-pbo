# TEMA/JUDUL: Sistem Penjualan dan Inventaris TCG


# superclass KartuTCG
class KartuTCG:
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

    def tampilkan_info_kartu(self):
        print("Nama Kartu: ", self._nama)
        print("Jenis TCG: ", self.jenis_tcg)
        print("Harga: Rp", self._harga)
        print("Stok: ", self.stok)


# subclass KartuPokemon & KartuOnePiece
class KartuPokemon(KartuTCG):

    def __init__(self, nama, harga, stok, seri_kartu, kelangkaan):
        super().__init__(nama, "Pokemon", harga, stok)

        # atribut spesifik KartuPokemon
        self.seri_kartu = seri_kartu
        self.kelangkaan = kelangkaan

    # overriding
    def tampilkan_info_kartu(self):
        print("Nama Kartu: ", self._nama)
        print("Jenis TCG: ", self.jenis_tcg)
        print("Harga: Rp", self._harga)
        print("Stok: ", self.stok)
        print("Seri Kartu: ", self.seri_kartu)
        print("Kelangkaan: ", self.kelangkaan)


class KartuOnePiece(KartuTCG):

    def __init__(self, nama, harga, stok, seri_kartu, kelangkaan):
        super().__init__(nama, "One Piece", harga, stok)

        # atribut spesifik KartuOnePiece
        self.seri_kartu = seri_kartu
        self.kelangkaan = kelangkaan

    # overriding
    def tampilkan_info_kartu(self):
        print("Nama Kartu: ", self._nama)
        print("Jenis TCG: ", self.jenis_tcg)
        print("Harga: Rp", self._harga)
        print("Stok: ", self.stok)
        print("Seri Kartu: ", self.seri_kartu)
        print("Kelangkaan: ", self.kelangkaan)


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


# main program
print("Sistem Penjualan dan Inventaris TCG")


# Data Toko
print("\nData Toko:")

toko1 = Toko(
    "IlhamGOD TCG Store",
    "Samarinda"
)

toko2 = Toko(
    "IlhamGOD TCG Store",
    "Balikpapan"
)

daftar_toko = [toko1, toko2]

for data_toko in daftar_toko:
    data_toko.tampilkan_info_toko()
    print()


# class method
print("Class Method:")

Toko.ubah_status_toko("Tutup")

print("Status Toko:", Toko.status_toko)


# static method
print("\nStatic Method:")

print("Stok 5:", Toko.cek_stok(5))
print("Stok 0:", Toko.cek_stok(0))


# Data Kartu TCG
print("\nData Kartu TCG:")

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
    "Winged Kuriboh",
    32000,
    100,
    "TLM-EN005",
    "Super Rare"
)

daftar_kartu = [kartu1, kartu2, kartu3]


# agregasi
toko1.tambah_kartu(kartu1)
toko1.tambah_kartu(kartu2)
toko1.tambah_kartu(kartu3)


for kartu in daftar_kartu:
    kartu.tampilkan_info_kartu()
    print()

print("Total Kartu:", KartuTCG.total_kartu)


# property getter
print("\nProperty Getter:")

print("Nama Toko:", toko1.nama_toko)

for kartu in daftar_kartu:
    print("Stok", kartu.nama, ":", kartu.stok)


# Property Setter Valid
print("\nProperty Setter Valid:")

kartu1.stok = 10

print("Stok Kartu 1 setelah diubah:", kartu1.stok, "(stok)")


# Property Setter Invalid
print("\nProperty Setter Invalid:")

try:
    kartu2.stok = -5
except ValueError as e:
    print("Error:", e)


# Data Pelanggan
print("\nData Pelanggan:")

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
    print()


# Data Transaksi
print("Data Transaksi:")

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
    print()