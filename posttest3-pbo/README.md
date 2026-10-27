# Sistem Penjualan dan Inventaris TCG

## Deskripsi Program

Program ini merupakan sistem sederhana untuk mengelola penjualan dan inventaris toko kartu Trading Card Game (TCG), khususnya kartu Pokemon dan One Piece. Program mencakup pengelolaan data toko, data kartu beserta stoknya, data pelanggan, dan transaksi pembelian.

Class yang digunakan adalah `KartuTCG` (abstract class), `KartuPokemon`, `KartuOnePiece`, `Toko`, `Pelanggan`, `Transaksi`, `DetailTransaksi`, `PembayaranQRIS`, dan `PembayaranTunai`.

---

## 1. Relasi UML (Class Diagram)

![Gambar 1. Class Diagram](png/uml.png)

Diagram UML di atas menggambarkan kelas-kelas yang digunakan dalam program beserta atribut, method, dan hubungan antar kelasnya. Dalam diagram ini terdapat empat jenis hubungan, yaitu asosiasi, agregasi, komposisi, dan pewarisan. Selain itu, terdapat juga *multiplicity* yang menunjukkan jumlah objek yang dapat terlibat dalam suatu hubungan. Angka `1` berarti tepat satu objek, sedangkan `0..*` berarti bisa tidak ada objek sama sekali atau bisa lebih dari satu objek.

**Asosiasi (`Transaksi` → `Pelanggan` dan `Transaksi` → `KartuTCG`)**

Pada program ini, kelas `Transaksi` menggunakan objek dari kelas `Pelanggan` dan `KartuTCG`. Kedua objek tersebut dibuat di luar kelas `Transaksi`, kemudian dimasukkan melalui constructor dan disimpan pada atribut `self.pelanggan` dan `self.kartu`.

Hubungan ini termasuk asosiasi karena objek pelanggan dan kartu dapat berdiri sendiri meskipun objek transaksi sudah tidak ada.

Pada hubungan `Transaksi` dengan `Pelanggan`, angka `1` yang berada di dekat kelas `Pelanggan` menunjukkan bahwa setiap transaksi hanya melibatkan satu pelanggan. Sementara itu, angka `0..*` di dekat kelas `Transaksi` berarti satu pelanggan bisa saja belum pernah melakukan transaksi atau sudah melakukan banyak transaksi.

Hal yang sama juga berlaku pada hubungan `Transaksi` dengan `KartuTCG`. Angka `1` di dekat `KartuTCG` berarti setiap transaksi hanya menggunakan satu jenis kartu, sedangkan `0..*` di dekat `Transaksi` berarti satu objek kartu dapat digunakan dalam beberapa transaksi atau belum pernah digunakan sama sekali.

**Agregasi (`Toko` ◇— `KartuTCG`)**

Kelas `Toko` memiliki list `daftar_kartu` yang digunakan untuk menyimpan kumpulan objek kartu. Kartu tersebut ditambahkan menggunakan method `tambah_kartu()`. Objek kartu dibuat secara terpisah dari toko, sehingga ketika objek toko dihapus, kartu tersebut masih bisa digunakan.

Hubungan ini termasuk agregasi karena objek kartu tidak bergantung sepenuhnya pada objek toko. Pada diagram, angka `0..*` di dekat kelas `KartuTCG` menunjukkan bahwa satu toko bisa memiliki banyak kartu atau belum memiliki kartu sama sekali. Sementara itu, angka `0..*` di dekat kelas `Toko` berarti satu kartu bisa terdaftar pada beberapa toko atau tidak terdaftar pada toko mana pun. Hal ini memungkinkan karena program tidak membatasi satu kartu hanya untuk satu toko.

**Komposisi (`Transaksi` ◆— `DetailTransaksi`)**

Pada kelas `Transaksi`, objek `DetailTransaksi` dibuat langsung di dalam constructor. Objek ini digunakan untuk menyimpan informasi kartu dan jumlah pembelian dalam suatu transaksi.

Hubungan ini termasuk komposisi karena detail transaksi merupakan bagian dari transaksi itu sendiri dan keberadaannya bergantung pada objek `Transaksi`.

Pada diagram, kedua kelas memiliki angka `1`. Angka `1` di dekat `DetailTransaksi` menunjukkan bahwa setiap transaksi memiliki tepat satu detail transaksi. Sementara itu, angka `1` di dekat `Transaksi` berarti setiap detail transaksi hanya menjadi bagian dari satu transaksi. Jadi, hubungan kedua kelas ini bersifat satu banding satu atau *one-to-one*.

**Pewarisan (`KartuPokemon` dan `KartuOnePiece` → `KartuTCG`)**

