posttest 2 PBO

Sistem Penjualan dan Inventaris TCG
Program ini merupakan sistem sederhana untuk penjualan dan inventaris kartu Trading Card Game (TCG) menggunakan konsep Object-Oriented Programming (OOP) dengan bahasa Python.

Melanjutkan dari posttest sebelumnya, program ini dibuat untuk memenuhi penerapan inheritance serta hubungan antar-class berupa association, aggregation, dan composition.


1. Inheritance

Inheritance diterapkan dengan membuat class KartuTCG sebagai superclass, kemudian membuat dua subclass yaitu:
"KartuPokemon"
"KartuOnePiece"

"KartuPokemon" dan "KartuOnePiece" mewarisi atribut dan method yang dimiliki oleh "KartuTCG". Dengan inheritance, informasi dasar yang sama seperti nama kartu, jenis TCG, harga, dan stok tidak perlu dibuat ulang dari awal pada setiap subclass.

Pada constructor masing-masing subclass digunakan "super().__init__()" untuk menjalankan constructor dari superclass.
Contohnya pada KartuPokemon:

"super().__init__(nama, "Pokemon", harga, stok)"

Sedangkan pada KartuOnePiece:

"super().__init__(nama, "One Piece", harga, stok)"

Selain mewarisi atribut dari superclass, setiap subclass juga memiliki atribut spesifik berupa:

"seri_kartu"

"kelangkaan"

Atribut tersebut digunakan untuk menyimpan informasi tambahan mengenai kartu.

Inheritance juga menerapkan method overriding. Method "tampilkan_info_kartu()" yang terdapat pada "KartuTCG" ditulis kembali pada "KartuPokemon" dan "KartuOnePiece". Tujuannya agar masing-masing subclass dapat menampilkan informasi kartu beserta atribut tambahannya.

Superclass juga menggunakan atribut protected _nama. Atribut tersebut dapat diakses oleh subclass ketika menampilkan informasi kartu.


2. Association

Association diterapkan pada hubungan antara Transaksi dengan Pelanggan dan KartuTCG.

Pada saat membuat objek Transaksi, objek pelanggan dan kartu diberikan sebagai parameter:

"transaksi1 = Transaksi(

    pelanggan1,

    kartu1,

    2

)"

Di dalam class Transaksi, objek tersebut kemudian disimpan:

"self.pelanggan = pelanggan"

"self.kartu = kartu"


Hubungan ini termasuk association karena Transaksi hanya menggunakan objek Pelanggan dan KartuTCG yang sudah dibuat sebelumnya.

Objek pelanggan dan kartu tidak dibuat oleh Transaksi. Keduanya dapat tetap ada dan digunakan di luar objek transaksi.

Dengan demikian, hubungan sederhananya seperti berikut:

Transaksi ───── Pelanggan

         │

         └───────── KartuTCG



3. Aggregation

Aggregation diterapkan pada hubungan antara Toko dengan KartuTCG.

Class Toko memiliki sebuah daftar untuk menyimpan kartu:

"self.daftar_kartu = []"

Kartu kemudian ditambahkan ke dalam toko menggunakan method:

"toko1.tambah_kartu(kartu1)"

"toko1.tambah_kartu(kartu2)"

"toko1.tambah_kartu(kartu3)"

Kartu-kartu tersebut dibuat terlebih dahulu di luar class Toko. Setelah itu, objek kartu diberikan kepada Toko untuk dimasukkan ke dalam "daftar_kartu".

Hal ini menunjukkan hubungan aggregation karena Toko memiliki atau menyimpan kumpulan kartu, tetapi objek kartu tetap dapat berdiri sendiri tanpa harus dibuat oleh Toko.

Hubungannya dapat digambarkan sebagai berikut:

Toko ◇──────── KartuTCG

Simbol belah ketupat kosong menunjukkan adanya hubungan aggregation.


4. Composition

Composition diterapkan pada hubungan antara Transaksi dengan DetailTransaksi.

Class DetailTransaksi digunakan untuk menyimpan informasi kartu dan jumlah yang dibeli:

"class DetailTransaksi:

    def __init__(self, kartu, jumlah):

        self.kartu = kartu

        self.jumlah = jumlah"

Berbeda dengan association dan aggregation, objek DetailTransaksi dibuat langsung di dalam class Transaksi:

"self.detail = DetailTransaksi(kartu, jumlah)"

Artinya, ketika objek Transaksi dibuat, objek DetailTransaksi juga dibuat sebagai bagian dari transaksi tersebut.

Hubungannya dapat digambarkan sebagai:

Transaksi ◆──────── DetailTransaksi

Simbol belah ketupat penuh menunjukkan adnya hubungan composition.

Pada program ini, DetailTransaksi digunakan sebagai bagian dari Transaksi untuk menyimpan jumlah kartu yang dibeli dan kemudian digunakan dalam perhitungan total harga.