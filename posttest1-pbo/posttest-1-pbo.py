# TEMA/JUDUL: Sistem Penjualan dan Inventaris TCG

class toko:
    status_toko = "Buka"

    def __init__(self, nama_toko, alamat_toko):
        self.__nama_toko = nama_toko
        self.alamat_toko = alamat_toko

    @property
    def nama_toko(self):
        return self.__nama_toko

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


class kartuTCG:
    total_kartu = 0

    def __init__(self, nama, jenis_tcg, harga, stok):
        self.nama = nama
        self.jenis_tcg = jenis_tcg
        self.harga = harga
        self.__stok = stok

        kartuTCG.total_kartu += 1

    def tampilkan_info_kartu(self):
        print("Nama Kartu: ", self.nama)
        print("Jenis TCG: ", self.jenis_tcg)
        print("Harga: Rp", self.harga)
        print("Stok: ", self.stok)

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            raise ValueError("Stok tidak boleh negatif.")

        self.__stok = stok_baru


class Pelanggan:
    def __init__(self, nama_pelanggan, id_pelanggan):
        self.nama_pelanggan = nama_pelanggan
        self.id_pelanggan = id_pelanggan

    def tampilkan_info_pelanggan(self):
        print("Nama Pelanggan: ", self.nama_pelanggan)
        print("ID Pelanggan: ", self.id_pelanggan)


class Transaksi:
    def __init__(self, pelanggan, kartuTCG, jumlah):
        self.pelanggan = pelanggan
        self.kartuTCG = kartuTCG
        self.__jumlah = jumlah

    def tampilkan_info_transaksi(self):
        total_harga = self.kartuTCG.harga * self.jumlah

        print("Pelanggan: ", self.pelanggan.nama_pelanggan)
        print("Kartu TCG: ", self.kartuTCG.nama)
        print("Jumlah: ", self.jumlah)
        print("Total Harga: Rp", total_harga)

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, jumlah_baru):
        if jumlah_baru <= 0:
            raise ValueError("Jumlah harus lebih dari 0.")

        self.__jumlah = jumlah_baru

# Main Program
print("Sistem Penjualan dan Inventaris TCG")

# Data Toko
print("\nData Toko:")

toko1 = toko("IlhamGOD TCG Store", "Samarinda")
toko2 = toko("IlhamGOD TCG Store", "Balikpapan")

daftar_toko = [toko1, toko2]

for data_toko in daftar_toko:
    data_toko.tampilkan_info_toko()
    print()

# Class Method
print("Class Method:")

toko.ubah_status_toko("Tutup")
print("Status Toko:", toko.status_toko)

# Static Method
print("\nStatic Method:")

print("Stok 5:", toko.cek_stok(5))
print("Stok 0:", toko.cek_stok(0))

# Data Kartu TCG
print("\nData Kartu TCG:")

kartu1 = kartuTCG(
    "Charizard",
    "Pokemon",
    1500000,
    5
)

kartu2 = kartuTCG(
    "Monkey D. Luffy",
    "One Piece",
    2000000,
    3
)

kartu3 = kartuTCG(
    "Blue-Eyes White Dragon",
    "Yu-Gi-Oh!",
    25000000,
    5
)

daftar_kartu = [kartu1, kartu2, kartu3]

for kartu in daftar_kartu:
    kartu.tampilkan_info_kartu()
    print()

print("Total Kartu:", kartuTCG.total_kartu)

# Property Getter
print("\nProperty Getter:")

print("Nama Toko:", toko1.nama_toko)

for kartu in daftar_kartu:
    print("Stok", kartu.nama, ":", kartu.stok)


# Property Setter Valid dan Invalid
print("\nProperty Setter Valid:")

kartu1.stok = 10

print("Stok Kartu 1 setelah diubah:", kartu1.stok)

print("\nProperty Setter Invalid:")

try:
    kartu2.stok = -5
except ValueError as e:
    print("Error:", e)

# Data Pelanggan
print("\nData Pelanggan:")

pelanggan1 = Pelanggan("Herlambang", "P001")
pelanggan2 = Pelanggan("Joseph", "P002")

daftar_pelanggan = [pelanggan1, pelanggan2]

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

daftar_transaksi = [transaksi1, transaksi2]

for transaksi in daftar_transaksi:
    transaksi.tampilkan_info_transaksi()
    print()

# Property Getter dan Setter Transaksi
print("Property Transaksi:")

# Property getter
print("Jumlah Transaksi 1:", transaksi1.jumlah)

# Setter valid
transaksi1.jumlah = 3

print("Jumlah setelah diubah:", transaksi1.jumlah)

# Setter invalid
try:
    transaksi2.jumlah = 0
except ValueError as e:
    print("Error:", e)