Kelas `KartuPokemon` dan `KartuOnePiece` merupakan turunan dari kelas `KartuTCG`. Kedua kelas tersebut mewarisi atribut dan method yang dimiliki oleh kelas induknya.

Kelas `KartuTCG` dibuat sebagai abstract class yang memiliki dua abstract method, yaitu `tampilkan_info_kartu()` dan `hitung_value_stok()`. Kedua method tersebut kemudian diimplementasikan kembali pada masing-masing subclass sesuai dengan jenis kartunya.

Pada diagram UML, hubungan pewarisan ditunjukkan dengan garis yang memiliki ujung segitiga kosong mengarah ke kelas `KartuTCG`. Berbeda dengan hubungan sebelumnya, pewarisan tidak menggunakan angka multiplicity karena hubungan ini menunjukkan hubungan antara kelas induk dan kelas turunan, bukan jumlah objek yang saling terhubung.

---

## 2. Abstraksi (Abstract Base Class)

Kelas `KartuTCG` dibuat menggunakan `ABC` dengan rincian sebagai berikut:

- Dua abstract method, yaitu `tampilkan_info_kartu()` dan `hitung_value_stok()`.
- Satu method konkret, yaitu `jalankan()`, yang digunakan bersama oleh seluruh subclass.

Subclass `KartuPokemon` dan `KartuOnePiece` mengimplementasikan seluruh abstract method tersebut. Konsep inheritance dari posttest sebelumnya tetap digunakan:

- Pemanggilan `super().__init__(...)` pada constructor setiap subclass.
- Atribut unik masing-masing subclass, yaitu `seri_kartu` dan `kelangkaan`.
- Atribut protected: `_nama` dan `_harga`.
- Atribut private: `__stok` (diakses melalui property) dan `__nama_toko`.

### Bukti Abstract Class Tidak Dapat Diinstansiasi

Objek `KartuTCG` dicoba dibuat secara langsung di dalam blok `try-except TypeError`.

![Gambar 2. Bukti abstraksi](png/2.png)

**Output:**

![Gambar 3. Output](png/3.png)


**Keterangan:**
Kesalahan `TypeError` muncul saat objek dibuat, bukan saat method dipanggil. Dengan demikian, kelas yang implementasinya belum lengkap dapat terdeteksi sejak awal.

---

## 3. Polimorfisme

### a. Polimorfisme melalui Pewarisan

Method `tampilkan_info_kartu()` dan `hitung_value_stok()` di-override oleh `KartuPokemon` dan `KartuOnePiece`. Kedua method dipanggil melalui satu perulangan yang berisi objek dari dua subclass berbeda.

![Gambar 4. Polimorfisme melalui pewarisan](png/4.png)

**Keterangan:**
Pada perulangan `for kartu in daftar_kartu` tidak terdapat pengecekan jenis kartu. Python memilih method milik masing-masing subclass pada saat program dijalankan.

### b. Duck Typing

Kelas `PembayaranQRIS` dan `PembayaranTunai` tidak memiliki hubungan pewarisan, tetapi keduanya memiliki method `proses_pembayaran()`. Kedua objek dipanggil melalui fungsi yang sama, yaitu `bayar_pesanan()`.

![Gambar 5. Duck typing](png/5.png)

**Output:**

![Gambar 5b. Output Duck typing](png/5b.png)

**Keterangan:**
Fungsi `bayar_pesanan()` tidak bergantung pada tipe objek, melainkan pada keberadaan method `proses_pembayaran()`.

### c. Operator Overloading

Kelas `KartuTCG` mendefinisikan method `__add__()` sehingga dua objek kartu dapat dijumlahkan menggunakan operator `+`.

![Gambar 6. Operator overloading](png/6.png)

**Output:**

![Gambar 6b. Output Operator overloading](png/6b.png)

**Keterangan:**
Ekspresi `kartu1 + kartu3` menghasilkan jumlah harga kedua kartu, yaitu Rp 101.100.000.

### d. Larangan Anti-Pattern

Program ini tidak menggunakan rantai `if` / `elif` yang memeriksa `type()` atau string jenis kartu untuk membedakan perilaku objek. Setiap objek menentukan perilakunya sendiri melalui method. Fungsi `isinstance()` hanya digunakan pada `__add__()` untuk memastikan kedua operand merupakan kartu.

---

## 4. Pengujian Fitur Lainnya

Bagian ini menguji fitur lain yang ada di program, yaitu relasi antar objek, class method, static method, dan property. Setiap pengujian terdiri dari kode yang dijalankan, output program, dan keterangan hasilnya.

### a. Pengujian Relasi (Agregasi, Asosiasi, dan Komposisi)

Pengujian ini menunjukkan ketiga relasi pada diagram berjalan di kode. Kartu dimasukkan ke dalam toko (agregasi), lalu objek `Transaksi` dibuat dari pelanggan dan kartu (asosiasi) yang secara otomatis membuat `DetailTransaksi` di dalamnya (komposisi).

![Gambar 7. Pengujian relasi](png/7.png)

**Output:**

![Gambar 8. output Pengujian relasi](png/8.png)

**Keterangan:**
Setiap transaksi menampilkan nama pelanggan, nama kartu, jumlah, dan total harga. Total harga dihitung dari harga kartu dikalikan jumlah pembelian yang tersimpan di `DetailTransaksi`.

### b. Pengujian Class Method dan Static Method
 
Method `ubah_status_toko()` adalah class method yang mengubah atribut class `status_toko`. Method `cek_stok()` adalah static method yang tidak memakai `self` maupun `cls`.

![Gambar 9. Class method dan static method](png/9.png)

**Output:**

![Gambar 9b. output Class method dan static method](png/9b.png)

**Keterangan:**
Status toko berubah menjadi "Tutup" untuk seluruh toko karena menggunakan atribut class. Method `cek_stok()` mengembalikan "Stok tersedia" apabila stok lebih dari 0 dan "Stok habis" apabila stok 0.

### c. Pengujian Property Getter dan Setter

Atribut `__stok` bersifat private sehingga diakses melalui property `stok`. Setter memvalidasi bahwa stok tidak boleh negatif.

![Gambar 10. Property getter dan setter](png/10.png)

**Output:**

![Gambar 10b. Output Property getter dan setter](png/10b.png)

**Keterangan:**
Stok kartu 1 berhasil diubah menjadi 10 karena nilainya valid. Ketika stok kartu 2 diisi `-5`, program menampilkan `ValueError` ("Stok tidak boleh negatif.") dan nilai stok sebelumnya tetap tersimpan.

---

## Prinsip SOLID

Program ini menerapkan prinsip Open/Closed Principle (OCP) dan Liskov Substitution Principle (LSP), serta pendekatan yang mendukung Dependency Inversion Principle (DIP).

| Prinsip | Bagian Kode |
|---|---|
| Open/Closed Principle (OCP) | `bayar_pesanan()` dan `KartuTCG` |
| Liskov Substitution Principle (LSP) | `KartuPokemon` dan `KartuOnePiece` |
| Dependency Inversion Principle (DIP) | Parameter `metode` pada `bayar_pesanan()` |

### 1. Open/Closed Principle (OCP)

Prinsip OCP berarti program dapat ditambahkan fitur baru tanpa harus mengubah kode yang sudah ada. Contohnya, kita bisa menambahkan metode pembayaran baru selama memiliki method `proses_pembayaran()`.

```python
def bayar_pesanan(metode, jumlah):
    metode.proses_pembayaran(jumlah)
```

Selain itu, jenis kartu baru seperti `KartuYuGiOh` juga dapat ditambahkan dengan membuat subclass dari `KartuTCG` dan mengimplementasikan kedua abstract method.

### 2. Liskov Substitution Principle (LSP)

Prinsip LSP berarti subclass dapat menggantikan parent class tanpa mengganggu jalannya program. Pada program ini, `KartuPokemon` dan `KartuOnePiece` dapat digunakan dengan cara yang sama karena keduanya merupakan turunan `KartuTCG`.

```python
for kartu in daftar_kartu:
    kartu.jalankan()
    kartu.tampilkan_info_kartu()
    print("Nilai Stok: Rp", kartu.hitung_value_stok())
```

Kedua jenis kartu dapat menjalankan method tersebut tanpa perlu pengecekan tipe objek, meskipun hasilnya berbeda sesuai implementasi masing-masing.

### 3. Dependency Inversion Principle (DIP)

Prinsip DIP berarti program sebaiknya bergantung pada abstraksi, bukan kelas tertentu. Pada program ini, pendekatan yang mendukung DIP terlihat dari fungsi `bayar_pesanan()` yang menerima objek pembayaran melalui parameter `metode`.

```python
qris = PembayaranQRIS()
tunai = PembayaranTunai()

bayar_pesanan(qris, 15000000)
bayar_pesanan(tunai, 10000000)
```

Fungsi tersebut dapat menggunakan QRIS maupun tunai tanpa perlu membuat objek pembayaran sendiri. Pendekatan ini menggunakan dependency injection dan duck typing, tetapi belum sepenuhnya menerapkan DIP karena belum ada abstract class khusus untuk pembayaran.